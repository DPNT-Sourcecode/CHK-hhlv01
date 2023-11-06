import dataclasses
from typing import Optional


@dataclasses.dataclass
class Offer:
    quantity: int
    price: int


@dataclasses.dataclass
class SKUItem:
    sku: str
    price: int
    quantity: int
    offer: Optional[Offer] = None

    def get_total_cost(self):
        """
        Return the total cost of the SKUItem, including any valid offers
        """
        cost = 0
        quantity = self.quantity

        if self.offer and self.offer.quantity >= quantity:
            cost = self.offer.price
            quantity -= self.offer.quantity

        cost += quantity * self.price

        return cost



