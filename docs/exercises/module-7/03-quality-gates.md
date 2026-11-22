---
layout: default
title: "Lab 3: Add quality gates"
permalink: /exercises/module-7/quality-gates/
parent: "Module 7: Governance, Licensing, and Resource Allocations"
nav_order: 3
---

# Lab 3: Add quality gates

**Time:** 35 minutes · **Mode:** guided demonstration and individual verification

## Safety note

Use a disposable branch or copy. The sample hooks download third-party code when installed. Review the repository, pinned revision, and hook behavior before installation. Do not install or run hooks on a production workstation without approval.

## Steps

1. Inspect `demos/module-7-governance/pre-commit-config.yaml`. For each hook, name the defect it catches and what it cannot prove.
2. If approved, install `pre-commit` and copy the sample configuration to a disposable repository root.
3. Run `pre-commit run --all-files` and the Module 1 tests. Record actual results.
4. Introduce trailing whitespace in a temporary file, run the hook again, and record what it detects/fixes. Revert only your temporary test file change.
5. Explain why the local hook can be skipped and why a required CI check / protected branch is needed for team enforcement.
6. Sketch which checks should be required in CI and which require human review (for example, authorization logic).

## Deliverable

Hook-to-risk matrix, captured successful and intentionally detected run, and CI/branch-protection recommendation. Do not claim a local pass proves application correctness or security.
