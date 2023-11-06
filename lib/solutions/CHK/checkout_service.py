from collections import Counter
from typing import Iterable, Union

from lib.solutions.CHK.models import SKUItem


class CheckoutService:
    def __init__(self):
        self.prices = {"A": 50, "B": 30, "C": 20, "D": 15}

    def _validate_sku(self, sku: str) -> bool:
        """
        Return True if the sku is valid, False otherwise
        """
        return False # TODO:

    def create_sku_items(self, skus: str) -> Union[Iterable[SKUItem], int]:
        """
        Return a list of SKUItems or -1 if any items are invalid
        """
        skus_list = list(skus)
        sku_counts = Counter(skus_list)


        sku_items = []
        for sku in skus:
            if self._validate_sku(sku):
                sku_items.append(SKUItem(sku, self.prices.get(sku))
            else:
                return -1


        return



