from dataclasses import dataclass
from src.document import Document
from src.prompt_utils import (
    COMPARE_PROMPT,
    COMPARE_PROMPT_WITH_USER_TOPICS
)

@dataclass
class JoogleDitto:
    documents_to_compare: list[tuple[Document, Document]]
    prompt: str = COMPARE_PROMPT
    user_topics: list[str] | None = None

    def compare(self) -> list[dict[str, str]]:
        prompts = [
            self.format_prompt(*documents_group)  # prompt
            for documents_group in self.documents_to_compare
        ]
        # return prompts

        # response_model = self.call_model(prompts)
        # result = self.format_response_model(response_model)
        return prompts

    def call_model(self, prompts):  # faça asyncrono e coloque em uma lista
        pass

    def format_response_model(self, response_model):
        pass


    def format_prompt(self, *documents_group):
        topics = sorted({
            topic
            for doc in documents_group
            for topic in doc.preprocess_text.keys()
        })
        # constroi o prompt
        sections = []
        for topic in topics:
            section = f'TOPICO: {topic}\n'
            documents_text = '\n\nPRÓXIMO TEXTO:\n'.join(
                [
                    f'IDENTIFICADOR DOCUMENTO: {doc.id}\n'
                    f'TEXTO: {doc.preprocess_text.get(topic, "Esse documento não possui este tópico.")}'  # noqa
                    for doc in documents_group
                ]
            )
            section += documents_text
            sections.append(section)
        text = '\n\n'.join(sections)

        if self.user_topics:
            return COMPARE_PROMPT_WITH_USER_TOPICS.format(
                text_fmt=text,
                user_topics=self.user_topics
            )
    
        return COMPARE_PROMPT.format(text_fmt=text)
        # return COMPARE_PROMPT.format(text_fmt=text)
        