from collections import Counter
from typing import Iterable, Union

from solutions.CHK.models import SKUItem, Offer


class CheckoutService:
    def __init__(self):
        self.prices = {"A": 50, "B": 30, "C": 20, "D": 15}
        self.items = self.prices.keys()

        self.offers = {"A": Offer(3, 130), "B": Offer(2, 45)}

    def _validate_sku(self, sku: str) -> bool:
        """
        Return True if the sku is valid, False otherwise
        """
        return sku in self.items

    def _get_sku_offer(self, sku: str):
        return self.offers.get(sku, None)

    def create_skus(self, skus: str) -> Union[Iterable[SKUItem], int]:
        """
        Return a list of SKUItems or -1 if no items, or any item is invalid
        """
        sku_counts = Counter(skus)

        sku_items = []
        # create SKUItem for each valid SKU, adding offer if found
        for sku, quantity in sku_counts.items():
            if self._validate_sku(sku):
                if offer := self._get_sku_offer(sku):
                    sku_item = SKUItem(sku, self.prices.get(sku), quantity, offer)
                else:
                    sku_item = SKUItem(sku, self.prices.get(sku), quantity)

                sku_items.append(sku_item)
            else:
                return -1

        return sku_items

    def calculate_cost(self, skus: Iterable[SKUItem]) -> int:
        """
        Return the total cost of all SKUs.
        """
        total_cost = 0

        for sku in skus:
            total_cost += sku.get_total_cost()

        return total_cost


