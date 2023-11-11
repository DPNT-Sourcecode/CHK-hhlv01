import dataclasses
from typing import Optional


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

    def apply(self, skus: Iterable[SKUItem]):
        return skus


@dataclasses.dataclass
class SKUItem:
    sku: str
    price: int
    offer_applied: Optional[bool] = False


