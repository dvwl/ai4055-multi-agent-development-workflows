---
layout: default
title: "Module 5: Bridging the Database Context"
permalink: /exercises/module-5/
parent: Exercises
nav_order: 5
---

# Module 5: Bridging the Database Context

Build a small Python API that exposes approved MySQL schema context—not a general-purpose database console. Work from `demos/module-4-6-python/`; the synthetic mode and tests run without a MySQL server.

## Learning outcomes

- Map a question to a named schema operation with validated arguments.
- Discover only allowlisted table metadata from the active schema.
- Explain how parameterized metadata queries, identifier allowlists, and response limits differ.
- Return predictable JSON and safe not-found/error responses.

## Lab pages

1. [Run the schema API](https://dvwl.github.io/ai4055-multi-agent-development-workflows/exercises/module-5/run-schema-api/)
2. [Extend and secure the API](https://dvwl.github.io/ai4055-multi-agent-development-workflows/exercises/module-5/extend-secure-api/)

## Guided exercise: inspect and verify the API

1. Follow the setup and test steps in the demo README. Start the API in synthetic mode and open its local OpenAPI page.
2. Call `GET /schema/tables`, then retrieve columns, constraints, indexes, and DDL for an allowed sample table.
3. Try a table name outside the configured allowlist and an invalid identifier. Confirm the backend rejects them without running caller-supplied SQL.
4. Trace a table name from the route to the repository. Identify where the allowlist is checked and where ordinary SQL values are parameterized.
5. Review the response-size and metadata-row caps. Explain why prompt instructions alone cannot enforce them.
6. If a local MySQL instance is available, use the synthetic schema script and a dedicated read-only account, configure `.env`, then repeat the checks against the active database. Do not use production data.

## Deliverable and acceptance criteria

Provide a sample request/response pair and a short safety review. It must show:

- Purpose-specific, read-only schema operations; no `execute_sql` endpoint.
- A backend-side table allowlist, parameterized values, bounded output, and safe failures.
- Secrets supplied locally and excluded from source control.
- Synthetic data/metadata for exercises and a note that live MySQL behavior is unverified unless tested locally.
- A human comparison of returned metadata with the database or fixture source.

## Key distinction

SQL value placeholders protect values. They do not parameterize identifiers such as table names. This starter validates every requested table against a server-side allowlist before selecting metadata; it never accepts SQL from the model or caller.

## Independent extension

Design one approved synthetic business lookup. Write the contract and threat cases first; then add an allowlisted, parameterized query, minimal response fields, a result cap, and tests for invalid, missing, and unauthorized requests. Explain why a dynamic SQL identifier still needs allowlisting even when values use placeholders.
