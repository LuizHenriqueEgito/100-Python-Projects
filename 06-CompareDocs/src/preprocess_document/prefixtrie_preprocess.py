from src.preprocess_document.base_preprocess import BasePreprocess
from src.utils_typing import PairDocuments

class PrefixTriePreprocess(BasePreprocess):
    def process(self, documents_pair: PairDocuments) -> PairDocuments:
        """
        docstring
        """
        if not self.requires_process(documents_pair):
            for document in documents_pair:
                document.preprocess_text = {'chunck_0': document.text}
        else:
            documents_pair = self.apply(documents_pair)
        return documents_pair
    
    def apply(self, documents_pais: PairDocuments) -> PairDocuments:
        """
        docstring
        retorna os documentos com .preprocess_text já chunckiado por similaridade
        """
        pass


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class PrefixTrie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def get_words(self, node=None, prefix=""):
        """Retorna todas as palavras armazenadas na trie."""
        if node is None:
            node = self.root
        words = []
        if node.is_end_of_word:
            words.append(prefix)
        for char, child in node.children.items():
            words.extend(self.get_words(child, prefix + char))
        return words
    
def trie_similarity(trie1, trie2):
    """
    Compara duas prefix tries e calcula a similaridade entre elas.
    
    Args:
        trie1 (PrefixTrie): Primeira trie.
        trie2 (PrefixTrie): Segunda trie.
        
    Returns:
        float: Similaridade entre as tries (0.0 a 1.0).
        dict: Estatísticas sobre a comparação.
    """
    # Obter os conjuntos de palavras armazenadas nas tries
    words1 = set(trie1.get_words())
    words2 = set(trie2.get_words())
    
    # Similaridade de Jaccard entre os conjuntos de palavras
    intersection = len(words1 & words2)
    union = len(words1 | words2)
    jaccard_similarity = intersection / union if union > 0 else 0.0

    # Comparação estrutural (nós compartilhados)
    def count_nodes(node):
        count = 1  # Contar o nó atual
        for child in node.children.values():
            count += count_nodes(child)
        return count

    nodes1 = count_nodes(trie1.root)
    nodes2 = count_nodes(trie2.root)
    
    # Nós compartilhados (caminhos comuns)
    def count_shared_nodes(node1, node2):
        if not node1 or not node2:
            return 0
        shared = 1 if node1 and node2 else 0
        for char in node1.children:
            if char in node2.children:
                shared += count_shared_nodes(node1.children[char], node2.children[char])
        return shared

    shared_nodes = count_shared_nodes(trie1.root, trie2.root)
    structural_similarity = shared_nodes / max(nodes1, nodes2) if max(nodes1, nodes2) > 0 else 0.0

    return (jaccard_similarity + structural_similarity) / 2, {
        "jaccard_similarity": jaccard_similarity,
        "structural_similarity": structural_similarity,
        "shared_nodes": shared_nodes,
        "nodes1": nodes1,
        "nodes2": nodes2
    }

import re

def tokenize(text):
    """Quebra o texto em palavras, removendo pontuações e convertendo para minúsculas."""
    return re.findall(r'\b\w+\b', text.lower())

def trie_similarity_from_texts(text1, text2):
    """
    Compara dois textos utilizando tries e calcula a similaridade entre eles.
    
    Args:
        text1 (str): Primeiro texto.
        text2 (str): Segundo texto.
        
    Returns:
        float: Similaridade entre as tries (0.0 a 1.0).
        dict: Estatísticas sobre a comparação.
    """
    # Tokenizar os textos
    tokens1 = tokenize(text1)
    tokens2 = tokenize(text2)

    # Criar as tries
    trie1 = PrefixTrie()
    trie2 = PrefixTrie()

    # Inserir tokens nas tries
    for token in tokens1:
        trie1.insert(token)
    for token in tokens2:
        trie2.insert(token)

    # Comparar as tries
    return trie_similarity(trie1, trie2)