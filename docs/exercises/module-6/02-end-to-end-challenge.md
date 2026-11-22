---
layout: default
title: "Lab 2: Verify the end-to-end workflow"
permalink: /exercises/module-6/end-to-end-challenge/
parent: "Module 6: Hands-On Technical Lab"
nav_order: 2
---

# Lab 2: Verify the end-to-end workflow

**Time:** 55 minutes · **Mode:** independent challenge, peer demonstration

## Challenge

Demonstrate that the answer depends on a live tool result rather than model recall.

1. Ask a natural-language question about table columns without naming the tool.
2. Inspect which tool Copilot calls and the raw structured response.
3. Compare the output to `schema.sql` in fixture mode or MySQL Workbench in live mode.
4. Ask about a nonexistent table and verify the safe rejection.
5. Ask an unsupported question about business records; show that the tool does not expose them and the assistant states the limitation.
6. Stop the API, repeat a request, and locate the failing layer. Restart the API and verify recovery.

## Optional extension

Implement or test one new **read-only schema** tool, such as a foreign-key relationship summary. Restrict it to allowlisted tables, bound the result, add a test for an unknown table, and explicitly register only the tool required. Do not add generic SQL execution.

## Peer scorecard

| Criterion | Evidence |
|---|---|
| Tool was actually invoked | Expanded call visible in Copilot activity |
| Response is grounded | Compared to API/fixture/MySQL evidence |
| Unknown input is safe | Backend rejection without SQL leakage |
| Failure is diagnosable | Correct layer identified from evidence |
| Scope is controlled | No exposed credentials or extra tool permissions |

## Deliverable

Three prompt/result pairs, scorecard, and a brief note on what remains unverified when using fixture mode instead of MySQL.
