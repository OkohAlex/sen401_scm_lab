"""Display inventory quantities, stock valuation, and stock-level extremes."""

from inventory import INVENTORY_ITEMS
from utils.helpers import (
    calculate_total_stock_value,
    highest_stock_item,
    lowest_stock_item,
)


def main() -> None:
    """Print inventory records and the total value of available stock."""
    if not INVENTORY_ITEMS:
        print("No inventory records are available.")
        return

    print("SEN 401 Inventory Status Accounting")
    print("===================================")
    for item in INVENTORY_ITEMS:
        print(
            f"{item.item_name}: {item.quantity} units "
            f"at ${item.price:.2f} each "
            f"(${item.quantity * item.price:.2f} total)"
        )
    highest = highest_stock_item(INVENTORY_ITEMS)
    lowest = lowest_stock_item(INVENTORY_ITEMS)
    print("-----------------------------------")
    print(f"Total stock value: ${calculate_total_stock_value(INVENTORY_ITEMS):.2f}")
    if highest is not None and lowest is not None:
        print(f"Largest quantity: {highest.item_name} ({highest.quantity} units)")
        print(f"Smallest quantity: {lowest.item_name} ({lowest.quantity} units)")


if __name__ == "__main__":
    main()
