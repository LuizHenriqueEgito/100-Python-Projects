from src.preprocess_document.base_preprocess import BasePreprocess
from src.document import Document


class DefaultPreprocess(BasePreprocess):
    def process(self, documents_pair: tuple[Document, Document]) -> tuple[Document, Document]:
        """
        docstring
        """
        for document in documents_pair:
            document.preprocess_text = {'chunck_0': document.text}
            # document.preprocess_text = document.text
            print(document.preprocess_text)
        return documents_pair
