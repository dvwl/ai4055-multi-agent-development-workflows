"""MCP stdio tools that call the local schema-context API."""

import json
import os
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen
from typing import Any

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("databaseContext")


def _get(path: str) -> dict[str, Any]:
    base_url = os.getenv("CONTEXT_API_URL", "http://127.0.0.1:8000").rstrip("/")
    api_key = os.getenv("CONTEXT_API_KEY", "")
    if not api_key:
        raise RuntimeError("CONTEXT_API_KEY is not configured in the MCP host environment")
    request = Request(
        f"{base_url}{path}",
        headers={"X-API-Key": api_key, "Accept": "application/json"},
    )
    try:
        with urlopen(request, timeout=5) as response:
            return json.loads(response.read().decode("utf-8"))
    except HTTPError as exc:
        raise RuntimeError(f"Schema API returned HTTP {exc.code}") from exc
    except URLError as exc:
        raise RuntimeError("Schema API is unavailable; confirm the local API is running") from exc


@mcp.tool()
def list_schema_tables() -> dict[str, Any]:
    """List allowlisted tables in the active training schema."""
    return _get("/schema/tables")


@mcp.tool()
def get_table_columns(table_name: str) -> dict[str, Any]:
    """Get column names, types, nullability, and keys for an available table."""
    return _get(f"/schema/tables/{quote(table_name, safe='')}/columns")


@mcp.tool()
def get_table_constraints(table_name: str) -> dict[str, Any]:
    """Get primary, foreign-key, and unique constraints for an available table."""
    return _get(f"/schema/tables/{quote(table_name, safe='')}/constraints")


@mcp.tool()
def get_table_indexes(table_name: str) -> dict[str, Any]:
    """Get index names and indexed columns for an available table."""
    return _get(f"/schema/tables/{quote(table_name, safe='')}/indexes")


@mcp.tool()
def get_table_ddl(table_name: str) -> dict[str, Any]:
    """Get bounded DDL for an available table in the training schema."""
    return _get(f"/schema/tables/{quote(table_name, safe='')}/ddl")


if __name__ == "__main__":
    mcp.run(transport="stdio")
