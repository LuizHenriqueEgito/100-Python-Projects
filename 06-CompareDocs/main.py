if __name__ == '__main__':
    from src.parse_event import EventInput
    from src.document import Document
    from src.document_pool import DocumentPool
    from src.preprocess_document import FactoryPreprocessDoc
    from src.joogle_ditto import JoogleDitto
    from pathlib import Path

    event = {
        'body': {
            'method': 'default',
            'model': 'modelo xpto',
            'user_topics': ['Ação', 'Autor'],
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
    # Faz o parse do evento
    event_input = EventInput.parse_event(event)
    # Adiciona os documentos em uma lista
    documents = [
        Document(**document) for document in event_input.documents
    ]
    # Crie o método de preprocessamento
    preprocess = FactoryPreprocessDoc.get_preprocess(  # TODO: reveja o método default e já mapeie como fazer os proximos
        preprocessor_method=event_input.method,
        user_topics=event_input.user_topics  # TODO: Adicione o user_topics
    )
    # Faz um pool de documentos
    documents_pool = DocumentPool(
        preprocess=preprocess,
        documents=documents
    )
    # Organiza os documentos para comparação
    documents_to_compare = documents_pool.preprocess_pool()
    # Faz a comparação dos documentos
    joogle_ditto = JoogleDitto(
        documents_to_compare=documents_to_compare,
        user_topics=event_input.user_topics
    )
    comparison_between_docs = joogle_ditto.compare()
    print(comparison_between_docs[0])
    # return comparison_between_docs
