from openai import AsyncOpenAI
import asyncio
from src.prompt_utils.compare_prompt import SYS_PROMPT

class ModelCompare:
    def __init__(
        self,
        # api_key: str | None,
        model: str = 'gpt-4o-mini',
        response_format = None
    ):
        self.api_key = '...'  # adicione
        if not self.api_key:
            raise ValueError("API key must be provided or set in OPENAI_API_KEY environment variable")
            
        self.client = AsyncOpenAI(api_key=self.api_key)
        self.model = model

    async def _call_model(self, prompt: str):
        try:
            response = await self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": SYS_PROMPT},
                    {"role": "user", "content": prompt}
                ],
                response_format={"type": "json_object"}
            )
            return response.choices[0].message.content
        except Exception as e:
            raise Exception(f"Error calling OpenAI API: {str(e)}")

    async def run(self):
        """Executa várias chamadas ao modelo em paralelo."""
        tasks = [self._call_model(prompt) for prompt in self.prompts]
        return await asyncio.gather(*tasks)

    async def __call__(self, prompts):
        """Processa uma lista de prompts."""
        self.prompts = prompts
        return await self.run()