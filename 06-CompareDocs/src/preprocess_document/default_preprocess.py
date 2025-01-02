from src.preprocess_document.base_preprocess import BasePreprocess
from src.utils_typing import PairDocuments

class DefaultPreprocess(BasePreprocess):
    """
    eu quero que saia 
    return (
        {
            'id': '123',
            'text_grouped_by_topics': {
                'topico 1': 'text do topico 1',
                'topico 2': 'text do topico 2',
                'topico 3': 'text do topico 3'
            }
        }, 
        {
            id: '456',
            'text_grouped_by_topics': {
                'topico 1': 'text topico 1',
                'topico 2': 'text topico 2',
                'topico 3': 'text topico 3'
            }
        }
    )
    """
    def process(self, documents_pair: PairDocuments) -> tuple[dict[str, str]]:
        processed_documents = tuple(
            {
                'id': document.id,
                'text_grouped_by_topics': {
                    'TEXTO COMPLETO': document.text
                }
            }
            for document in documents_pair
        )
        return processed_documents
