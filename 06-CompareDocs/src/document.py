from tiktoken import encoding_for_model
from typing import Any


N_TOKENS_TO_SMALL_DOC = 50
class Document:
    def __init__(self, id: str, text: str):
        self.id = id
        self.text = text
        self.small_doc = self._is_small_doc()
        self.preprocess_text: Any | None = None  # TODO: remova o Any

    def __len__(self) -> int:
        encodding = encoding_for_model('gpt-4o-mini')
        tokenized = encodding.encode(self.text)
        return len(tokenized)

    def __str__(self):
        return f"{type(self).__name__}(id={self.id}, small_doc={self.small_doc})"
    
    def __repr__(self):
        return self.__str__()
    
    def _is_small_doc(self):
        return len(self) < N_TOKENS_TO_SMALL_DOC