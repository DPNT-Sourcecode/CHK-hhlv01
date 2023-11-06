from collections import Counter
from typing import Iterable, Union

from lib.solutions.CHK.models import SKUItem


class CheckoutService:
    def __init__(self):
        self.prices = {"A": 50, "B": 30, "C": 20, "D": 15}
        self.items = self.prices.keys()

    def _validate_sku(self, sku: str) -> bool:
        """
        Return True if the sku is valid, False otherwise
        """
        return sku in self.items

    def create_sku_items(self, skus: str) -> Union[Iterable[SKUItem], int]:
        """
        Return a list of SKUItems or -1 if no items, or any item is invalid
        """
        sku_counts = Counter(skus)

        sku_items = []
        for sku, quantity in sku_counts.items():
            if self._validate_sku(sku):
                sku_items.append(SKUItem(sku, self.prices.get(sku), quantity))
            else:
                return -1

        return sku_items

    def _apply_offer(self):
        pass

    def calculate_cost(self):
        pass
