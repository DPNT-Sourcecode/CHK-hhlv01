import dataclasses
from typing import Optional, Dict, Iterable


@dataclasses.dataclass
class SKUItem:
    sku: str
    price: int
    offer_applied: Optional[bool] = False


class AbstractCond:
    def applies(self, skus: Dict[str, int]):
        pass


@dataclasses.dataclass
class Condition(AbstractCond):
    sku: str
    quantity: int

    def applies(self, skus: Dict[str, int]):
        """
        Return True if the Condition applies to the SKUItem's provided
        """
        return self.quantity <= skus.get(self.sku, 0)


@dataclasses.dataclass
class MultiCondition(AbstractCond):
    sku: Iterable[str]
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


