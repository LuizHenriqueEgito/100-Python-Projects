from src.preprocess_document.base_preprocess import BasePreprocess
from src.document import Document

class MinHashPreprocess(BasePreprocess):
    def process(self, documents_pair: tuple[Document, Document]) -> tuple[Document, Document]:
        """
        docstring
        """
        if not self.requires_process(documents_pair):
            for document in documents_pair:
                document.preprocess_text = {'chunck_0': document.text}
        else:
            documents_pair = self.apply(documents_pair)
        return documents_pair
    
    def apply(self, documents_pais: tuple[Document, Document]) -> tuple[Document, Document]:
        """
        docstring
        retorna os documentos com .preprocess_text já chunckiado por similaridade
        """
        pass