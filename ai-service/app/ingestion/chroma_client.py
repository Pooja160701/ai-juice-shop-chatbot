import chromadb

from app.ingestion.embeddings import embedding_service
from app.core.config import settings

client = chromadb.PersistentClient(
    path=settings.CHROMA_PATH
)

collection = client.get_or_create_collection(
    name="juice_shop_products"
)

class ChromaService:

    def add_documents(self, docs):

        for doc in docs:

            embedding = embedding_service.create_embedding(
                doc["text"]
            )

            collection.add(
                ids=[doc["id"]],
                documents=[doc["text"]],
                metadatas=[doc["metadata"]],
                embeddings=[embedding]
            )


chroma_service = ChromaService()