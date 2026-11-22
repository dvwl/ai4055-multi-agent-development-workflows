---
layout: default
title: "Lab 2: Design a tool contract"
permalink: /exercises/module-4/design-tool-contract/
parent: "Module 4: Copilot Extensibility Architecture"
nav_order: 2
---

# Lab 2: Design a tool contract

**Time:** 35 minutes · **Mode:** team design review

## Objective

Specify an approved operation before implementing the backend.

## Contract task

Design `get_table_columns(table_name)` for the synthetic training schema. Include:

- Input type, required/optional status, and validation.
- Example successful response and maximum result size.
- Unknown table, unauthorized request, and database-unavailable behavior.
- Authentication and authorization responsibilities.
- Data that must not be returned.
- Logging and correlation data that must not leak secrets.

## Threat review

Review your design against these requests:

1. A table name containing SQL punctuation or an injection attempt.
2. A valid table outside the approved schema allowlist.
3. A table with very large DDL or metadata.
4. A caller without credentials.
5. A legitimate user asking for arbitrary SQL execution.

For each, state which backend control handles it and the safe response. Prompt instructions are not the enforcement point.

## Independent redesign

Design `get_latest_orders(customer_id, limit)` as a conceptual contract only. Specify server-side authorization/tenant scope, parameter binding, a hard maximum limit, minimized response fields, and tests. Do not implement customer lookup in the schema-only demo.

## Deliverable

Contract table, three failure cases, and a reviewer sign-off that there is no generic SQL or arbitrary-URL tool.
