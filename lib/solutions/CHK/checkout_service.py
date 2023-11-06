from typing import Iterable, Union

from lib.solutions.CHK.models import SKUItem


class CheckoutService:
    SKU_PRICES = {"A": 50, "B": 30, "C": 20, "D": 15}

    def create_sku_items(self, skus: str) -> Union[Iterable[SKUItem, int]]:
        """
        Return a list of SKUItems or -1 if any items are invalid
        """
        skus_list = list(skus)

        [for sku in skus_list]

        return

