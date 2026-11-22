---
layout: default
title: "Lab 1: Choose the integration pattern"
permalink: /exercises/module-4/choose-integration-pattern/
parent: "Module 4: Copilot Extensibility Architecture"
nav_order: 1
---

# Lab 1: Choose the integration pattern

**Time:** 25 minutes · **Mode:** pairs

## Objective

Choose an extension path based on who initiates the interaction and which Copilot surface must use it.

## Scenarios

For each case, name the likely component and explain the boundary:

1. Copilot should read the current schema of a local training database.
2. An external build platform sends a deployment-completed event to an internal service.
3. Engineers need a reusable, read-only code-review role.
4. A Python application needs to create and control Copilot sessions programmatically.

Consider custom agent, MCP server/tool, backend API, webhook, IDE extension, and Copilot SDK. Do not treat them as synonyms.

## Steps

1. Sketch user → Copilot surface → agent → tool client → backend → protected system.
2. Mark the initiating actor, transport, authentication owner, authorization owner, and data boundary.
3. Identify which capability the custom agent file configures and which capability the actual tool server provides.
4. Check current VS Code support for the target harness before committing to an integration.
5. Swap one scenario with another pair and critique their chosen pattern.

## Deliverable

One architecture sketch and a decision table containing chosen pattern, alternative rejected, key dependency, and item to verify in current product documentation.
