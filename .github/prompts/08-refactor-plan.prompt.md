---
name: Plan a bounded refactor
description: Inspect repository evidence and propose a dependency-aware plan without editing files.
---

# Task

Plan the requested refactor using the repository source and tests.

## Rules

1. Read applicable repository instructions and inspect the relevant source, tests, and callers.
2. Cite file paths for repository-specific findings; distinguish facts from assumptions.
3. Return acceptance criteria, affected files, dependencies, focused tests, risks, and open questions.
4. Preserve existing public behavior unless the request explicitly approves a change.
5. Do not edit files or run commands. Stop for human approval.
