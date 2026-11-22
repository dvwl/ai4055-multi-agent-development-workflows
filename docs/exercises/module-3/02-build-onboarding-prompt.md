---
layout: default
title: "Lab 2: Build an onboarding prompt"
permalink: /exercises/module-3/build-onboarding-prompt/
parent: "Module 3: Grounding and Prompt Templates"
nav_order: 2
---

# Lab 2: Build an onboarding prompt

**Time:** 45 minutes · **Mode:** guided build, individual test

## Goal

Create a reusable prompt file that produces a repository-grounded checklist for a proposed service without implementing it.

## Task

1. Inspect `.github/prompts/new-service-onboarding.prompt.md` and `demos/module-3-python/service-layout.md`.
2. Create or adapt a `.prompt.md` under `.github/prompts/`. Include purpose, inputs, grounding steps, output format, and an explicit no-edit stop condition.
3. Invoke it with `notification_preferences` and the provided layout.
4. Verify three cited source paths and label each checklist statement as verified, assumed, or unanswered.
5. Re-run with a changed constraint (for example, “must not add a dependency”) and note which outputs changed.

## Review questions

- Can another learner invoke the prompt without repeating its instructions?
- Are optional details clearly distinguished from required inputs?
- Does it instruct the agent to inspect files, not infer architecture from the layout alone?
- Does the output contain implementation order, tests, risks, and open questions?
- Did it stop before editing?

## Deliverable

The prompt file, two generated checklists, a change comparison, and a peer-verified evidence checklist.
