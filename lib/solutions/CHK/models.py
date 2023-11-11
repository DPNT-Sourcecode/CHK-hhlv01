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

    def applies(self, skus: Iterable[SKUItem]):
        """
        Return True if the Condition applies to the SKUItem's provided
        """
        return len(skus) >= self.quantity and all(not sku.offer_applied for sku in skus)


@dataclasses.dataclass
class Result:
    sku: str
    # quantity: int
    price: int

    def apply(self, skus: Dict[str, Iterable[SKUItem]]):
        res_skus = skus.get(self.sku, [])

        for sku in res_skus:
            sku.set_offer_applied()
            sku.price -= self.price

        skus[self.sku] = res_skus

        return skus


@dataclasses.dataclass
class Offer:
    condition: Condition
    result: Result

    def apply(self, skus: Dict[str, Iterable[SKUItem]]):
        # if condition is valid and item not offer_applied

        valid_skus = skus.get(self.condition.sku, [])
        if self.condition.applies(valid_skus):
            skus[self.condition.sku] = [sku.set_offer_applied() for sku in valid_skus]

            # apply result
            skus = self.result.apply(skus)

            # call apply again until offer cond unsatisfied
            skus = self.apply(skus)

        return skus

