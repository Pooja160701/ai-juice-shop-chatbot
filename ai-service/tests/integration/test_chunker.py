from app.ingestion.chunker import product_chunker


def test_chunk_products():

    products = [
        {
            "id": 1,
            "name": "Banana Juice",
            "description": "Fresh banana juice",
            "price": 2.99,
            "deluxePrice": 3.99,
        }
    ]

    docs = product_chunker.chunk_products(products)

    assert len(docs) == 1
    assert docs[0]["id"] == "1"
    assert "Banana Juice" in docs[0]["text"]