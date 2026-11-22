"""Local environment configuration for the schema-context demo."""

import os

from dotenv import load_dotenv

load_dotenv()


class SettingsError(ValueError):
    """Raised when local database settings are incomplete or invalid."""


DEFAULT_TABLES = ("customers", "orders", "order_items", "products")


def allowed_tables() -> tuple[str, ...]:
    configured = os.getenv("SCHEMA_ALLOWLIST", ",".join(DEFAULT_TABLES))
    tables = tuple(name.strip() for name in configured.split(",") if name.strip())
    if not tables:
        raise SettingsError("SCHEMA_ALLOWLIST must contain at least one table")
    if any(not name.replace("_", "").isalnum() for name in tables):
        raise SettingsError("SCHEMA_ALLOWLIST contains an invalid table identifier")
    return tables


def mysql_config() -> dict[str, str | int]:
    required = ("MYSQL_HOST", "MYSQL_DATABASE", "MYSQL_USER", "MYSQL_PASSWORD")
    missing = [name for name in required if not os.getenv(name)]
    if missing:
        raise SettingsError(f"Missing required MySQL settings: {', '.join(missing)}")
    try:
        port = int(os.getenv("MYSQL_PORT", "3306"))
    except ValueError as exc:
        raise SettingsError("MYSQL_PORT must be an integer") from exc
    if not 1 <= port <= 65535:
        raise SettingsError("MYSQL_PORT must be between 1 and 65535")
    return {
        "host": os.environ["MYSQL_HOST"],
        "port": port,
        "database": os.environ["MYSQL_DATABASE"],
        "user": os.environ["MYSQL_USER"],
        "password": os.environ["MYSQL_PASSWORD"],
        "connection_timeout": 5,
    }
