import dataclasses
from typing import Optional, Dict


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

    def applies(self, skus: Dict[str, int]):
        """
        Return True if the Condition applies to the SKUItem's provided
        """
        return self.quantity <= skus.get(self.sku, 0)


@dataclasses.dataclass
class Result:
    sku: str
    quantity: int
    price: int

    def apply(self, skus: Dict[str, int]):
        """
        Return the SKUs and cost
        """
        res_skus = skus.get(self.sku, [])

        count = 0
        for sku in res_skus:
            if count == self.quantity:
                break

            if count == 0:
                sku.price = self.price
            else:
                sku.price = 0

            sku.set_offer_applied()
            count += 1

        skus[self.sku] = res_skus

        return skus


@dataclasses.dataclass
class Offer:
    condition: Condition
    result: Result




