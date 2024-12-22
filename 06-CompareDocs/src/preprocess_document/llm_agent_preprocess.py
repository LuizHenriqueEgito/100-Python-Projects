from src.preprocess_document.base_preprocess import BasePreprocess
from src.document import Document

class LLMPreprocess(BasePreprocess):
    def process(self, documents_pair: tuple[Document, Document]) -> tuple[Document, Document]:
        if self.requires_process(documents_pair):
            print(f"Processing pair: {documents_pair}")
            documents_pair[0].preprocess_text = 'LLM PREPROCESS \n\n\n' + documents_pair[0].text
            documents_pair[1].preprocess_text = 'LLM PREPROCESS \n\n\n' + documents_pair[1].text
            return documents_pair
        return documents_pair