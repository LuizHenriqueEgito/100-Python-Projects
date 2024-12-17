from dataclasses import dataclass
from src.prompt import prompt_template
import json

@dataclass
class JoogleDitto:
    document_i: str
    document_j: str
    prompt: str = prompt_template

    def compare(
        self, 
        model: str = 'gpt-4o-mini', 
        prompt: str = prompt
    ):
        ...

    def _fmt_comparison(self) -> str:
        # use json
        ...
