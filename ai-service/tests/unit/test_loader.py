from app.ingestion.loader import product_loader


def test_load_products():

    products = product_loader.load_products()

    assert isinstance(products, list)
    assert len(products) > 0

    first = products[0]

    assert "id" in first
    assert "name" in first