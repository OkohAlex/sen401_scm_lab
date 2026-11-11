"""FastAPI routes for the migrated inventory application."""

from contextlib import asynccontextmanager
from collections.abc import AsyncIterator

from fastapi import FastAPI, HTTPException, status

from app.controllers import (
    DuplicateItemError,
    create_inventory_item,
    get_inventory_item,
    list_inventory,
)
from app.database import initialize_database
from app.models import InventoryItem, InventoryItemInput
from app.seed import seed_inventory


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    """Ensure the database and migrated sample records exist at startup."""
    initialize_database()
    seed_inventory()
    yield


app = FastAPI(
    title="SEN 401 Inventory API",
    version="1.0.0",
    description="Inventory API backed by migrated SQLite data.",
    lifespan=lifespan,
)


@app.get("/health")
def health_check() -> dict[str, str]:
    """Return the service health status."""
    return {"status": "ok"}


@app.get("/api/v1/inventory", response_model=list[InventoryItem])
def read_inventory() -> list[InventoryItem]:
    """List inventory records."""
    return list_inventory()


@app.get("/api/v1/inventory/{item_id}", response_model=InventoryItem)
def read_inventory_item(item_id: int) -> InventoryItem:
    """Read one inventory record by its identifier."""
    item = get_inventory_item(item_id)
    if item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Inventory item not found",
        )
    return item


@app.post(
    "/api/v1/inventory",
    response_model=InventoryItem,
    status_code=status.HTTP_201_CREATED,
)
def add_inventory_item(item: InventoryItemInput) -> InventoryItem:
    """Create an inventory record in SQLite."""
    try:
        return create_inventory_item(item)
    except DuplicateItemError as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"An item named '{error}' already exists",
        ) from error
