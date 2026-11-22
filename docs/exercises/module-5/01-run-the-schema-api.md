---
layout: default
title: "Lab 1: Run the schema API"
permalink: /exercises/module-5/run-schema-api/
parent: "Module 5: Bridging the Database Context"
nav_order: 1
---

# Lab 1: Run the schema API

**Time:** 35 minutes · **Mode:** guided, then individual

## Objective

Run the shared FastAPI starter in fixture mode and trace API responses back to the provider.

## Setup

Follow `demos/module-4-6-python/README.md` to create the virtual environment, install requirements, and copy `.env.example`. Set a local throwaway `TOOL_API_KEY`; leave `SCHEMA_SOURCE=fixture`.

From the demo folder, run the tests and start the server:

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
.\.venv\Scripts\python.exe -m uvicorn database_context.main:app --host 127.0.0.1 --port 8000
```

Open `http://127.0.0.1:8000/docs`. The health route is unauthenticated liveness; schema routes require `X-API-Key`.

## Guided task

1. Call `/schema/tables` using the API key.
2. Request columns and constraints for `orders`.
3. Follow the call from FastAPI route → provider → fixture data.
4. Compare the response to `schema.sql` and record any intentional differences.
5. Call a table not in the allowlist and record the status code and response.

## Independent task

Choose `products` or `order_items`. Predict the output before calling the route; then compare the actual JSON with the fixture and SQL schema. Explain each mismatch or truncation flag.

## Evidence

Capture the test result, one successful response, one safe rejection, and the source file that produced each result. Do not capture the API key in screenshots or logs.
