---
layout: default
title: "Lab 3: Constrained multi-file refactor"
permalink: /exercises/module-2/constrained-refactor/
parent: "Module 2: Rules and Constraints Engineering"
nav_order: 3
---

# Lab 3: Constrained multi-file refactor

**Time:** 45 minutes · **Mode:** individual implementation, peer review

## Task

Use `demos/module-1-python/`. Ask Copilot to add `find_tickets` to the service with optional status and minimum-priority filters, sorted by descending priority then ascending ID. Preserve existing helpers and input immutability.

1. Run the baseline tests and save the result.
2. Ask for a plan first. Require file paths, acceptance criteria, and edge cases; do not allow edits yet.
3. Compare the plan with the rules from [Lab 2](write-test-instructions/). Approve or revise scope before implementation.
4. Implement the smallest change; add tests for combinations of filters, ordering/ties, empty input, and unchanged input.
5. Review the diff and run the tests yourself.
6. Ask a peer to mark each requirement as evidenced, missing, or not applicable.

## Stop conditions

Stop and ask for clarification if existing tests conflict with requested ordering, if Copilot proposes a new dependency, or if it changes unrelated files or public helpers.

## Success evidence

Passing test output, a focused diff, a checklist mapping each acceptance criterion to a test, and one example of a rule that helped—or failed to help—constrain the change.
