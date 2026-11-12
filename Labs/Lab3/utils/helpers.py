"""Calculations for the inventory demonstration."""

from collections.abc import Sequence

from models import InventoryItem


def calculate_total_stock_value(items: Sequence[InventoryItem]) -> float:
    """Return the sum of quantity multiplied by unit price."""
    return sum(item.quantity * item.price for item in items)


def highest_stock_item(items: Sequence[InventoryItem]) -> InventoryItem | None:
    """Return the item with the largest quantity, or None for empty stock."""
    if not items:
        return None
    return max(items, key=lambda item: item.quantity)


def lowest_stock_item(items: Sequence[InventoryItem]) -> InventoryItem | None:
    """Return the item with the smallest quantity, or None for empty stock."""
    if not items:
        return None
    return min(items, key=lambda item: item.quantity)
