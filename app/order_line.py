import dataclasses


@dataclasses.dataclass(eq=False)
class OrderLine():
    id: str
    product_name: str
    quantity: int