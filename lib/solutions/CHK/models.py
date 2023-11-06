import dataclasses


@dataclasses.dataclass
class SKUItem:
    sku: str
    price: int
    quantity: int


