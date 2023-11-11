import dataclasses


@dataclasses.dataclass
class Condition:
    sku: str
    quantity: int


@dataclasses.dataclass
class Result:
    sku: str
    quantity: int
    price: int


@dataclasses.dataclass
class Offer:
    condition: Condition
    result: Result


@dataclasses.dataclass
class SKUItem:
    sku: str
    price: int
    offer_applied: Optional[bool] = False

