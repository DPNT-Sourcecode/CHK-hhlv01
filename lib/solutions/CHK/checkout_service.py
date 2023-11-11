from collections import Counter
from typing import Dict

from solutions.CHK import models


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

        # create SKUItem for each valid SKU, adding offer if found
        for sku in sku_counts.keys():
            if not self._validate_sku(sku):
                return -1

        return sku_counts

    def apply_offer(self, offer: models.Offer, skus: Dict[str, int]):

        if offer.condition.applies(skus):
            skus[self.condition.sku] = [sku.set_offer_applied() for sku in valid_skus]

            # apply result
            skus = self.result.apply(skus)

            # call apply again until offer cond unsatisfied
            skus = self.apply(skus)

        return skus

    def calculate_cost(self, skus: Dict[str, int]) -> int:
        """
        Return the total cost of all SKUs.
        """

        total_cost = 0
        for offer in self.offers:
            skus, cost = offer.apply(skus)
            total_cost += cost

        return total_cost



