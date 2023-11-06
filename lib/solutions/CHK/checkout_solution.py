# noinspection PyUnusedLocal
# skus = unicode string
from solutions.CHK.checkout_service import CheckoutService


def checkout(skus):
    # skus to list - list entries only chars A-Z
    checkout_service = CheckoutService()

    sku_items = checkout_service.create_skus(skus)

    if sku_items != -1:
        cost = checkout_service.calculate_cost(sku_items)
        return cost

    return -1  # if the input is None



