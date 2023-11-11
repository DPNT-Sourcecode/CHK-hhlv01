from collections import Counter
from typing import Dict

from lib.solutions.CHK import models


class CheckoutService:
    def __init__(self):
        self.prices = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 2}
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

    def apply_offer(self, offer: models.Offer, skus: Dict[str, int], cost: int = 0):
        if offer.condition.applies(skus) and offer.result.applies(skus):
            if offer.condition.sku == offer.result.sku:
                skus[offer.condition.sku] -= offer.condition.quantity

            # if the result price is 0, subtract from quantity
            if offer.result.price == 0:
                skus[offer.result.sku] -= offer.result.quantity

            cost += offer.result.price

            # prevent further offers using items with none available for offer
            if skus[offer.result.sku] <= 0:
                del skus[offer.result.sku]

            # call apply again until offer cond unsatisfied
            cost, skus = self.apply_offer(offer, skus, cost)

        return cost, skus

    def calculate_cost(self, skus: Dict[str, int]) -> int:
        """
        Return the total cost of all SKUs.
        """

        total_cost = 0
        for offer in self.offers:
            cost, skus = self.apply_offer(offer, skus)
            total_cost += cost

            if not skus:  # if there are no items to apply offers to
                break

        # add any remaining full price items
        for sku, quantity in skus.items():
            total_cost += self.prices.get(sku) * quantity

        return total_cost




