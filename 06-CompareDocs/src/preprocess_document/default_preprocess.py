from src.preprocess_document.base_preprocess import BasePreprocess
from src.document import Document


class DefaultPreprocess(BasePreprocess):
    def __init__(self):
        print(f'Preprocess: {type(self).__name__}')
    
    def processing(self, documents_pair: tuple[Document, Document]) -> tuple[Document, Document]:
        """
        docstring
        """
        for document in documents_pair:
            document.preprocess_text = {'chunck_0': document.text}
        return documents_pair
