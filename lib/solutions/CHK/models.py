import dataclasses


@dataclasses.dataclass
class Offer:
    quantity: int
    price: int


@dataclasses.dataclass
class SKUItem:
    sku: str
    price: int
    quantity: int
    offer: Offer

    def get_total_cost(self):
        return self.price * self.quantity

