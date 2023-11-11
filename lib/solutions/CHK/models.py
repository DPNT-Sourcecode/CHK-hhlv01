import dataclasses
from typing import Optional, Iterable, Dict


@dataclasses.dataclass
class SKUItem:
    sku: str
    price: int
    offer_applied: Optional[bool] = False

    def set_offer_applied(self):
        self.offer_applied = True
        return self

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

    def apply(self, skus: Dict[str, Iterable[SKUItem]]):
        # if condition is valid and item not offer_applied

        valid_skus = skus.get(self.condition.sku, [])
        if len(valid_skus) >= self.condition.quantity and all(not sku.offer_applied for sku in valid_skus):


            skus[self.condition.sku] = [sku.set_offer_applied() for sku in valid_skus]

            # apply result
            self.result.
            skus[self.result.sku] = update_sku


            # call apply again until offer cond unsatisified
            skus = self.apply(skus)

        return skus








