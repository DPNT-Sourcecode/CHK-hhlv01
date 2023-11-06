# noinspection PyUnusedLocal
# skus = unicode string
from lib.solutions.CHK.checkout_service import CheckoutService


def checkout(skus):
    # skus to list - list entries only chars A-Z
    sku_items = CheckoutService.create_sku_items(skus)

    # counter for skus

    # apply offers

    # sum price

    raise NotImplementedError()



