---
layout: default
title: "Lab 3: Agent Skills"
permalink: /exercises/module-1/agent-skill/
parent: "Module 1: Copilot Multi-Agent Architecture"
nav_order: 3
---

# Lab 3: Create and verify an Agent Skill

**Suggested duration:** 15 minutes

## Objective

Package a reusable Python test workflow so Copilot can apply it when relevant.

## Agent versus skill

A custom agent defines a focused role and its available tools. An Agent Skill packages task-specific instructions and may include supporting scripts, templates, or reference material. A skill is not another agent role.

## Task

1. In the Agent Customizations editor, open **Skills** and create a workspace skill named `python-test-workflow`, or inspect the example at `.github/skills/python-test-workflow/SKILL.md`.
2. Confirm that the skill has a clear name and description. Its instructions should tell Copilot to find and run the relevant standard-library `unittest` tests and report the exact command and outcome.
3. Invoke `/python-test-workflow` in a fresh chat and ask it to validate the demo project.
4. Separately, ask a natural-language request that should match the skill. Check whether it is selected automatically; automatic selection is not guaranteed.
5. Verify the command and result in the terminal rather than relying only on the agent's summary.

Workspace skills use `.github/skills/<skill-name>/SKILL.md`. Add scripts or other resources only when the workflow needs them, and inspect them before use.

## Individual build

Create a second small skill for a repeatable workflow you use (for example, reviewing a Python diff or generating a test checklist). State when it applies, what inputs it needs, ordered steps, and what evidence it must report. Keep this exercise read-only; do not bundle scripts or grant extra tool access unless there is a justified need.

## Deliverable

Show the skill directory, its `SKILL.md`, and evidence from at least one invocation. Note whether the skill was explicitly invoked or selected automatically.

## Reflection

How is the skill different from a custom agent and from repository-wide instructions? What made the skill discoverable? How did you verify its behavior rather than relying on its description?
