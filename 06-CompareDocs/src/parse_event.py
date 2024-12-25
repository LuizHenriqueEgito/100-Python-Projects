from typing import Self
from dataclasses import dataclass

@dataclass
class EventInput:
    method: str
    model: str
    documents: list[dict[str, str]]
    user_topics: str

    @classmethod
    def parse_event(cls, event) -> Self:
        body = event['body']
        return cls(
            method=body.get('method', 'default'),
            model=body.get('model', 'model'),
            documents=body.get('documents'),
            user_topics=body.get('user_topics')
        )