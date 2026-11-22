---
layout: default
title: "Module 9: Integrated Capstone Project"
permalink: /exercises/module-9/
parent: Exercises
nav_order: 9
---

# Module 9: The Integrated Capstone Project

## Capstone lab pages

1. [Analyze requirements](https://dvwl.github.io/ai4055-multi-agent-development-workflows/exercises/module-9/analyze-requirements/)
2. [Ground the workspace and approve a plan](https://dvwl.github.io/ai4055-multi-agent-development-workflows/exercises/module-9/ground-and-plan/)
3. [Implement and verify](https://dvwl.github.io/ai4055-multi-agent-development-workflows/exercises/module-9/implement-and-verify/)
4. [Review and deliver](https://dvwl.github.io/ai4055-multi-agent-development-workflows/exercises/module-9/review-delivery/)

## Scenario

Deliver a **Customer Account Health Dashboard** enhancement for a customer-operations application. Use the Python starter in `demos/capstone-python/` and the approved local database-context tool from Modules 4–6 where available.

The supplied [feature request](https://github.com/dvwl/ai4055-multi-agent-development-workflows/blob/main/demos/capstone-python/feature-request.md) intentionally contains unanswered business questions. Analyze and record them before implementation; do not let Copilot invent policy.

## Capstone stages

Teams should not start implementation while an unresolved requirement changes authorization, tenant scope, or data exposure.

### Independent extension

Use this extension for a second requirement slice, additional regression/security tests, a seeded code-review exercise, or a team presentation. Each learner should individually trace one requirement through its acceptance criterion, implementation files, test evidence, and PR summary.

1. **Analyze requirements:** create a structured feature analysis with users, functional/non-functional requirements, data, APIs, security constraints, acceptance criteria, assumptions, and open questions.
2. **Ground the workspace:** inspect global and scoped instructions, prompt/skill resources, existing code, tests, and interfaces. Attach critical files explicitly.
3. **Retrieve approved context:** use the local database-context MCP tools for schema and explicitly allowed synthetic operational data. Verify returned facts against the local database.
4. **Plan and approve:** propose architecture, affected files, dependency order, tests, risks, and unresolved decisions. Get human approval before implementation.
5. **Implement in stages:** make small multi-file changes in dependency order, with review checkpoints.
6. **Verify:** run focused and full tests, lint/type checks if configured, and inspect access boundaries and the final diff.
7. **Prepare a pull request:** use a feature branch, stage only intended files, and write an evidence-backed PR summary. Creating a PR is not merging it.
8. **Summarize structure:** describe actual changed components and data flows from the final code, not just the original plan.
9. **Review and govern:** conduct a separate code/security review, triage findings, and leave merge approval to an authorized human.

## Team roles

- **Copilot operator:** drives the approved task and records prompts and evidence.
- **Technical lead:** resolves requirements and approves architecture.
- **QA reviewer:** checks acceptance criteria and test evidence.
- **Security reviewer:** checks authorization, tenant scoping, data exposure, and secrets.
- **Release approver:** checks required gates and makes the final human approval decision.

Small groups may rotate roles. One person must not approve their own change solely because Copilot reports success.

## Deliverables

- Feature analysis and decision log.
- Schema/telemetry evidence with source and freshness noted.
- Approved architecture and dependency-aware implementation plan.
- Reviewed code diff and test/check output.
- Pull-request description and structural summary.
- Review findings, remediation status, and human approval decision.

## Assessment (100 points)

| Area | Points |
|---|---:|
| Requirements and traceability | 10 |
| Grounding and instruction compliance | 10 |
| Safe use of approved database context | 10 |
| Architecture and implementation plan | 15 |
| Multi-file implementation quality | 20 |
| Verification evidence | 15 |
| PR and structural summary | 10 |
| Code review and governance | 10 |

### Mandatory safety gates

The capstone is incomplete if secrets are committed, unauthorized or cross-tenant data access is introduced, critical findings remain unresolved, failed/unrun tests are claimed as passing, or required human approval is bypassed.
