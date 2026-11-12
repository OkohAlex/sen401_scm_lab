"""Tests for inventory validation and calculations."""

import unittest

from models import InventoryItem
from utils.helpers import (
    calculate_total_stock_value,
    highest_stock_item,
    lowest_stock_item,
)


class InventoryTests(unittest.TestCase):
    def test_empty_inventory_has_zero_value_and_no_extremes(self) -> None:
        self.assertEqual(calculate_total_stock_value([]), 0)
        self.assertIsNone(highest_stock_item([]))
        self.assertIsNone(lowest_stock_item([]))

    def test_calculates_value_and_quantity_extremes(self) -> None:
        items = [
            InventoryItem("Keyboard", 3, 10.0),
            InventoryItem("Monitor", 1, 150.0),
            InventoryItem("Mouse", 8, 5.0),
        ]

        self.assertEqual(calculate_total_stock_value(items), 220.0)
        self.assertEqual(highest_stock_item(items), items[2])
        self.assertEqual(lowest_stock_item(items), items[1])

    def test_rejects_negative_inventory_values(self) -> None:
        with self.assertRaisesRegex(ValueError, "quantity must be non-negative"):
            InventoryItem("Keyboard", -1, 10.0)
        with self.assertRaisesRegex(ValueError, "price must be finite and non-negative"):
            InventoryItem("Keyboard", 1, -0.01)


if __name__ == "__main__":
    unittest.main()
