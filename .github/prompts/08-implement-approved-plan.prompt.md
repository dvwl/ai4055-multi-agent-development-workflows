---
name: Implement an approved plan
description: Implement only the human-approved plan in dependency order and test each stage.
---

# Task

Implement the approved plan supplied by the operator. If no approved plan is attached or scope has changed, stop and request it.

## Workflow

1. Re-check the relevant source, tests, and repository instructions.
2. Confirm the approved files and acceptance criteria.
3. Implement contracts before dependent implementations.
4. Add or update focused tests; avoid unrelated edits and dependencies.
5. Run the relevant documented tests and report the exact command and result.
6. Stop if requirements conflict or the change needs an unapproved architecture/security decision.
