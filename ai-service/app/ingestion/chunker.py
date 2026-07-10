from typing import List, Dict


class ProductChunker:

    def chunk_products(self, products: List[Dict]):

        documents = []

        for product in products:

            document = f"""
Product Name:
{product['name']}

Description:
{product['description']}

Price:
{product['price']}

Deluxe Price:
{product['deluxePrice']}
"""

            documents.append(
                {
                    "id": str(product["id"]),
                    "text": document,
                    "metadata": {
                        "id": product["id"],
                        "name": product["name"],
                        "price": product["price"],
                        "deluxe_price": product["deluxePrice"],
                        "image": product["image"],
                    }
                }
            )

        return documents


product_chunker = ProductChunker()