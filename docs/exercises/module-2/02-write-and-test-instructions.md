---
layout: default
title: "Lab 2: Write and test instructions"
permalink: /exercises/module-2/write-test-instructions/
parent: "Module 2: Rules and Constraints Engineering"
nav_order: 2
---

# Lab 2: Write and test instructions

**Time:** 35 minutes · **Mode:** individual, then peer review

## Goal

Write a concise, testable global rule and a path-specific rule, then check their coverage and behavior.

## Task

1. Inspect the Module 1 ticket implementation and tests. Record the existing conventions before writing rules.
2. Draft one repository rule that applies across modules and one Python-specific rule that applies only to `demos/**/*.py`.
3. Put the rules in temporary `.instructions.md` files on a disposable branch, using `applyTo` frontmatter for scoped rules.
4. Check the glob against both a Python source file and a Markdown exercise page. If available, inspect the VS Code customizations UI for diagnostics.
5. Ask Copilot to plan a tiny service change. Compare its plan with the actual repo patterns; avoid broad claims that a rule guarantees behavior.
6. Ask a peer to locate ambiguity, overlap, over-broad scope, stale commands, or a rule impossible to enforce through instructions alone.

## Challenge

Create an intentionally ambiguous rule such as “make the implementation robust.” Ask two learners to interpret it independently, then replace it with observable acceptance criteria.

## Deliverable

Submit the two rules, intended file matches, a short plan response, peer-review feedback, and the revision. Do not leave experimental rules in the shared branch unless the instructor approves them.
