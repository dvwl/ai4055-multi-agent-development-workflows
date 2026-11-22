---
layout: default
title: "Module 2: Rules and Constraints Engineering"
permalink: /exercises/module-2/
parent: Exercises
nav_order: 2
---

# Module 2: Rules and Constraints Engineering

Learn to guide Copilot with repository-wide instructions, path-specific rules, and a task boundary. These files influence agent behavior; they do not replace tests, tool permissions, or human review.

## Prerequisites

- Complete [Module 1](https://dvwl.github.io/ai4055-multi-agent-development-workflows/exercises/module-1/).
- Open the repository root in VS Code.
- Run the Module 1 Python demo tests before changing the workspace instructions.

## Lab pages

1. [Map instruction scope](https://dvwl.github.io/ai4055-multi-agent-development-workflows/exercises/module-2/instruction-scope/)
2. [Write and test instructions](https://dvwl.github.io/ai4055-multi-agent-development-workflows/exercises/module-2/write-test-instructions/)
3. [Constrained multi-file refactor](https://dvwl.github.io/ai4055-multi-agent-development-workflows/exercises/module-2/constrained-refactor/)

## Labs

1. Inspect the current conventions and identify where rules belong.
2. Review `.github/copilot-instructions.md` and scoped Python instruction files.
3. Use the rules to plan a small multi-file refactor of the ticket service.
4. Review whether the rules apply to the intended files, then inspect the diff and run tests.

Do not ask Copilot to “make the rules deterministic.” Instructions reduce unwanted variation but do not enforce permissions or guarantee compliance.

## Exercise

Use the Module 1 ticket demo. Ask Copilot to move the combined ticket-selection behavior into a focused service function while preserving existing filter/sort helpers and their behavior.

Before implementation, require a plan that names the files, acceptance criteria, and tests. Keep the change limited to the Python source and tests. Do not introduce a database, new dependency, or public API.

## Deliverable and success criteria

- Identify one rule that applies repository-wide and one that applies only to a path.
- Confirm each `applyTo` glob matches the intended Python files and not the course Markdown.
- Show a small diff and passing tests.
- Record any vague, conflicting, stale, or impossible rule you found and how you clarified it.

Instructions are guidance, not a deterministic enforcement mechanism. Validate actual changes and test results.

## Independent challenge

Ask a peer to create a deliberately over-broad or conflicting rule, then use a throwaway branch to observe where it applies. Correct its scope and wording. Record one control that must be enforced outside the prompt (for example, required checks or protected-branch review).
