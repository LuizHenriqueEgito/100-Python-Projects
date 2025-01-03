from typing import Self

from src.preprocess_document.lda_preprocess import LDAPreprocess
from src.preprocess_document.llm_agent_preprocess import LLMPreprocess
from src.preprocess_document.minhash_preprocess import MinHashPreprocess
from src.preprocess_document.prefixtrie_preprocess import PrefixTriePreprocess
from src.preprocess_document.default_preprocess import DefaultPreprocess


# SimpleFactory
class FactoryPreprocessDoc:
    @staticmethod
    def get_preprocess(
        preprocessor_method: str, 
        user_topics: list[str] | None = None
    ) -> Self:
        match preprocessor_method:
            case 'lda':
                return LDAPreprocess(user_topics)
            case 'minhash':
                return MinHashPreprocess(user_topics)
            case 'llm':
                return LLMPreprocess(user_topics)
            case 'trie':
                return PrefixTriePreprocess(user_topics)
            case '' | 'default':
                return DefaultPreprocess()
