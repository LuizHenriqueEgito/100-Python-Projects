from tiktoken import encoding_for_model
from enum import StrEnum
from enum import IntEnum


class ModelMaxTokens(IntEnum):
    GPT_3_5 = 10
    GPT_4o = 20
    GPT_3_5_TURBO = 30


class LongTextAction(StrEnum):
    TRUNCATE = 'truncate'
    SUMMARY = 'summary'


class Document:
    def __init__(
            self,
            document: str,
            model: str,
            long_text_action: LongTextAction | None
    ):
        self.document = self.document
        self.long_text_action = long_text_action
        self.model = model

    def __len__(self) -> int:
        encoding = encoding_for_model(self.model)
        tokenized = encoding.encode(self.document)
        return len(tokenized)
    
    def _preprocess_document(self)
