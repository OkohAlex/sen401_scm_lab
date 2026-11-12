"""SQLite connection and schema management."""

import os
import sqlite3
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path


def database_path() -> Path:
    """Return the configured SQLite file path."""
    default_path = Path(__file__).resolve().parents[1] / "data" / "inventory.db"
    return Path(os.environ.get("DATABASE_PATH", str(default_path)))


@contextmanager
def get_connection() -> Iterator[sqlite3.Connection]:
    """Open a row-addressable SQLite connection, creating its parent folder."""
    path = database_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(path, timeout=10)
    connection.row_factory = sqlite3.Row
    try:
        with connection:
            yield connection
    finally:
        connection.close()


def initialize_database() -> None:
    """Create the inventory table if it does not already exist."""
    with get_connection() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS inventory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                item_name TEXT NOT NULL UNIQUE,
                quantity INTEGER NOT NULL CHECK (quantity >= 0),
                price REAL NOT NULL CHECK (price >= 0)
            )
            """
        )
