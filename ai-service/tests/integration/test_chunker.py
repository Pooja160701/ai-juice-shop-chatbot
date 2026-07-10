from app.ingestion.loader import product_loader
from app.ingestion.chunker import product_chunker


def test_chunk_products():

    products = product_loader.load_products()

    docs = product_chunker.chunk_products(products)

    assert isinstance(docs, list)
    assert len(docs) > 0

    first = docs[0]

    assert "id" in first
    assert "text" in first
    assert "metadata" in first