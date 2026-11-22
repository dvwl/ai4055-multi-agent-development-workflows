---
layout: default
title: "Lab 4: Human-reviewed agent workflow"
permalink: /exercises/module-1/reviewed-refactor/
parent: "Module 1: Copilot Multi-Agent Architecture"
nav_order: 4
---

# Lab 4: Run a human-reviewed agent workflow

**Suggested duration:** 20 minutes

## Objective

Use distinct agent roles in sequence to make a bounded Python change while keeping the developer in control.

## Change request

Refactor the ticket-query service to add one `find_tickets` operation with optional status and minimum-priority filters. It must return tickets:

- matching the requested filters (the lab request will ask for open tickets at priority 2 or higher);
- ordered by descending priority, then ascending ticket ID.

Keep the input collection unchanged. Preserve the existing helper behavior, and add tests for the new operation and its edge cases.

## Workflow

1. Run the inspect-and-plan task from [Lab 1](https://dvwl.github.io/ai4055-multi-agent-development-workflows/exercises/module-1/inspect-and-plan/). Review the files and assumptions the planner cites.
2. Select the implementer only after you approve the plan. Ask it to implement the change and run the relevant tests.
3. Inspect the diff and run the tests yourself. Check filtering, ordering, tie-breaking, empty input, and input immutability.
4. Select the reviewer. Ask for actionable findings against the refactored service and tests; do not ask it to implement fixes.
5. Decide which findings are valid. If you request a fix, review the new diff and test evidence again.

## Individual challenge

Repeat the sequence with a different minimum priority or an additional status filter. Before implementation, write down what behavior must remain unchanged. After the reviewer responds, classify each finding as valid, not applicable, or requiring clarification, with a brief evidence-based reason.

## Expected evidence

- A small, relevant diff.
- Tests that pass locally, with the exact command recorded.
- A reviewer report grounded in the changed files.
- A short handoff note describing what you accepted, rejected, or asked to change.

The roles are invoked sequentially by the learner. This lab teaches role boundaries and review, not automatic orchestration or parallel edits.

## Debrief

Which handoff saved repetition? Where did you still need to inspect code or make a decision? What evidence would another engineer need to reproduce your conclusion?
