# Modules 4–6: Python database-context tool

This single starter is used progressively:

| Module | Use of the same project |
|---|---|
| 4 — Extensibility architecture | Trace the boundary and review the named tool contract. Do not build a webhook bridge. |
| 5 — Database context | Run the FastAPI service, inspect safe MySQL metadata operations, and extend/test one endpoint. |
| 6 — Hands-on lab | Run the MCP stdio server that calls the local API, connect it to Copilot, and verify actual tool results. |

The default **fixture mode** runs offline with synthetic schema metadata. Optional MySQL mode reads metadata from a local training database. Both modes expose only a fixed allowlist of read-only schema operations; there is no arbitrary SQL endpoint.

## Prerequisites

- Python 3.11 or later.
- VS Code with a Copilot surface that supports MCP for the end-to-end exercise.
- Optional: local MySQL 8+ and MySQL Workbench for live metadata validation.

## Install and run the offline starter

From this directory, create a local environment and install the requirements:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
Copy-Item .env.example .env
```

Edit `.env` and replace `TOOL_API_KEY` with a local throwaway value. Keep `.env` untracked. For fixture mode, leave `SCHEMA_SOURCE=fixture`.

Run the tests:

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

Start the API on loopback only:

```powershell
.\.venv\Scripts\python.exe -m uvicorn database_context.main:app --host 127.0.0.1 --port 8000
```

Open `http://127.0.0.1:8000/docs` and try `GET /health`, then use an `X-API-Key` header for the schema routes. The service binds to loopback; do not expose it through a tunnel or public interface during this lab.

## Optional live MySQL mode

1. Run `schema.sql` in a disposable local MySQL instance. It creates synthetic `training_company` tables.
2. Create a dedicated read-only user restricted to that schema. Grant only the metadata/table-read privileges needed for the exercise.
3. Set `SCHEMA_SOURCE=mysql` and the connection values in `.env`.
4. Restrict `SCHEMA_ALLOWLIST` to the tables learners are allowed to inspect.
5. Restart the API and compare its metadata responses with MySQL Workbench.

Never use production credentials or customer data. The API's local API key is a lab boundary, not a production identity/tenant authorization system.

## Module 6: configure the MCP bridge

The MCP process is a separate stdio server. It calls the local API; it does not connect directly to MySQL. Review `copilot-mcp-config.example.json` and adapt it for your local paths. It is an example for the **user-level Copilot `mcp-config.json`** (or the VS Code Copilot MCP configuration editor), where a working directory can be set. A workspace-root `.mcp.json` is an alternative with different field support; check the current reference before using it. Do not use the deprecated `.vscode/mcp.json` format for a new Copilot-harness setup.

Set `CONTEXT_API_KEY` in the environment of the process that launches the MCP server, with the same throwaway value as `TOOL_API_KEY`. The example uses an environment-variable reference; it does not contain the key. Restart VS Code after changing its parent environment if needed.

The MCP server provides `list_schema_tables`, `get_table_columns`, `get_table_constraints`, `get_table_indexes`, and `get_table_ddl`. Select only the tools needed. Inspect startup requests and tool activity; verify an answer against the API fixture or local MySQL metadata.

## Security and failure checks

- Missing/wrong API key: request is rejected.
- Unknown or non-allowlisted table: safe not-found response.
- Excess metadata: response is capped and reports truncation.
- Database unavailable or configuration invalid: safe service error; logs retain diagnostic detail.
- Caller-supplied SQL is never accepted. Values use driver parameters; table identifiers are allowlisted and quoted only after validation.

## Test limits

The unit/API suite uses fixture mode and does not require MySQL or a Copilot account. It does not prove live MySQL privileges, OS secret handling, MCP discovery in every Copilot surface, or production authorization. Record those checks separately when unavailable.
