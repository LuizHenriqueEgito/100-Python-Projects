from typing import Self
from src.preprocess_document.lda_preprocess import LDAPreprocess
from src.preprocess_document.llm_agent_preprocess import LLMPreprocess
from src.preprocess_document.minhash_preprocess import MinHashPreprocess
from src.preprocess_document.prefixtrie_preprocess import PrefixTriePreprocess
from src.preprocess_document.default_preprocess import DefaultPreprocess

class FactoryPreprocessDoc:
    @staticmethod
    def get_preprocess(
        preprocessor_method: str, 
        user_topics: list[str] | None = None
    ) -> Self:
        match preprocessor_method:
            case 'lda':
                print('prep: LDAPreprocess')
                return LDAPreprocess(user_topics)
            case 'minhash':
                print('prep: MinHashPreprocess')
                return MinHashPreprocess(user_topics)
            case 'llm':
                print('prep: LLMPreprocess')
                return LLMPreprocess(user_topics)
            case 'trie':
                print('prep: PrefixTriePreprocess')
                return PrefixTriePreprocess(user_topics)
            case '' | 'default':
                print('prep: DefaultPreprocess')
                return DefaultPreprocess()