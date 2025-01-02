from abc import ABC, abstractmethod
from src.utils_typing import PairDocuments, PairPreprocessedDocs, PoolDocuments
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

class BasePreprocess(ABC):
    def __init__(self):
        print(f'Preprocess: {type(self).__name__}')
    
    @abstractmethod
    def process(
        self,
        documents_pair: PairDocuments,
        user_topics: list[str] | None = None
    ) -> dict:
        pass

    def requires_process(self, documents_pair: PairDocuments) -> bool:
        return not all(doc.small_doc for doc in documents_pair)
    
    def parallel_processing(
            self, 
            documents_pool: PoolDocuments
    ) -> list[PairPreprocessedDocs]:
        with ProcessPoolExecutor() as executor:
            result_preprocess = list(
                executor.map(
                    self.process,
                    [documents_pair for documents_pair in documents_pool]
                )
            )
        return result_preprocess