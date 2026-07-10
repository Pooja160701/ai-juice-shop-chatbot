from openai import OpenAI

from app.core.config import settings
from app.monitoring.metrics import EMBEDDING_REQUESTS

client = OpenAI(api_key=settings.OPENAI_API_KEY)


class EmbeddingService:

    def create_embedding(self, text: str):
        
        print("Embedding API called")
        EMBEDDING_REQUESTS.inc()
        response = client.embeddings.create(
            model="text-embedding-3-small",
            input=text
        )

        return response.data[0].embedding


embedding_service = EmbeddingService()