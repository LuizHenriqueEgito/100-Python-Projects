from typing import Self
from src.preprocess_document.lda_preprocess import LDAPreprocess
from src.preprocess_document.llm_agent_preprocess import LLMPreprocess
from src.preprocess_document.minhash_preprocess import MinHashPreprocess
from src.preprocess_document.prefixtrie_preprocess import PrefixTriePreprocess

class FactoryPreprocessDoc:
    @staticmethod
    def get_preprocess(preprocessor: str) -> Self:
        match preprocessor:
            case 'lda':
                return LDAPreprocess()
            case 'minhash':
                return MinHashPreprocess()
            case 'llm':
                return LLMPreprocess()
            case 'trie':
                return PrefixTriePreprocess()
            case _:
                raise('No preprocess has been defined...')