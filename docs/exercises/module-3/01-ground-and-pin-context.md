---
layout: default
title: "Lab 1: Ground and pin context"
permalink: /exercises/module-3/ground-and-pin-context/
parent: "Module 3: Grounding and Prompt Templates"
nav_order: 1
---

# Lab 1: Ground and pin context

**Time:** 30 minutes · **Mode:** guided, then individual

## Goal

Use workspace discovery to find evidence, then inspect and attach the files that should stay in scope.

## Task

Use the Module 1 ticket service or the Module 4–6 Python API.

1. Ask `#codebase` or workspace search to locate the service entry point, its tests, and the documented test command. Ask for paths and short evidence, not a repository-wide summary.
2. Open the files and verify the claims. Record one candidate file that search missed or returned as a false positive.
3. Attach the source, tests, and relevant instructions using the context picker or file-reference controls available in your VS Code version.
4. Ask for a plan to add a narrowly scoped behavior. Require the agent to separate facts, assumptions, and unknowns.
5. Do not edit files. Ask a peer to verify two cited paths and the acceptance criteria.

## Independent variation

Repeat with another demo directory or choose different test files. Compare how the evidence set changes and which files you pinned deliberately.

## Deliverable

An evidence map (claim → path → verification), the pinned context list, and one context gap you would resolve before implementation.

`#codebase` is a discovery aid; it does not mean every repository file was loaded into the model context.
