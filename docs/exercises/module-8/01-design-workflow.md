---
layout: default
title: "Lab 1: Design a dependency-aware workflow"
permalink: /exercises/module-8/design-workflow/
parent: "Module 8: Multi-File Workflow Orchestration"
nav_order: 1
---

# Lab 1: Design a dependency-aware workflow

**Time:** 35 minutes · **Mode:** small teams

## Objective

Turn a multi-file Python change into stages with explicit inputs, outputs, dependencies, conditions, and human gates.

## Task

Use `demos/module-8-workflows/workflow-guide.md` and the Module 1 ticket service.

1. Inspect the current service, tests, call sites, and instructions without editing.
2. Draw the dependency graph for adding a filtered `find_tickets` operation.
3. Identify which tasks must be sequential and which research tasks may happen independently.
4. Write observable conditions for “proceed,” “pause for clarification,” and “verification failed.”
5. Add one human approval point before implementation and one before the final report.
6. Compare two architecture options, but choose only one to implement.

## Individual variation

Use `decision-cases.md` to make a branch for a public-contract conflict. State exactly what evidence triggers the branch and who resolves it.

## Deliverable

Workflow graph, stage contract table, conditions, and a concise risk note explaining why YAML/prompt text is not an executable orchestration engine by itself.
