from app.core.logging import logger

from app.ingestion.loader import product_loader
from app.ingestion.chunker import product_chunker
from app.ingestion.chroma_client import chroma_service


def main():

    logger.info("Loading products...")

    products = product_loader.load_products()

    logger.info(f"{len(products)} products loaded.")

    docs = product_chunker.chunk_products(products)

    logger.info("Generating embeddings...")

    chroma_service.add_documents(docs)

    logger.info("Index created successfully.")


if __name__ == "__main__":
    main()