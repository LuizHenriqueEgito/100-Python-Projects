from dataclasses import dataclass
from src.document import Document


@dataclass
class JoogleDitto:
    documents_to_compare: list[tuple[Document, Document]]

    def compare(self) -> list[dict[str, str]]:  # {'documentosComparados': 'docX comparado com docY', 'comparacao': {'resumo': '', 'topicosSemelhantes': '', 'topicosdiferentes': ''}}
        pass

    