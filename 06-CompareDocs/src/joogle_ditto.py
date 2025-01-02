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
class DittoDocuments:
    def __init__(self, preproces_pair_docs):
        self.preproces_pair_docs = preproces_pair_docs
        self.topics = set()
        self.index = 0

        for processed_doc in preproces_pair_docs:
            self.topics.update(processed_doc['text_grouped_by_topics'].keys())
        self.topics = list(self.topics)


    def __iter__(self):
        self.index = 0
        return self
    
    def __next__(self):
        if self.index >= len(self.topics):
            raise StopIteration
        
        current_topic = self.topics[self.index]
        self.index += 1

        results = [f'{current_topic}\n']
        for doc in self.preproces_pair_docs:
            doc_id = doc['id']
            text = doc['text_grouped_by_topics'].get(current_topic, 'vazio')
            results.append(f"ID DOCUMENTO - ({doc_id})\n{text}\n")
        return "\n".join(results)
    

    def generate_text_to_compare(self) -> str:
        sections = []
        for topic in self.topics:
            section = f"{topic}:\n"
            for document in self.preproces_pair_docs:
                doc_id = document["id"]
                text = document["text_grouped_by_topics"].get(topic, "vazio")
                section += f"ID DOCUMENTO - ({doc_id})\n{text}\n"
            sections.append(section)
        return "\n\n".join(sections)



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
