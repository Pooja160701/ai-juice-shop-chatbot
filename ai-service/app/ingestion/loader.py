import requests
from typing import List, Dict
from app.core.config import settings

JUICE_SHOP_API = settings.JUICE_SHOP_API


class ProductLoader:

    def load_products(self) -> List[Dict]:
        """
        Fetch products from Juice Shop REST API.
        """

        response = requests.get(JUICE_SHOP_API, timeout=30)

        response.raise_for_status()

        payload = response.json()

        return payload["data"]


product_loader = ProductLoader()