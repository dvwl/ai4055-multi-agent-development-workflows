import os
import unittest
from unittest.mock import patch

from database_context.providers import MySQLProvider, TableUnavailable


class FakeCursor:
    def __init__(self, rows: list[dict[str, object]]) -> None:
        self.rows = rows
        self.executed: tuple[str, tuple[object, ...]] | None = None

    def execute(self, query: str, params: tuple[object, ...] = ()) -> None:
        self.executed = (query, params)

    def fetchall(self) -> list[dict[str, object]]:
        return self.rows

    def close(self) -> None:
        pass


class FakeConnection:
    def __init__(self, rows: list[dict[str, object]]) -> None:
        self.cursor_instance = FakeCursor(rows)

    def cursor(self, dictionary: bool = False) -> FakeCursor:
        return self.cursor_instance

    def close(self) -> None:
        pass


class MySQLProviderTests(unittest.TestCase):
    def test_rejects_unallowlisted_identifier_before_connecting(self) -> None:
        connect_calls: list[object] = []
        provider = MySQLProvider(connector=lambda **kwargs: connect_calls.append(kwargs))

        with self.assertRaises(TableUnavailable):
            provider.get_columns("customers` OR 1=1 --")

        self.assertEqual([], connect_calls)

    def test_table_name_is_bound_as_a_value_after_allowlist_check(self) -> None:
        validation = FakeConnection([{"TABLE_NAME": "customers"}])
        columns = FakeConnection([{"name": "customer_id", "type": "bigint"}])
        connections = iter([validation, columns])
        with patch.dict(
            os.environ,
            {
                "MYSQL_HOST": "127.0.0.1",
                "MYSQL_DATABASE": "training_company",
                "MYSQL_USER": "reader",
                "MYSQL_PASSWORD": "local-only",
            },
        ):
            provider = MySQLProvider(connector=lambda **kwargs: next(connections))
            result = provider.get_columns("customers")

        self.assertEqual("customers", result["table"])
        self.assertEqual("customers", columns.cursor_instance.executed[1][0])
        self.assertIn("TABLE_NAME = %s", columns.cursor_instance.executed[0])
        self.assertNotIn("customers", columns.cursor_instance.executed[0])


if __name__ == "__main__":
    unittest.main()
