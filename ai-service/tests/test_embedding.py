from app.ingestion.embeddings import embedding_service

vector = embedding_service.create_embedding(
    "Apple Juice"
)

print(len(vector))