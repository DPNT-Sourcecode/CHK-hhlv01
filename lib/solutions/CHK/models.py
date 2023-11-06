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
    price: int
    quantity: int
