from app.ingestion.loader import product_loader

products = product_loader.load_products()

print(f"Loaded {len(products)} products\n")

for product in products[:5]:
    print(product["name"])