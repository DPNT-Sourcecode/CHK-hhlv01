# noinspection PyUnusedLocal
# skus = unicode string
from solutions.CHK.checkout_service import CheckoutService


def checkout(skus):
    if skus:
        # skus to list - list entries only chars A-Z
        checkout_service = CheckoutService()

        sku_items = checkout_service.create_sku_items(skus)

        if sku_items != -1:
            cost = checkout_service.calculate_cost()
            return cost

    return -1  # if the input is None



