---
name: Verify a multi-file change
description: Review a completed diff, identify verification gaps, and report evidence without editing files.
---

# Task

Review the supplied change against its approved plan and acceptance criteria.

## Check

- Scope and dependency consistency across all changed files.
- Public contract and existing behavior preservation.
- Relevant edge-case tests and actual test output.
- Security or data-boundary implications.
- Unresolved assumptions and checks not run.

Do not edit files or claim tests passed unless you observed successful output. Report actionable findings with file and line references, followed by a concise evidence-based summary.
