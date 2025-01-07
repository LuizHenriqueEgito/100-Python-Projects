from itertools import product
import re
from datasketch import MinHash
from src.preprocess_document.base_preprocess import BasePreprocess
from src.utils_typing import PairDocuments


class TrieNode:
    """Representa um nó de uma árvore Trie."""
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class PrefixTrie:
    """Implementação de uma Trie para gerenciamento de prefixos."""
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        """Insere uma palavra na Trie."""
        node = self.root
        for char in word:
            node = node.children.setdefault(char, TrieNode())
        node.is_end_of_word = True

    def get_words(self, node=None, prefix="") -> list[str]:
        """Retorna todas as palavras armazenadas na Trie."""
        if node is None:
            node = self.root
        words = [prefix] if node.is_end_of_word else []
        for char, child in node.children.items():
            words.extend(self.get_words(child, prefix + char))
        return words


def tokenize(text: str) -> list[str]:
    """Divide o texto em tokens, removendo pontuações e convertendo para minúsculas."""
    return re.findall(r'\b\w+\b', text.lower())


def trie_similarity(trie1: PrefixTrie, trie2: PrefixTrie) -> float:
    """
    Calcula a similaridade entre duas Tries usando a métrica de Jaccard.
    """
    words1, words2 = set(trie1.get_words()), set(trie2.get_words())
    intersection = len(words1 & words2)
    union = len(words1 | words2)
    return intersection / union if union > 0 else 0.0


def trie_similarity_from_texts(text1: str, text2: str) -> float:
    """
    Calcula a similaridade entre dois textos usando Tries.
    """
    trie1, trie2 = PrefixTrie(), PrefixTrie()
    for token in tokenize(text1):
        trie1.insert(token)
    for token in tokenize(text2):
        trie2.insert(token)
    return trie_similarity(trie1, trie2)


class PrefixTriePreprocess(BasePreprocess):
    """Classe para preprocessamento utilizando Tries."""
    
    def process(self, documents_pair: PairDocuments) -> PairDocuments:
        """
        Preprocessa o par de documentos, dividindo-os em partes e calculando similaridades.
        """
        if not self.requires_process(documents_pair):
            for document in documents_pair:
                document.preprocess_text = {"chunk_0": document.text}
            return documents_pair

        return self.apply(documents_pair)

    def apply(self, documents_pair: PairDocuments) -> PairDocuments:
        """
        Aplica o preprocessamento baseado em Tries aos documentos.
        """
        dict_text_parts = [
            (document.id, self.split_text_into_n_parts(document.text))
            for document in documents_pair
        ]
        (id_i, parts_i), (id_j, parts_j) = dict_text_parts
        trie_scores = self.pair_similar_parts(parts_i, parts_j)
        trie_scores = self.sort_scores(trie_scores)

        grouped_topics_i, grouped_topics_j = {}, {}
        for idx, (_, part_i, part_j) in enumerate(trie_scores, start=1):
            topic_key = f"topic_{idx}"
            grouped_topics_i[topic_key] = parts_i.get(part_i)
            grouped_topics_j[topic_key] = parts_j.get(part_j)

        return (
            {"id": id_i, "text_grouped_by_topics": grouped_topics_i},
            {"id": id_j, "text_grouped_by_topics": grouped_topics_j},
        )

    def pair_similar_parts(self, parts_i: dict, parts_j: dict) -> list[tuple[float, str, str]]:
        """
        Encontra pares de partes mais similares entre dois dicionários de texto.
        """
        scores = [
            (trie_similarity_from_texts(text_i, text_j), part_i, part_j)
            for (part_i, text_i), (part_j, text_j) in product(parts_i.items(), parts_j.items())
        ]
        scores.sort(reverse=True, key=lambda x: x[0])

        paired, used_i, used_j = [], set(), set()
        for score, part_i, part_j in scores:
            if part_i not in used_i and part_j not in used_j:
                paired.append((score, part_i, part_j))
                used_i.add(part_i)
                used_j.add(part_j)

        remaining_i = set(parts_i) - used_i
        remaining_j = set(parts_j) - used_j
        paired.extend((0.0, part, None) for part in remaining_i)
        paired.extend((0.0, None, part) for part in remaining_j)

        return paired

    @staticmethod
    def sort_scores(scores: list[tuple[float, str, str]]) -> list[tuple[float, str, str]]:
        """Ordena os pares de similaridade pela posição original das partes."""
        return sorted(scores, key=lambda x: int(x[1].split('_')[1]) if x[1] else float('inf'))