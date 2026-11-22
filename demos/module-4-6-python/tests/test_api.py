import os
import unittest
from unittest.mock import patch

from fastapi.testclient import TestClient

from database_context.main import app, get_provider
from database_context.providers import FixtureProvider


class SchemaApiTests(unittest.TestCase):
    def setUp(self) -> None:
        self.env = patch.dict(os.environ, {"TOOL_API_KEY": "test-only-key", "SCHEMA_SOURCE": "fixture"})
        self.env.start()
        app.dependency_overrides[get_provider] = FixtureProvider
        self.client = TestClient(app)

    def tearDown(self) -> None:
        app.dependency_overrides.clear()
        self.env.stop()

    def test_health_does_not_require_database_or_api_key(self) -> None:
        response = self.client.get("/health")

        self.assertEqual(200, response.status_code)
        self.assertEqual({"status": "ok"}, response.json())

    def test_schema_endpoint_requires_api_key(self) -> None:
        response = self.client.get("/schema/tables")

        self.assertEqual(401, response.status_code)

    def test_lists_fixture_tables_with_valid_key(self) -> None:
        response = self.client.get("/schema/tables", headers={"X-API-Key": "test-only-key"})

        self.assertEqual(200, response.status_code)
        self.assertEqual("training_company_fixture", response.json()["schema"])
        self.assertIn("customers", response.json()["tables"])

    def test_describes_allowed_table(self) -> None:
        response = self.client.get(
            "/schema/tables/orders/constraints", headers={"X-API-Key": "test-only-key"}
        )

        self.assertEqual(200, response.status_code)
        self.assertEqual("customers", response.json()["constraints"][1]["references_table"])

    def test_unknown_table_returns_safe_not_found(self) -> None:
        response = self.client.get(
            "/schema/tables/not_a_table/columns", headers={"X-API-Key": "test-only-key"}
        )

        self.assertEqual(404, response.status_code)
        self.assertEqual({"detail": "Table is not available"}, response.json())

    def test_invalid_table_identifier_is_not_reflected(self) -> None:
        response = self.client.get(
            "/schema/tables/customers%27%20OR%201%3D1/columns",
            headers={"X-API-Key": "test-only-key"},
        )

        self.assertEqual(404, response.status_code)
        self.assertNotIn("OR 1=1", response.text)


if __name__ == "__main__":
    unittest.main()
