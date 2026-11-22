---
layout: default
title: "Lab 2: Extend and secure the API"
permalink: /exercises/module-5/extend-secure-api/
parent: "Module 5: Bridging the Database Context"
nav_order: 2
---

# Lab 2: Extend and secure the API

**Time:** 55 minutes · **Mode:** guided implementation, peer review

## Objective

Implement or improve one metadata operation with bounded output and backend-side validation.

## Task

1. Inspect `database_context/providers.py` and the API tests.
2. Select one: improve the index fixture/query, verify constraint metadata, or add a focused test for a missing failure case.
3. Write expected behavior before editing.
4. Ask Copilot to propose a plan, then approve a narrow list of files.
5. Implement the smallest change and add a regression test.
6. Run the full offline test suite.
7. Review that values are bound parameters; dynamic identifiers are checked against `SCHEMA_ALLOWLIST` before use; output remains capped.

## Optional MySQL practice

With instructor approval, load `schema.sql` into a disposable local MySQL instance. Create a least-privilege reader, populate `.env`, set `SCHEMA_SOURCE=mysql`, and repeat the request. Compare against `SHOW CREATE TABLE` or `SHOW INDEX`. Skip this if local MySQL is unavailable; do not use a remote production database.

## Peer review checklist

- Does an unknown table fail before a metadata query for that table?
- Is SQL input from the model completely absent?
- Are errors safe for callers while diagnostic details stay in logs?
- Is the API bound to `127.0.0.1` for this lab?
- Does the test prove behavior rather than only assert a constant?

## Deliverable

One implementation/test change, exact test output, and a short threat-model note.
