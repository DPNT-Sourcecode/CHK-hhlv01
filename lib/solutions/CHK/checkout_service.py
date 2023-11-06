from typing import Iterable, Union

from lib.solutions.CHK.models import SKUItem


class CheckoutService:
    SKU_PRICES = {"A": 50, "B": 30, "C": 20, "D": 15}

    @staticmethod
    def _validate_sku(sku: str) -> bool:
        """
        Return True if the sku is valid, False otherwise
        """
        return False # TODO:

    @staticmethod
    def create_sku_items(skus: str) -> Union[Iterable[SKUItem, int]]:
        """
        Return a list of SKUItems or -1 if any items are invalid
        """
        skus_list = list(skus)

        [SKUItem(sku, SKU_PRICES.get()) for sku in skus_list if ]

        return


