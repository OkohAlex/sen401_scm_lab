"""Load the legacy JSON inventory records into SQLite."""

import json
import os
from pathlib import Path

from app.database import get_connection, initialize_database
from app.models import InventoryItemInput


def seed_inventory() -> int:
    """Import validated records from JSON without duplicating existing items."""
    default_path = Path(__file__).resolve().parents[1] / "data" / "legacy_inventory.json"
    source_path = Path(os.environ.get("SEED_DATA_PATH", str(default_path)))
    with source_path.open(encoding="utf-8") as source:
        records = json.load(source)
    if not isinstance(records, list):
        raise ValueError("Legacy inventory JSON must contain a list")

    imported_count = 0
    with get_connection() as connection:
        for record in records:
            item = InventoryItemInput.model_validate(record)
            cursor = connection.execute(
                "INSERT OR IGNORE INTO inventory (item_name, quantity, price) "
                "VALUES (?, ?, ?)",
                (item.item_name, item.quantity, item.price),
            )
            imported_count += cursor.rowcount
    return imported_count


def main() -> None:
    """Initialize SQLite and report how many legacy records were imported."""
    initialize_database()
    imported_count = seed_inventory()
    print(f"Imported {imported_count} inventory records into SQLite.")


if __name__ == "__main__":
    main()
