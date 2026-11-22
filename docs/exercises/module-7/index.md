---
layout: default
title: "Module 7: Governance, Licensing, and Resource Allocations"
permalink: /exercises/module-7/
parent: Exercises
nav_order: 7
---

# Module 7: Governance, Licensing, and Resource Allocations

## Lab pages

1. [Policy and code provenance](https://dvwl.github.io/ai4055-multi-agent-development-workflows/exercises/module-7/policy-provenance/)
2. [Plan model and resource use](https://dvwl.github.io/ai4055-multi-agent-development-workflows/exercises/module-7/resource-planning/)
3. [Add quality gates](https://dvwl.github.io/ai4055-multi-agent-development-workflows/exercises/module-7/quality-gates/)

Design controls around Copilot-assisted work: policy, code provenance, resource planning, verification, and human approvals.

## Lab 1: Review the governance boundary

Use the scenarios in `demos/module-7-governance/policy-review.md` to classify each control as a product policy, repository instruction, access control, verification gate, or human approval. Identify which controls can actually prevent an action and which only guide model behavior.

Discuss the distinction between public-code matching controls, content exclusions, and repository instructions. Check current product and organization settings for the delivery environment; do not assume one setting blocks all copyrighted or sensitive content.

## Lab 2: Build a resource plan

Complete `demos/module-7-governance/usage-plan.csv` with representative tasks, the minimum suitable model/workflow, expected verification, and escalation criteria. Use current account policy and observed usage data if available. Treat any estimates as local planning assumptions, not guaranteed prices, quotas, or entitlements.

Compare a routine task, a cross-file change, and a high-impact security/data task. Explain when to stop or escalate instead of simply selecting a more capable model.

## Lab 3: Add local and CI quality gates

1. Inspect `demos/module-7-governance/pre-commit-config.yaml` and identify each hook's purpose and limits.
2. In a disposable branch, install `pre-commit` only if the facilitator approves the environment change: `python -m pip install pre-commit`.
3. Run `pre-commit run --all-files` and the Python tests; introduce a harmless whitespace issue in a disposable file to observe feedback.
4. Explain why a local hook is a convenience gate, not an authorization boundary; required CI and branch protections must be configured on the hosting platform.

## Deliverable

Submit a one-page control map, a filled usage plan, and evidence of one successful local check plus one intentionally detected issue.

## Safety criteria

- No secrets or customer records in prompts, commits, or demo output.
- No claim that model instructions guarantee deterministic behavior.
- No invented current Copilot plan limits, AI credit prices, or license entitlements.
- Human review remains required for sensitive or high-impact changes.

## Independent exercise

Draft a lightweight governance checklist for a team onboarding Copilot. Include who owns policy settings, how excluded content is tested, which checks run locally and in CI, how reviewers handle generated code provenance concerns, and how current plan/usage policy is checked. Do not copy account-specific or non-public policy settings into this public course repo.
