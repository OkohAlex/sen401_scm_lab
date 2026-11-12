"""Validated data models for the inventory project."""

from dataclasses import dataclass
from math import isfinite


@dataclass(frozen=True)
class InventoryItem:
    """A named inventory item with a non-negative quantity and unit price."""

    item_name: str
    quantity: int
    price: float

    def __post_init__(self) -> None:
        """Reject invalid stock records before they reach calculations."""
        name = self.item_name.strip() if isinstance(self.item_name, str) else ""
        if not name:
            raise ValueError("item_name must not be empty")
        if isinstance(self.quantity, bool) or not isinstance(self.quantity, int):
            raise ValueError("quantity must be an integer")
        if self.quantity < 0:
            raise ValueError("quantity must be non-negative")
        if isinstance(self.price, bool) or not isinstance(self.price, (int, float)):
            raise ValueError("price must be a number")
        if not isfinite(self.price) or self.price < 0:
            raise ValueError("price must be finite and non-negative")
        object.__setattr__(self, "item_name", name)
        object.__setattr__(self, "price", float(self.price))
