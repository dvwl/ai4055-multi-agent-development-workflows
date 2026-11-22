---
layout: default
title: "Lab 1: Register the MCP tools"
permalink: /exercises/module-6/register-mcp-tools/
parent: "Module 6: Hands-On Technical Lab"
nav_order: 1
---

# Lab 1: Register the MCP tools

**Time:** 40 minutes · **Mode:** instructor demo, then individual setup

## Objective

Connect Copilot to the stdio MCP server that calls the local API. The MCP server and API are distinct processes; neither is configured by the custom-agent file alone.

## Steps

1. Complete Module 5 in fixture mode and confirm the API is running on `127.0.0.1:8000`.
2. Set `CONTEXT_API_KEY` in the environment used to launch VS Code, matching the local API key. Do not paste the secret into chat or commit it.
3. Copy `copilot-mcp-config.example.json` to the supported **user-level Copilot `mcp-config.json`** location or use the Agent Customizations MCP editor. Replace the sample executable and working-directory paths with local absolute paths.
4. Review the `databaseContext` server command, five named tools, environment references, and startup/trust prompts before enabling it.
5. Restart or reload the Copilot session as needed; check the selected harness and inspect the tool inventory.
6. Ask Copilot to list schema tables. Expand the tool call and verify the output against the fixture/API.

Current config locations and fields vary by harness. Use the current [VS Code MCP setup guide](https://code.visualstudio.com/docs/agent-customization/mcp-servers) and [configuration reference](https://code.visualstudio.com/docs/agents/reference/mcp-configuration). Do not copy secrets to a shared workspace `.mcp.json`.

## Troubleshooting evidence

Record whether the failure is MCP startup, API connectivity, API authentication, MySQL/fixture provider, or Copilot tool selection. Capture the safe error only—never credentials.

## Deliverable

Local configuration path (without secret values), discovered tool names, one expanded tool trace, and one verified response.
