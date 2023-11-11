import dataclasses
from typing import Optional, Iterable


@dataclasses.dataclass
class SKUItem:
    sku: str
    price: int
    offer_applied: Optional[bool] = False


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

    def apply(self, skus: Dict[int, SKUItem]):
        # if condition is valid and item not offer_applied
        if self.condition.sku ==



        # apply result

        # call apply again until offer cond unsatisified

        return skus




