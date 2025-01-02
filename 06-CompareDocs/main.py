from src.parse_event import EventInput
from src.document import Document
from src.document_pool import generate_pool  # DocumentPool
from itertools import combinations
from src.preprocess_document import FactoryPreprocessDoc
from src.joogle_ditto import JoogleDitto, DittoDocuments
from pathlib import Path
from configs import N_DOCS_TO_COMPARE, N_TOKENS_TO_SMALL_DOC
from icecream import ic
import asyncio

async def fuba(event):
    # Faz o parse do evento
    event_input = EventInput.parse_event(event)
    # Adiciona os documentos em uma lista
    documents = [
        Document(**document) 
        for document in event_input.documents
    ]
    
    # Crie o método de preprocessamento
    preprocess = FactoryPreprocessDoc.get_preprocess(
        preprocessor_method=event_input.method,
        user_topics=event_input.user_topics
    )

    # Faz um pool de documentos
    documents_pool = generate_pool(documents, n_docs=N_DOCS_TO_COMPARE)

    # Faz o preprocessamento dos documentos
    preproces_documents_pool = preprocess.parallel_processing(documents_pool)
    ditto_documents_pool = [
        DittoDocuments(preproces_pair_docs)
        for preproces_pair_docs in preproces_documents_pool  
    ]

    # Faz a comparação dos documentos
    joogle_ditto = JoogleDitto(
        ditto_documents_pool=ditto_documents_pool,
        user_topics=event_input.user_topics
    )

    comparison_between_docs = await joogle_ditto.compare()
    return comparison_between_docs


if __name__ == '__main__':


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
    if __name__ == "__main__":
        event = event# Obtém o evento de algum lugar
        comparison_results = asyncio.run(fuba(event))
        print(comparison_results)
    # # Faz o parse do evento
    # event_input = EventInput.parse_event(event)
    # # Adiciona os documentos em uma lista
    # # ic(event_input)
    # documents = [
    #     Document(**document) 
    #     for document in event_input.documents
    # ]
    # ic(documents)
    # # Crie o método de preprocessamento
    # preprocess = FactoryPreprocessDoc.get_preprocess(
    #     preprocessor_method=event_input.method,
    #     user_topics=event_input.user_topics
    # )
    # ic(preprocess)
    # # Faz um pool de documentos
    # # C = DocumentPool(
    # #     preprocess=preprocess,
    # #     documents=documents
    # # )
    # documents_pool = generate_pool(documents, n_docs=N_DOCS_TO_COMPARE)
    # ic(documents_pool)

    # # Faz o preprocessamento dos documentos
    # preproces_documents_pool = preprocess.parallel_processing(documents_pool)
    # ditto_documents_pool = [
    #     DittoDocuments(preproces_pair_docs)
    #     for preproces_pair_docs in preproces_documents_pool  
    # ]
    # ic(ditto_documents_pool[0].generate_text_to_compare())

    # # Faz a comparação dos documentos
    # joogle_ditto = JoogleDitto(
    #     ditto_documents_pool=ditto_documents_pool,
    #     user_topics=event_input.user_topics
    # )

    # comparison_between_docs = await joogle_ditto.compare()
    # ic(comparison_between_docs[0])
    # # return comparison_between_docs
