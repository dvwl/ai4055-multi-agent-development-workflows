"""Local FastAPI endpoints for bounded database schema metadata."""

import hmac
import logging
import os
from collections.abc import Callable
from typing import Any

from fastapi import Depends, FastAPI, Header, HTTPException

from database_context.providers import (
    FixtureProvider,
    MySQLProvider,
    SchemaUnavailable,
    TableUnavailable,
)
from database_context.settings import SettingsError

logger = logging.getLogger(__name__)
app = FastAPI(title="AI4055 Schema Context API", version="1.0.0")


def require_tool_key(x_api_key: str | None = Header(default=None)) -> None:
    expected = os.getenv("TOOL_API_KEY", "")
    if not expected:
        raise HTTPException(status_code=503, detail="Tool authentication is not configured")
    if not x_api_key or not hmac.compare_digest(x_api_key, expected):
        raise HTTPException(status_code=401, detail="Unauthorized")


def get_provider() -> Any:
    mode = os.getenv("SCHEMA_SOURCE", "fixture").strip().lower()
    if mode == "fixture":
        return FixtureProvider()
    if mode == "mysql":
        return MySQLProvider()
    raise HTTPException(status_code=500, detail="SCHEMA_SOURCE must be fixture or mysql")


def _call(operation: Callable[[], dict[str, Any]]) -> dict[str, Any]:
    try:
        return operation()
    except TableUnavailable as exc:
        raise HTTPException(status_code=404, detail="Table is not available") from exc
    except (SchemaUnavailable, SettingsError) as exc:
        logger.exception("Schema metadata operation failed")
        raise HTTPException(status_code=503, detail="Schema data source is unavailable") from exc


@app.get("/health")
def health() -> dict[str, str]:
    """Return process liveness without contacting MySQL."""
    return {"status": "ok"}


@app.get("/schema/tables", dependencies=[Depends(require_tool_key)])
def list_tables(provider: Any = Depends(get_provider)) -> dict[str, Any]:
    return _call(provider.list_tables)


@app.get("/schema/tables/{table_name}/columns", dependencies=[Depends(require_tool_key)])
def get_columns(table_name: str, provider: Any = Depends(get_provider)) -> dict[str, Any]:
    return _call(lambda: provider.get_columns(table_name))


@app.get("/schema/tables/{table_name}/constraints", dependencies=[Depends(require_tool_key)])
def get_constraints(table_name: str, provider: Any = Depends(get_provider)) -> dict[str, Any]:
    return _call(lambda: provider.get_constraints(table_name))


@app.get("/schema/tables/{table_name}/indexes", dependencies=[Depends(require_tool_key)])
def get_indexes(table_name: str, provider: Any = Depends(get_provider)) -> dict[str, Any]:
    return _call(lambda: provider.get_indexes(table_name))


@app.get("/schema/tables/{table_name}/ddl", dependencies=[Depends(require_tool_key)])
def get_ddl(table_name: str, provider: Any = Depends(get_provider)) -> dict[str, Any]:
    return _call(lambda: provider.get_ddl(table_name))
