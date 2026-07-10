from app.ingestion.chroma_client import collection
from app.ingestion.embeddings import embedding_service
from app.monitoring.metrics import RAG_SEARCHES

class ProductRetriever:

    def retrieve(
        self,
        question: str,
        k: int = 5,
        max_distance: float = 1.2,
    ):

        query_embedding = embedding_service.create_embedding(question)

        print("Retriever called")
        RAG_SEARCHES.inc()

        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=k,
        )

        filtered_docs = []

        for doc, metadata, distance in zip(
            results["documents"][0],
            results["metadatas"][0],
            results["distances"][0],
        ):

            if distance <= max_distance:

                filtered_docs.append(
                    {
                        "document": doc,
                        "metadata": metadata,
                        "distance": distance,
                    }
                )

        return filtered_docs


product_retriever = ProductRetriever()