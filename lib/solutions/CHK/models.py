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

    def applies(self, skus: Dict[str, Iterable[SKUItem]]):
        valid_skus = skus.get(self.sku, [])
        return len(valid_skus) >= self.quantity and all(
            not sku.offer_applied for sku in valid_skus
        )


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


        if len(valid_skus) >= self.condition.quantity and all(
            not sku.offer_applied for sku in valid_skus
        ):
            skus[self.condition.sku] = [sku.set_offer_applied() for sku in valid_skus]

            # apply result
            res_skus = skus.get(self.result.sku, [])

            result.

            skus[self.result.sku] = res_skus

            # call apply again until offer cond unsatisified
            skus = self.apply(skus)

        return skus









