---
layout: default
title: "Lab 2: Custom agents"
permalink: /exercises/module-1/custom-agents/
parent: "Module 1: Copilot Multi-Agent Architecture"
nav_order: 2
---

# Lab 2: Create and verify custom agents

**Suggested duration:** 25 minutes

## Objective

Configure reusable, role-focused agents and verify that their instructions and tool choices fit their responsibilities.

## Agent roles

The workspace examples are:

- `python-work-planner` — inspect the project and return a plan without editing.
- `python-implementer` — implement an approved, bounded Python change and run relevant tests.
- `python-reviewer` — inspect changes and tests, then report actionable findings without editing.

## Task

1. In VS Code, open the Agent Customizations editor from the Command Palette (**Chat: Open Customizations**) and select **Agents**.
2. Inspect the workspace agents. Confirm the planner and reviewer are read-oriented; compare their instructions with the implementer's.
3. Create a custom agent in the workspace, or adapt one of the examples. Workspace agent files use `.github/agents/<name>.agent.md`.
4. Give it a specific purpose, the input it needs, the actions it may take, and a useful output format.
5. Start a fresh chat, select the agent, and give it a small task that can be checked against the repository.
6. Review its response and tool activity. Do not infer that a “do not edit” sentence alone restricts the available tools.

## Individual build

Create a new agent rather than only reading the supplied samples. Choose either a **test planner** that returns scenarios and test cases, or a **documentation reviewer** that checks docs against actual source. Give it a narrow mission, an input expectation, a structured output, a stop condition, and only the tools needed for the role. Run one positive case and one case outside its scope; record what happened.

## Deliverable

Show the agent file and one verification run. Explain which tools the role needs and what evidence demonstrates that it behaved as intended.

## Reflection

Could ordinary repository instructions or a one-time request do this job? What recurring behavior justifies a separate custom agent? Which part of your design is guidance rather than enforceable permission?

## Checkpoint

Could the same job be handled by the default agent with a one-time prompt? If so, explain what recurring instructions, tool scope, or output format makes a custom agent worthwhile.
