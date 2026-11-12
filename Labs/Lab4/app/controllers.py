"""Database operations for inventory API requests."""

import sqlite3

from app.database import get_connection
from app.models import InventoryItem, InventoryItemInput


class DuplicateItemError(Exception):
    """Raised when an inventory item name already exists."""


def _to_inventory_item(row: sqlite3.Row) -> InventoryItem:
    """Convert a database row into the public response model."""
    return InventoryItem(
        id=row["id"],
        item_name=row["item_name"],
        quantity=row["quantity"],
        price=row["price"],
    )


def list_inventory() -> list[InventoryItem]:
    """Return all inventory records in stable insertion order."""
    with get_connection() as connection:
        rows = connection.execute(
            "SELECT id, item_name, quantity, price FROM inventory ORDER BY id"
        ).fetchall()
    return [_to_inventory_item(row) for row in rows]


def get_inventory_item(item_id: int) -> InventoryItem | None:
    """Return one inventory record, or None if its identifier is absent."""
    with get_connection() as connection:
        row = connection.execute(
            "SELECT id, item_name, quantity, price FROM inventory WHERE id = ?",
            (item_id,),
        ).fetchone()
    return _to_inventory_item(row) if row is not None else None


def create_inventory_item(item: InventoryItemInput) -> InventoryItem:
    """Insert an inventory record and return its database-assigned identifier."""
    try:
        with get_connection() as connection:
            cursor = connection.execute(
                "INSERT INTO inventory (item_name, quantity, price) "
                "VALUES (?, ?, ?)",
                (item.item_name, item.quantity, item.price),
            )
            row = connection.execute(
                "SELECT id, item_name, quantity, price FROM inventory WHERE id = ?",
                (cursor.lastrowid,),
            ).fetchone()
    except sqlite3.IntegrityError as error:
        if "inventory.item_name" in str(error):
            raise DuplicateItemError(item.item_name) from error
        raise

    if row is None:
        raise RuntimeError("Inserted inventory record could not be read back")
    return _to_inventory_item(row)
