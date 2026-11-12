"""Integration tests for the FastAPI inventory service."""

import os
import tempfile
import unittest
from unittest.mock import patch

from fastapi.testclient import TestClient

from app.main import app


class InventoryApiTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        database_path = os.path.join(self.temporary_directory.name, "inventory.db")
        self.environment = patch.dict(os.environ, {"DATABASE_PATH": database_path})
        self.environment.start()
        self.client_context = TestClient(app)
        self.client = self.client_context.__enter__()

    def tearDown(self) -> None:
        self.client_context.__exit__(None, None, None)
        self.environment.stop()
        self.temporary_directory.cleanup()

    def test_reads_migrated_records(self) -> None:
        response = self.client.get("/api/v1/inventory")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 4)
        self.assertEqual(response.json()[0]["item_name"], "USB-C Dock")

    def test_creates_and_reads_inventory_record(self) -> None:
        create_response = self.client.post(
            "/api/v1/inventory",
            json={"item_name": "Desk Lamp", "quantity": 5, "price": 24.5},
        )

        self.assertEqual(create_response.status_code, 201)
        item_id = create_response.json()["id"]
        read_response = self.client.get(f"/api/v1/inventory/{item_id}")
        self.assertEqual(read_response.status_code, 200)
        self.assertEqual(read_response.json()["item_name"], "Desk Lamp")

    def test_rejects_invalid_data_and_duplicate_names(self) -> None:
        invalid_response = self.client.post(
            "/api/v1/inventory",
            json={"item_name": "Invalid", "quantity": -1, "price": 10},
        )
        duplicate_response = self.client.post(
            "/api/v1/inventory",
            json={"item_name": "USB-C Dock", "quantity": 1, "price": 10},
        )

        self.assertEqual(invalid_response.status_code, 422)
        self.assertEqual(duplicate_response.status_code, 409)

    def test_missing_item_returns_not_found(self) -> None:
        response = self.client.get("/api/v1/inventory/9999")

        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
