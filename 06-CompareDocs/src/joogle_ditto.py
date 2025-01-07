from dataclasses import dataclass
# from src.utils_typing import PoolDocuments, PairPreprocessedDocs
from src.openai_utils import ModelCompare
import asyncio

from src.preprocess_document.base_preprocess import BasePreprocess
from src.prompt_utils import (
    COMPARE_PROMPT,
    COMPARE_PROMPT_WITH_USER_TOPICS
)


# Use o async do LLM se tiver mais de 2 comparações use o async ou use o sempre
class DittoPairDocuments:
    def __init__(self, preprocess_pair_docs: list[dict]):
        self.preprocess_pair_docs = preprocess_pair_docs
        self.topics = self._extract_topics()
        self._iterator_index = 0

    def _extract_topics(self) -> list[str]:
        topics = set()
        for doc in self.preprocess_pair_docs:
            topics.update(doc.get('text_grouped_by_topics', {}).keys())
        return sorted(topics)

    def __iter__(self):
        self._iterator_index = 0
        return self

    def __next__(self) -> str:
        if self._iterator_index >= len(self.topics):
            raise StopIteration

        topic = self.topics[self._iterator_index]
        self._iterator_index += 1

        return self._format_topic_comparison(topic)

    def _format_topic_comparison(self, topic: str) -> str:
        lines = [f"{topic}\n"]
        for doc in self.preprocess_pair_docs:
            doc_id = doc['id']
            text = doc.get("text_grouped_by_topics", {}).get(topic, "Tópico NÃO PRESENTE nesse texto...")
            lines.append(f"DOCUMENT ({doc_id})\n{text}\n")
        return "\n".join(lines)

    def generate_text_to_compare(self) -> str:
        return "\n".join(
            self._format_topic_comparison(topic) 
            for topic in self.topics
        )


class JoogleDitto:
    def __init__(
        self,
        ditto_documents_pool,
        user_topics
    ):
        self.ditto_documents_pool = ditto_documents_pool
        self.user_topics = user_topics
        self.model = ModelCompare()

    def fmt_prompt(self, ditto_documents: 'DittoDocuments') -> str:
        template_args = {
            "text_fmt": ditto_documents.generate_text_to_compare()
        }
        
        if self.user_topics:
            template_args["user_topics"] = self.user_topics
            return COMPARE_PROMPT_WITH_USER_TOPICS.format(**template_args)
        
        return COMPARE_PROMPT.format(**template_args)

    async def compare(self):
        prompts = [
            self.fmt_prompt(ditto_documents)
            for ditto_documents in self.ditto_documents_pool
        ]
        return await self.model(prompts)
