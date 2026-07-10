from app.ingestion.loader import product_loader
from app.ingestion.chunker import product_chunker

products = product_loader.load_products()

docs = product_chunker.chunk_products(products)

print(docs[0]["text"])