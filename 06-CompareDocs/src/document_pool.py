from itertools import combinations
from concurrent.futures import ProcessPoolExecutor
from src.preprocess_document.base_preprocess import BasePreprocess
from src.document import Document


N_DOCS_TO_COMPARE = 2  # nº documentos a serem comparados

class DocumentPool:
    def __init__(
        self, 
        preprocess: BasePreprocess, 
        documents: list[Document]
    ):
        self.preprocess = preprocess
        self.documents = documents
        self.documents_to_compare = self.combines_documents()

    def combines_documents(self) -> list[tuple[Document, Document]]:
        return list(combinations(self.documents, N_DOCS_TO_COMPARE))

    def preprocess_pool(self) -> list:
        with ProcessPoolExecutor() as executor:
            results = list(executor.map(self.process_pair, self.documents_to_compare, [self.preprocess] * len(self.documents_to_compare)))
        return results

    @staticmethod
    def process_pair(doc_pair, preprocess: BasePreprocess):
        return preprocess.process(doc_pair)