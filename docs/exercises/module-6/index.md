---
layout: default
title: "Module 6: Hands-On Technical Lab"
permalink: /exercises/module-6/
parent: Exercises
nav_order: 6
---

# Module 6: Hands-On Technical Lab

Run the shared Python FastAPI schema-context API and connect it to a supported MCP tool bridge. The included sample is read-only and synthetic by default; no cloud service or MySQL installation is required for the offline portion.

## Learning outcomes

- Run and test the API without MySQL.
- Optionally connect it to a local MySQL schema using a restricted account and local-only secrets.
- Register the separate stdio MCP server in a supported Copilot client.
- Verify tool results against authoritative schema evidence before relying on an answer.

## Lab pages

1. [Register the MCP tools](https://dvwl.github.io/ai4055-multi-agent-development-workflows/exercises/module-6/register-mcp-tools/)
2. [Verify the end-to-end workflow](https://dvwl.github.io/ai4055-multi-agent-development-workflows/exercises/module-6/end-to-end-challenge/)

## Lab sequence

1. Open the course repository root in VS Code so workspace agents and instructions are discoverable. In the integrated terminal, change to `demos/module-4-6-python/` and follow its README setup steps.
2. Run the tests, start the API on `127.0.0.1`, and inspect the health and schema routes.
3. Configure `.env` and a local MySQL read-only account only if performing live verification. The included SQL schema is synthetic; never substitute production credentials or records.
4. Start the API, then enable the documented stdio MCP server configuration. Verify the tools are discovered and inspect at least one tool invocation and its response.
5. Ask for a table's columns and constraints. Compare the answer with the API result and, when using MySQL, `DESCRIBE`, `SHOW CREATE TABLE`, or `SHOW INDEX` output.
6. Test an unallowlisted table and document the backend rejection. Record whether the evidence came from the fixture or a live MySQL connection.

## Completion criteria

- Offline Python tests pass and the synthetic API responds with bounded schema metadata.
- The MCP bridge exposes named, read-only operations that call the API; it does not expose raw SQL.
- Any MySQL connection is local, read-only, allowlisted, and configured with secrets outside source control.
- A human verifies the tool trace and response against the source schema. A plausible Copilot answer alone is not evidence.

## Verification boundary

The included unit/API tests require no MySQL or Copilot account. Live MySQL queries require a separately configured local MySQL instance and privileges; live MCP discovery requires a compatible Copilot surface and its current MCP configuration. Record those as unverified if unavailable.

## Independent challenge and reflection

Without naming a tool in the prompt, ask a question that should require schema discovery. Inspect the call and compare the result with the API/MySQL source. Then ask an unsupported question and check that the assistant states the limit. Finally, stop the API or use a wrong test key and record which layer fails and what evidence helped diagnose it.
