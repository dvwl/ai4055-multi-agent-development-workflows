---
layout: default
title: "Module 3: Grounding and Prompt Templates"
permalink: /exercises/module-3/
parent: Exercises
nav_order: 3
---

# Module 3: Grounding and Prompt Templates

Practice finding relevant repository evidence, explicitly attaching authoritative files, and creating a reusable prompt file that produces a plan—not an unapproved implementation.

## Prerequisites

- Complete Modules 1–2.
- Open this repository in VS Code with the Copilot harness.
- Review the sample [service layout](https://github.com/dvwl/ai4055-multi-agent-development-workflows/blob/main/demos/module-3-python/service-layout.md).

## Lab pages

1. [Ground and pin context](https://dvwl.github.io/ai4055-multi-agent-development-workflows/exercises/module-3/ground-and-pin-context/)
2. [Build an onboarding prompt](https://dvwl.github.io/ai4055-multi-agent-development-workflows/exercises/module-3/build-onboarding-prompt/)
3. [Manage context and split work](https://dvwl.github.io/ai4055-multi-agent-development-workflows/exercises/module-3/manage-context/)

## Lab: Automated service onboarding

1. Use workspace search or `#codebase` to locate comparable Python components. Treat this as discovery, not proof that the whole repository is in model context.
2. Open and inspect the candidate files; attach known authoritative references using the context controls available in your VS Code version.
3. Open `.github/prompts/new-service-onboarding.prompt.md` and review its inputs, grounding steps, output, and stop condition.
4. Invoke the prompt with a service name and the demo layout file.
5. Check file-path evidence, distinguish facts from assumptions, and ask the agent to surface conflicts or unanswered questions.

### Independent practice

Adapt the prompt to a second service name and a changed constraint. Compare the checklist, verify at least three cited files, and record which prompt instructions changed the output. Keep the agent in planning mode; do not implement the proposed service.

## Deliverable and success criteria

- A reusable `.prompt.md` file under `.github/prompts/`.
- An implementation checklist tied to actual repository evidence.
- Explicit assumptions/open questions and no edits made by the planning exercise.

Context controls, prompt variables, and prompt-file support vary by Copilot surface and version. Verify the syntax and behavior in the editor used for the course; do not state a universal token limit.

## Peer-review questions

- Is each repository-specific claim linked to a file the reviewer can inspect?
- Does the checklist include contracts, dependencies, tests, risks, and unanswered questions?
- Did the prompt separate verified facts from assumptions?
- Did the agent stop before editing?
