from tiktoken import encoding_for_model
# from enum import IntEnum


# class ModelMaxTokens(IntEnum):
#     GPT_3_5 = 10
#     GPT_4o = 20
#     GPT_3_5_TURBO = 30
MODEL_CONFIGS = {
    'gpt-3.5-turbo': 16_385,     
    'gpt-3.5-turbo-16k': 16_385, 
    'gpt-4': 8_192,              
    'gpt-4-32k': 32_768,         
    'gpt-4-turbo': 128_000,      
    'gpt-4o': 128_000,           
    'gpt-4o-mini': 128_000
}


class Document:
    def __init__(
            self,
            document: str,
            model: str
    ):
        self.document = self._preprocess(document)
        self.encodding = encoding_for_model(model)

    def __len__(self) -> int:
        tokenized = self.encoding.encode(self.document)
        return len(tokenized)
    
    def _preprocess(self):
        if len_doc := len(self) > MODEL_CONFIGS[self.model]:
            # trunca o texto
            return self.encodding.decoding(self.document[:len_doc])
        return self.document
