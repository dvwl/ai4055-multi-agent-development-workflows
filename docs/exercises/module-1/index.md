---
layout: default
title: "Module 1: Copilot Multi-Agent Architecture"
permalink: /exercises/module-1/
parent: Exercises
nav_order: 1
has_children: true
---

# Module 1: Introduction to Copilot Multi-Agent Architecture

## Before you start

- VS Code with GitHub Copilot enabled and access to Agent Mode.
- Python 3.9 or later.
- This repository opened as the VS Code workspace root so its `.github/agents/` and `.github/skills/` customizations are available.

The exact labels in VS Code can vary by version. The labs focus on the workspace files and on verifying what Copilot actually does.

## Learning outcomes

- Explain the agent lifecycle: receive, ground, plan, act, evaluate, and report.
- Create and test role-focused custom agents.
- Create and invoke a reusable Agent Skill.
- Use a planned, human-reviewed handoff to make a bounded multi-file Python change.

## Lab sequence

1. [Inspect the starter project and trace the agent lifecycle](https://dvwl.github.io/ai4055-multi-agent-development-workflows/exercises/module-1/inspect-and-plan/)
2. [Create and verify custom agents](https://dvwl.github.io/ai4055-multi-agent-development-workflows/exercises/module-1/custom-agents/)
3. [Create and verify an Agent Skill](https://dvwl.github.io/ai4055-multi-agent-development-workflows/exercises/module-1/agent-skill/)
4. [Run the human-reviewed multi-agent workflow](https://dvwl.github.io/ai4055-multi-agent-development-workflows/exercises/module-1/reviewed-refactor/)

[Open the Python demo project](https://dvwl.github.io/ai4055-multi-agent-development-workflows/demos/)

## Success criteria

At the end, you should be able to show:

- A repository-grounded plan with relevant file paths and assumptions.
- Three focused custom-agent configurations and evidence that you selected and tested them.
- A skill file with a clear purpose, activation description, and test workflow.
- A reviewed Python change, relevant tests, and an accurate report of what passed.

The example agents and skill are in `.github/agents/` and `.github/skills/`. Treat them as inspectable examples; change them on a branch or make copies when performing the setup steps. For independent practice, have each learner design a distinct role (for example, test planner or documentation reviewer), explain its permitted tools, and verify it with a new task—not only reuse the instructor's prompt.
