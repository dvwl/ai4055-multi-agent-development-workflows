---
name: New Service Onboarding
description: Analyze repository patterns and produce a grounded implementation checklist for a new Python service. Do not edit files.
---

# Task

Prepare an implementation checklist for a proposed Python service.

## Inputs

- Service name: ${input:serviceName}
- Structural layout file: ${input:layoutFile}
- Additional constraints: ${input:constraints}

## Instructions

1. Read applicable repository instructions.
2. Use workspace search, including `#codebase` where available, to discover comparable services.
3. Open and inspect the relevant implementations, interfaces, configuration, and tests. Do not assume search attached every file to context.
4. Cite repository paths for findings. Separate verified facts from assumptions.
5. Identify dependencies, contracts, tests, risks, and open questions.
6. If the layout or repository sources conflict, describe the conflict and ask for a decision.

## Output

Return an ordered checklist with proposed files, purpose, acceptance criteria, tests, risks, and unresolved questions.

Do not edit files, create code, or run commands. Stop after presenting the checklist for human review.
