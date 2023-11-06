# noinspection PyUnusedLocal
# skus = unicode string
from lib.solutions.CHK.checkout_service import CheckoutService


def checkout(skus):
    if skus:
        # skus to list - list entries only chars A-Z
        checkout_service = CheckoutService()

        sku_items = checkout_service.create_sku_items(skus)

        if sku_items:

            # apply offers

            # sum price

    return -1  # if the input is None
