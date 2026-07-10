from app.ingestion.loader import product_loader
from app.ingestion.chunker import product_chunker
from app.ingestion.chroma_client import chroma_service

products = product_loader.load_products()

docs = product_chunker.chunk_products(products)

chroma_service.add_documents(docs)

print("Products indexed successfully!")