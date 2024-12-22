if __name__ == '__main__':
    from src.parse_event import EventInput
    from src.document import Document
    from src.document_pool import DocumentPool
    from src.preprocess_document import FactoryPreprocessDoc
    from src.joogle_ditto import JoogleDitto
    from pathlib import Path

    event = {
        'body': {
            'method': 'llm',
            'model': 'modelo xpto',
            'documents': [
                {
                    'id': '1', 
                    'text': Path('data/documentA.txt').read_text(encoding='utf-8')
                },
                {
                    'id': '2', 
                    'text': Path('data/documentB.txt').read_text(encoding='utf-8')
                },
                {
                    'id': '3', 
                    'text': Path('data/documentA-inverse.txt').read_text(encoding='utf-8')
                },
                {
                    'id': '4', 
                    'text': Path('data/documentB-inverse.txt').read_text(encoding='utf-8')
                }
            ]
        }
    }
    event_input = EventInput.parse_event(event)
    documents = [
        Document(**document) for document in event_input.documents
    ]
    preprocess = FactoryPreprocessDoc.get_preprocess(preprocessor=event_input.method)
    documents_pool = DocumentPool(
        preprocess=preprocess,
        documents=documents
    )
    documents_to_compare = documents_pool.combines_documents()
    print(documents_to_compare)
    print(documents_pool.preprocess_pool())
    # ditto = JoogleDitto(documents_to_compare)
    # result = ditto.compare()
    
    