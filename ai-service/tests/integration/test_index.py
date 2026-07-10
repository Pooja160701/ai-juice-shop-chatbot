from app.ingestion.loader import product_loader
from app.ingestion.chunker import product_chunker
from app.ingestion.chroma_client import chroma_service
from app.ingestion.chroma_client import collection


def test_index_products():

    products = product_loader.load_products()

    docs = product_chunker.chunk_products(products)

    chroma_service.add_documents(docs)

    assert collection.count() > 0