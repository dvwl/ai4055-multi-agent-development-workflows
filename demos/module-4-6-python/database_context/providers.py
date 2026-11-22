"""Fixture and MySQL implementations of the read-only schema provider."""

from collections.abc import Callable
from typing import Any

import mysql.connector
from mysql.connector import Error as MySQLError

from database_context.settings import SettingsError, allowed_tables, mysql_config

MAX_METADATA_ROWS = 200
MAX_DDL_CHARS = 16000

FIXTURE = {
    "customers": {
        "columns": [
            {"name": "customer_id", "type": "bigint", "nullable": False, "key": "PRI", "extra": "auto_increment"},
            {"name": "email", "type": "varchar(255)", "nullable": False, "key": "UNI", "extra": ""},
            {"name": "display_name", "type": "varchar(120)", "nullable": False, "key": "", "extra": ""},
            {"name": "status", "type": "enum", "nullable": False, "key": "MUL", "extra": ""},
            {"name": "created_at", "type": "timestamp", "nullable": False, "key": "", "extra": "DEFAULT_GENERATED"},
        ],
        "constraints": [
            {"name": "PRIMARY", "type": "PRIMARY KEY", "column": "customer_id", "references_table": None, "references_column": None},
            {"name": "uq_customers_email", "type": "UNIQUE", "column": "email", "references_table": None, "references_column": None},
        ],
        "indexes": [
            {"name": "PRIMARY", "column": "customer_id", "sequence": 1, "unique": True, "type": "BTREE"},
            {"name": "uq_customers_email", "column": "email", "sequence": 1, "unique": True, "type": "BTREE"},
            {"name": "ix_customers_status_created", "column": "status", "sequence": 1, "unique": False, "type": "BTREE"},
            {"name": "ix_customers_status_created", "column": "created_at", "sequence": 2, "unique": False, "type": "BTREE"},
        ],
        "ddl": "CREATE TABLE customers (customer_id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY, email VARCHAR(255) NOT NULL UNIQUE, display_name VARCHAR(120) NOT NULL, status ENUM('active','paused','closed') NOT NULL DEFAULT 'active', created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP)",
    },
    "orders": {
        "columns": [
            {"name": "order_id", "type": "bigint", "nullable": False, "key": "PRI", "extra": "auto_increment"},
            {"name": "customer_id", "type": "bigint", "nullable": False, "key": "MUL", "extra": ""},
            {"name": "order_status", "type": "enum", "nullable": False, "key": "", "extra": ""},
            {"name": "created_at", "type": "timestamp", "nullable": False, "key": "", "extra": "DEFAULT_GENERATED"},
        ],
        "constraints": [
            {"name": "PRIMARY", "type": "PRIMARY KEY", "column": "order_id", "references_table": None, "references_column": None},
            {"name": "fk_orders_customer", "type": "FOREIGN KEY", "column": "customer_id", "references_table": "customers", "references_column": "customer_id"},
        ],
        "indexes": [
            {"name": "PRIMARY", "column": "order_id", "sequence": 1, "unique": True, "type": "BTREE"},
            {"name": "ix_orders_customer_created", "column": "customer_id", "sequence": 1, "unique": False, "type": "BTREE"},
            {"name": "ix_orders_customer_created", "column": "created_at", "sequence": 2, "unique": False, "type": "BTREE"},
        ],
        "ddl": "CREATE TABLE orders (order_id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY, customer_id BIGINT NOT NULL, order_status ENUM('new','processing','complete','cancelled') NOT NULL, created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, CONSTRAINT fk_orders_customer FOREIGN KEY (customer_id) REFERENCES customers (customer_id))",
    },
    "order_items": {
        "columns": [
            {"name": "order_id", "type": "bigint", "nullable": False, "key": "PRI", "extra": ""},
            {"name": "product_id", "type": "bigint", "nullable": False, "key": "PRI", "extra": ""},
            {"name": "quantity", "type": "int", "nullable": False, "key": "", "extra": ""},
        ],
        "constraints": [
            {"name": "PRIMARY", "type": "PRIMARY KEY", "column": "order_id", "references_table": None, "references_column": None},
            {"name": "PRIMARY", "type": "PRIMARY KEY", "column": "product_id", "references_table": None, "references_column": None},
            {"name": "fk_order_items_order", "type": "FOREIGN KEY", "column": "order_id", "references_table": "orders", "references_column": "order_id"},
            {"name": "fk_order_items_product", "type": "FOREIGN KEY", "column": "product_id", "references_table": "products", "references_column": "product_id"},
        ],
        "indexes": [{"name": "PRIMARY", "column": "order_id", "sequence": 1, "unique": True, "type": "BTREE"}, {"name": "PRIMARY", "column": "product_id", "sequence": 2, "unique": True, "type": "BTREE"}],
        "ddl": "CREATE TABLE order_items (order_id BIGINT NOT NULL, product_id BIGINT NOT NULL, quantity INT NOT NULL, PRIMARY KEY (order_id, product_id))",
    },
    "products": {
        "columns": [
            {"name": "product_id", "type": "bigint", "nullable": False, "key": "PRI", "extra": "auto_increment"},
            {"name": "product_name", "type": "varchar(160)", "nullable": False, "key": "", "extra": ""},
            {"name": "active", "type": "tinyint(1)", "nullable": False, "key": "MUL", "extra": "DEFAULT_GENERATED"},
        ],
        "constraints": [{"name": "PRIMARY", "type": "PRIMARY KEY", "column": "product_id", "references_table": None, "references_column": None}],
        "indexes": [{"name": "PRIMARY", "column": "product_id", "sequence": 1, "unique": True, "type": "BTREE"}, {"name": "ix_products_active", "column": "active", "sequence": 1, "unique": False, "type": "BTREE"}],
        "ddl": "CREATE TABLE products (product_id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY, product_name VARCHAR(160) NOT NULL, active BOOLEAN NOT NULL DEFAULT TRUE)",
    },
}


class TableUnavailable(Exception):
    """Raised for unknown or non-allowlisted table names."""


class SchemaUnavailable(Exception):
    """Raised when schema metadata cannot be retrieved."""


class FixtureProvider:
    def list_tables(self) -> dict[str, Any]:
        names = [name for name in allowed_tables() if name in FIXTURE]
        return {"schema": "training_company_fixture", "tables": names, "truncated": False}

    def _table(self, table_name: str) -> dict[str, Any]:
        if table_name not in allowed_tables() or table_name not in FIXTURE:
            raise TableUnavailable
        return FIXTURE[table_name]

    def get_columns(self, table_name: str) -> dict[str, Any]:
        return self._bounded(table_name, "columns")

    def get_constraints(self, table_name: str) -> dict[str, Any]:
        return self._bounded(table_name, "constraints")

    def get_indexes(self, table_name: str) -> dict[str, Any]:
        return self._bounded(table_name, "indexes")

    def get_ddl(self, table_name: str) -> dict[str, Any]:
        ddl = self._table(table_name)["ddl"]
        return {"table": table_name, "ddl": ddl[:MAX_DDL_CHARS], "truncated": len(ddl) > MAX_DDL_CHARS}

    def _bounded(self, table_name: str, key: str) -> dict[str, Any]:
        rows = self._table(table_name)[key]
        return {"table": table_name, key: rows[:MAX_METADATA_ROWS], "truncated": len(rows) > MAX_METADATA_ROWS}


class MySQLProvider:
    def __init__(self, connector: Callable[..., Any] | None = None) -> None:
        if connector is None:
            import mysql.connector

            connector = mysql.connector.connect
        self._connector = connector

    def _fetch(self, query: str, params: tuple[Any, ...] = ()) -> list[dict[str, Any]]:
        connection = None
        cursor = None
        try:
            config = mysql_config()
        except SettingsError as exc:
            raise SchemaUnavailable("The schema data source is not configured") from exc
        try:
            connection = self._connector(**config)
            cursor = connection.cursor(dictionary=True)
            cursor.execute(query, params)
            return cursor.fetchall()
        except MySQLError as exc:
            raise SchemaUnavailable("The schema data source is unavailable") from exc
        finally:
            if cursor is not None:
                cursor.close()
            if connection is not None:
                connection.close()

    def _validate_table(self, table_name: str) -> None:
        if table_name not in allowed_tables():
            raise TableUnavailable
        rows = self._fetch(
            "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES "
            "WHERE TABLE_SCHEMA = DATABASE() AND TABLE_NAME = %s "
            "AND TABLE_TYPE = 'BASE TABLE' LIMIT 1",
            (table_name,),
        )
        if not rows:
            raise TableUnavailable

    def list_tables(self) -> dict[str, Any]:
        names = allowed_tables()
        placeholders = ", ".join("%s" for _ in names)
        rows = self._fetch(
            "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES "
            f"WHERE TABLE_SCHEMA = DATABASE() AND TABLE_TYPE = 'BASE TABLE' AND TABLE_NAME IN ({placeholders}) "
            "ORDER BY TABLE_NAME LIMIT %s",
            (*names, MAX_METADATA_ROWS + 1),
        )
        schema_rows = self._fetch("SELECT DATABASE() AS schema_name")
        tables = [row["TABLE_NAME"] for row in rows[:MAX_METADATA_ROWS]]
        return {
            "schema": schema_rows[0]["schema_name"] if schema_rows else None,
            "tables": tables,
            "truncated": len(rows) > MAX_METADATA_ROWS,
        }

    def get_columns(self, table_name: str) -> dict[str, Any]:
        self._validate_table(table_name)
        rows = self._fetch(
            "SELECT COLUMN_NAME AS name, COLUMN_TYPE AS type, IS_NULLABLE AS nullable, "
            "COLUMN_DEFAULT AS `default`, COLUMN_KEY AS `key`, EXTRA AS extra "
            "FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = DATABASE() "
            "AND TABLE_NAME = %s ORDER BY ORDINAL_POSITION LIMIT %s",
            (table_name, MAX_METADATA_ROWS + 1),
        )
        return self._bounded(table_name, "columns", rows)

    def get_constraints(self, table_name: str) -> dict[str, Any]:
        self._validate_table(table_name)
        rows = self._fetch(
            "SELECT tc.CONSTRAINT_NAME AS name, tc.CONSTRAINT_TYPE AS type, "
            "kcu.COLUMN_NAME AS `column`, kcu.REFERENCED_TABLE_NAME AS references_table, "
            "kcu.REFERENCED_COLUMN_NAME AS references_column "
            "FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS AS tc "
            "LEFT JOIN INFORMATION_SCHEMA.KEY_COLUMN_USAGE AS kcu "
            "ON tc.CONSTRAINT_SCHEMA = kcu.CONSTRAINT_SCHEMA "
            "AND tc.TABLE_NAME = kcu.TABLE_NAME AND tc.CONSTRAINT_NAME = kcu.CONSTRAINT_NAME "
            "WHERE tc.CONSTRAINT_SCHEMA = DATABASE() AND tc.TABLE_NAME = %s "
            "ORDER BY tc.CONSTRAINT_NAME, kcu.ORDINAL_POSITION LIMIT %s",
            (table_name, MAX_METADATA_ROWS + 1),
        )
        return self._bounded(table_name, "constraints", rows)

    def get_indexes(self, table_name: str) -> dict[str, Any]:
        self._validate_table(table_name)
        rows = self._fetch(
            "SELECT INDEX_NAME AS name, COLUMN_NAME AS `column`, SEQ_IN_INDEX AS sequence, "
            "(NON_UNIQUE = 0) AS `unique`, INDEX_TYPE AS type "
            "FROM INFORMATION_SCHEMA.STATISTICS WHERE TABLE_SCHEMA = DATABASE() "
            "AND TABLE_NAME = %s ORDER BY INDEX_NAME, SEQ_IN_INDEX LIMIT %s",
            (table_name, MAX_METADATA_ROWS + 1),
        )
        return self._bounded(table_name, "indexes", rows)

    def get_ddl(self, table_name: str) -> dict[str, Any]:
        self._validate_table(table_name)
        quoted_identifier = "`" + table_name.replace("`", "``") + "`"
        rows = self._fetch(f"SHOW CREATE TABLE {quoted_identifier}")
        if not rows:
            raise TableUnavailable
        ddl = rows[0].get("Create Table", "")
        return {"table": table_name, "ddl": ddl[:MAX_DDL_CHARS], "truncated": len(ddl) > MAX_DDL_CHARS}

    @staticmethod
    def _bounded(table_name: str, key: str, rows: list[dict[str, Any]]) -> dict[str, Any]:
        return {"table": table_name, key: rows[:MAX_METADATA_ROWS], "truncated": len(rows) > MAX_METADATA_ROWS}
