from app.ingestion.embeddings import embedding_service


def test_embedding():

    vector = embedding_service.create_embedding(
        "Apple Juice"
    )

    assert isinstance(vector, list)
    assert len(vector) > 0