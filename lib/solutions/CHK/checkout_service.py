from collections import Counter
from typing import Dict, Iterable

from lib.solutions.CHK import models


class CheckoutService:
    def __init__(self):
        self.prices = {"A": 50, "B": 30, "C": 20, "D": 15}
        self.items = self.prices.keys()

        self.offers = [
            models.Offer(models.Condition("E", 2), models.Result("B", 1, 0)),
            models.Offer(models.Condition("A", 5), models.Result("A", 5, 200)),
            models.Offer(models.Condition("A", 3), models.Result("A", 3, 130)),
            models.Offer(models.Condition("B", 2), models.Result("B", 2, 45)),
        ]

    def _validate_sku(self, sku: str) -> bool:
        """
        Return True if the sku is valid, False otherwise
        """
        return sku in self.items

    def create_skus(self, skus: str):
        """
        Return a list of SKUItems and Offers or -1 if any item is invalid
        """
        sku_counts = Counter(skus)
        sku_items = {}

        # create SKUItem for each valid SKU, adding offer if found
        for sku, quantity in sku_counts.items():
            if self._validate_sku(sku):
                sku_items[sku] = [
                    models.SKUItem(sku, self.prices.get(sku))
                    for i in range(0, quantity)
                ]
            else:
                return -1

        return sku_items

    def calculate_cost(self, skus: Dict[str, Iterable[models.SKUItem]]) -> int:
        """
        Return the total cost of all SKUs.
        """

        for offer in self.offers:
            skus = offer.apply(skus)

        total_cost = sum(sku.price for sku in skus.values())
        return total_cost

