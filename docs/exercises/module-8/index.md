---
layout: default
title: "Module 8: Multi-File Workflow Orchestration"
permalink: /exercises/module-8/
parent: Exercises
nav_order: 8
---

# Module 8: Multi-File Declarative Workflow Orchestration

## Lab pages

1. [Design a dependency-aware workflow](https://dvwl.github.io/ai4055-multi-agent-development-workflows/exercises/module-8/design-workflow/)
2. [Run the workflow and recover](https://dvwl.github.io/ai4055-multi-agent-development-workflows/exercises/module-8/run-and-recover/)

Turn a broad change into inspectable stages with dependencies, decision gates, and verification. A written workflow description is not executable unless a compatible runner interprets it.

## Lab: Orchestrate a multi-file refactor

Use the ticket-service project in [Module 1](https://dvwl.github.io/ai4055-multi-agent-development-workflows/exercises/module-1/) and the workflow guide in `demos/module-8-workflows/`.

1. **Analyse:** inspect the existing feature, tests, callers, and repository instructions without editing.
2. **Plan:** produce a dependency map, acceptance criteria, test plan, and open questions.
3. **Compare:** describe two plausible designs and trade-offs; do not implement both.
4. **Approve:** a human selects one design and confirms the allowed files.
5. **Implement sequentially:** update the domain/service contract first, then implementation and tests. Stop at each review gate.
6. **Verify:** run focused tests, then the full relevant suite; inspect the complete diff.

The example prompt chain is in `.github/prompts/`. It is invoked step by step; it is not a universal Copilot workflow engine. Use parallel research only for independent tasks, and do not run agents concurrently on shared files in this lab.

### Independent practice

Choose one adjacent but independent task (for example, adding a README usage example) and decide whether it can be researched or implemented in parallel. State the shared-file/integration risk. Do not actually parallelize edits to the ticket service; instead explain the synchronization gate you would require.

## Conditional decision exercise

Use the case in `demos/module-8-workflows/decision-cases.md` to define a conditional path. State observable criteria for each branch and identify the human approval point. The branch is a plan until a compatible workflow implementation executes it.

## Deliverable and success criteria

- A readable workflow with explicit inputs, outputs, dependencies, stop conditions, and human gates.
- One approved implementation path, not competing edits.
- Passing test evidence and a reviewed diff.
- A short note explaining which tasks could be parallelized safely and why.

## Assessment rubric

| Criterion | Evidence |
|---|---|
| Dependency order | Contract and callers are mapped; implementation follows dependencies. |
| Decision quality | Alternatives and conditions are explicit; only one path is approved. |
| Change control | Scope, stop condition, and human gates are documented. |
| Verification | Relevant tests actually run; failures are accurately reported. |
| Integration | Final diff is coherent across source, tests, and docs. |
