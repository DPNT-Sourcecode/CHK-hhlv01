from collections import Counter
from typing import Iterable

from solutions.CHK import models


class CheckoutService:
    def __init__(self):
        self.prices = {"A": 50, "B": 30, "C": 20, "D": 15}
        self.items = self.prices.keys()

        self.offers = {
            "E": [
                models.Offer(
                    models.OfferCondition("E", 2), models.OfferResult("B", 1, 0)
                )
            ],
            "A": [
                models.Offer(
                    models.OfferCondition("A", 5), models.OfferResult("A", 5, 200)
                ),
                models.Offer(
                    models.OfferCondition("A", 3), models.OfferResult("A", 3, 130)
                ),
            ],
            "B": [
                models.Offer(
                    models.OfferCondition("B", 2), models.OfferResult("B", 2, 45)
                )
            ],
        }

    def _validate_sku(self, sku: str) -> bool:
        """
        Return True if the sku is valid, False otherwise
        """
        return sku in self.items

    def _get_sku_offers(self, sku: str):
        return self.offers.get(sku, [])

    def create_skus(self, skus: str):
        """
        Return a list of SKUItems and Offers or -1 if any item is invalid
        """
        sku_counts = Counter(skus)

        sku_items = []
        sku_offers = []
        # create SKUItem for each valid SKU, adding offer if found
        for sku, quantity in sku_counts.items():
            if self._validate_sku(sku):
                sku_item = models.SKUItem(sku, quantity, self.prices.get(sku))
                sku_items.append(sku_item)
            else:
                return -1

        return sku_items

    def calculate_cost(self, skus: Iterable[models.SKUItem]) -> int:
        """
        Return the total cost of all SKUs.
        """
        total_cost = 0

        for sku in skus:
            if offers := self.offers.get(sku.sku):
                for offer in offers:
                    if sku.on_offer(offer):
                        total_cost += 1

        return total_cost
