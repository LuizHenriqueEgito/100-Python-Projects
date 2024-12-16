from typing import Self
from dataclasses import dataclass


@dataclass
class EventInput:
    document_a: str
    document_b: str
    model: str
    long_text_action: LongTextAction


    @classmethod
    def from_event(cls, event) -> Self:
        return cls(
            ...
        )