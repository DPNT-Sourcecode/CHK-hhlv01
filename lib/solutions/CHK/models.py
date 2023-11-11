import dataclasses
from typing import Optional, Dict


@dataclasses.dataclass
class SKUItem:
    sku: str
    price: int
    offer_applied: Optional[bool] = False


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

    def applies(self, skus: Dict[str, int]):
        """
        Return True if the Condition applies to the SKUItem's provided
        """
        return self.quantity <= skus.get(self.sku, 0)


@dataclasses.dataclass
class Offer:
    condition: Condition
    result: Result

