---
layout: default
title: "Module 4: Copilot Extensibility Architecture"
permalink: /exercises/module-4/
parent: Exercises
nav_order: 4
---

# Module 4: Copilot Extensibility Architecture

Design a narrow, reviewable path from a Copilot workflow to an approved capability. This Python-only exercise uses the shared starter at `demos/module-4-6-python/`.

## Learning outcomes

- Distinguish custom-agent instructions, MCP tools, backend APIs, and webhooks.
- Choose a supported tool integration for the Copilot surface you will use.
- Specify a typed request and bounded response without offering arbitrary SQL or URL execution.
- Identify where authentication, authorization, validation, and data minimization belong.

## Lab pages

1. [Choose the integration pattern](https://dvwl.github.io/ai4055-multi-agent-development-workflows/exercises/module-4/choose-integration-pattern/)
2. [Design a tool contract](https://dvwl.github.io/ai4055-multi-agent-development-workflows/exercises/module-4/design-tool-contract/)

## Guided exercise: design the tool boundary

1. Read `demos/module-4-6-python/README.md` and inspect the API routes and MCP server.
2. In a short sequence or architecture sketch, show: user → Copilot agent → MCP tool → local FastAPI operation → allowlisted schema metadata.
3. For `get_table_columns`, record its input, success response, not-found behavior, and output limits. Identify which validations happen in the backend rather than in the prompt.
4. Compare the agent file with the MCP configuration. Explain why the custom-agent file does not itself forward prompts to an arbitrary webhook or register API routes.
5. Classify each example: Copilot invokes an MCP tool; an API validates an operation; an external service sends a webhook event; an agent profile changes instructions.
6. Review the local security checklist. Point out where credentials live, why table names are allowlisted, and what must change before exposing the service beyond loopback.

## Deliverable and review checklist

Submit an architecture sketch and a one-page tool contract for one schema operation. The design passes when it:

- Names the Copilot surface and a supported tool mechanism; does not treat a webhook as a Copilot tool by default.
- Maps natural language to fixed operations, not executable SQL.
- Keeps MySQL credentials in an ignored local environment file and applies backend-side allowlists and bounded responses.
- Returns only synthetic/schema metadata needed for the task and records remaining production controls.
- Includes a human check of actual tool calls and returned evidence.

## Local verification

Use the runnable API and offline tests in `demos/module-4-6-python/README.md`. The demo mode needs no MySQL. Confirm the exact MCP support and configuration for your installed VS Code/Copilot surface; a custom agent and an MCP server are separate configuration pieces.

## Independent practice

Choose an internal capability such as build status or documentation lookup. Do not connect to a real system. Submit a one-page decision record with the initiating actor, target Copilot surface, tool transport, backend responsibility, authentication owner, input/output contract, failure cases, and one rejected alternative. Peer-review another team's trust boundary before Module 5.
