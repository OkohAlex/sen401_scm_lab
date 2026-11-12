"""Request and response models for the inventory API."""

from pydantic import BaseModel, ConfigDict, Field, field_validator


class InventoryItemInput(BaseModel):
    """Validated inventory fields accepted by the API."""

    item_name: str = Field(min_length=1, max_length=120)
    quantity: int = Field(ge=0)
    price: float = Field(ge=0, allow_inf_nan=False)

    @field_validator("item_name")
    @classmethod
    def normalize_item_name(cls, value: str) -> str:
        """Strip surrounding whitespace and reject names that become blank."""
        normalized = value.strip()
        if not normalized:
            raise ValueError("item_name must not be blank")
        return normalized


class InventoryItem(InventoryItemInput):
    """Inventory item returned by the API."""

    model_config = ConfigDict(from_attributes=True)

    id: int
