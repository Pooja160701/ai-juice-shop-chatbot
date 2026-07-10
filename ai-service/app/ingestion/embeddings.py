from openai import OpenAI

from app.core.config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)


class EmbeddingService:

    def create_embedding(self, text: str):

        response = client.embeddings.create(
            model="text-embedding-3-small",
            input=text
        )

        return response.data[0].embedding


embedding_service = EmbeddingService()