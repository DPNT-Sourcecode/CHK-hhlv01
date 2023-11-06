import dataclasses


@dataclasses.dataclass
class OfferCondition:
    sku: str
    quantity: int


@dataclasses.dataclass
class OfferResult:
    sku: str
    quantity: int
    price: int


@dataclasses.dataclass
class Offer:
    condition: OfferCondition
    result: OfferResult


@dataclasses.dataclass
class SKUItem:
    sku: str
    quantity: int
    price: int

    def on_offer(self, offer_cond: OfferCondition):
        return offer_cond.sku == self.sku and offer_cond.quantity <= self.quantity


