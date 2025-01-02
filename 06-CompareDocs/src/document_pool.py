from itertools import combinations
from dataclasses import dataclass
# from concurrent.futures import ProcessPoolExecutor
from src.preprocess_document.base_preprocess import BasePreprocess
from src.document import Document
from src.utils_typing import PoolDocuments, PairPreprocessedDocs

# from configs import N_DOCS_TO_COMPARE

def generate_pool(documents: list[Document], n_docs: int = 2) -> PoolDocuments:
    return list(
        combinations(documents, n_docs)
    )


# class DocumentPool:
#     def __init__(
#         self, 
#         preprocess: BasePreprocess, 
#         documents: list[Document]
#     ):
#         self.preprocess = preprocess
#         self.documents = documents
#         self.documents_to_compare = self.combines_documents()

#     def combines_documents(self) -> list[tuple[Document, Document]]:
#         return list(combinations(self.documents, N_DOCS_TO_COMPARE))

#     def preprocess_pool(self) -> list:
#         with ProcessPoolExecutor() as executor:
#             results = list(
#                 executor.map(
#                     self.process_pair,
#                     [doc_pair for doc_pair in self.documents_to_compare]
#                 )
#             )
#         self.documents_to_compare = results
#         return results

#     def process_pair(self, doc_pair):
#         return self.preprocess.processing(doc_pair)
