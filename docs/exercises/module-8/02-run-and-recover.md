---
layout: default
title: "Lab 2: Run the workflow and recover"
permalink: /exercises/module-8/run-and-recover/
parent: "Module 8: Multi-File Workflow Orchestration"
nav_order: 2
---

# Lab 2: Run the workflow and recover

**Time:** 45 minutes · **Mode:** individual, then pair review

## Steps

1. Use `.github/prompts/08-refactor-plan.prompt.md` to produce the plan. Inspect cited files and approve scope.
2. Use `.github/prompts/08-implement-approved-plan.prompt.md` only after an explicit human approval.
3. Implement the contract before the behavior and tests. Pause after each stage to inspect the diff.
4. Run focused tests, then the full Module 1 test suite.
5. If a test fails, classify it as a regression, pre-existing issue, or environment failure. Fix only an in-scope root cause; otherwise stop and report.
6. Use `.github/prompts/08-verify-and-report.prompt.md` for a read-only final review. Compare its report with the actual diff and test output.

## Parallel-work decision

Select a task adjacent to the refactor (such as independent documentation review). Decide whether it can run in parallel without editing shared files. Record synchronization and integration checks. Do not have multiple agents edit the same service or test files concurrently.

## Deliverable

Approved plan, staged diff, test results, recovery classification (if a failure occurred), and a final evidence-based report. Note whether any described workflow stage was manually invoked rather than automated.
