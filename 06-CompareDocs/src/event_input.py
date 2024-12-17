from typing import Self
from dataclasses import dataclass
from src.prompt import prompt_template


@dataclass
class EventInput:
    documents: list[str]
    model: str
    prompt: str

    @classmethod
    def from_event(cls, event) -> Self:
        return cls(
            ...  # caso exista prompt use se não existir use o prompt_template
        )