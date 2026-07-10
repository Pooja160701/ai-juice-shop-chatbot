from unittest.mock import patch

from app.ingestion.loader import product_loader


@patch("app.ingestion.loader.requests.get")
def test_load_products(mock_get):

    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "data": [
            {
                "id": 1,
                "name": "Banana Juice"
            }
        ]
    }

    products = product_loader.load_products()

    assert len(products) == 1
    assert products[0]["name"] == "Banana Juice"