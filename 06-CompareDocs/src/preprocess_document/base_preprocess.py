from abc import ABC, abstractmethod
from src.document import Document

class BasePreprocess(ABC):
    @abstractmethod
    def process(self, documents_pair: tuple[Document, Document]) -> dict:  # defina o que deve retornar
        pass

    def requires_process(self, documents_pair: tuple[Document, Document]) -> bool:
        if not all([doc.small_doc for doc in documents_pair]):
            return True
        return False