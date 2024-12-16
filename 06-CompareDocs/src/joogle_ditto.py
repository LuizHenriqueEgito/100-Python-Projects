from dataclasses import dataclass


@dataclass
class JoogleDitto:
    document_a: str
    document_b: str

    def compare(self):
        ...
