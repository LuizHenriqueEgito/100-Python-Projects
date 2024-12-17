from src.event_input import EventInput
from src.document import Document
from src.joogle_ditto import JoogleDitto

def lambda_handler(event, context):
    event_input = EventInput.from_event(event)
    documents = [Document(doc) for doc in event_input.documents]
    doc_i, doc_j = documents
    if doc_i == doc_j:
        return {}
    joggle_ditto = JoogleDitto(doc_i, doc_j)
    model = event_input.model
    prompt = event_input.prompt
    comparison = joggle_ditto.compare(
        model=model,
        prompt=prompt
    )
    return comparison
