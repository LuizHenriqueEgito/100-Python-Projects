from src.preprocess_document.base_preprocess import BasePreprocess
from src.utils_typing import PairDocuments

class LLMPreprocess(BasePreprocess):
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
