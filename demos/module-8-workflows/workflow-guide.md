# Customer-service refactor workflow

This is a human-readable workflow specification for the Module 8 lab. It is not an executable Copilot workflow format.

## Goal

Add a `find_tickets` service operation to the Module 1 Python demo. It supports optional status and minimum-priority filters, returns tickets in descending priority and ascending ticket-ID order, and preserves caller-owned input.

## Sequential stages and gates

| Stage | Inputs | Output | Gate |
|---|---|---|---|
| Analyze | Request, source, tests, instructions | Evidence-backed file/dependency map | Operator checks cited files |
| Plan | Analysis | Acceptance criteria, edge cases, test plan | Human approves scope and files |
| Implement contract | Approved plan | Function signature and behavior | Review interface before dependents |
| Implement behavior | Approved contract | Service implementation and focused tests | Run focused tests |
| Verify | Complete diff | Full test result and risk notes | Human reviews diff and evidence |
| Report | Verified change | Summary of changes and limits | Do not claim unrun checks passed |

## Dependency map

```text
Request + repository instructions
              |
              v
      Inspect source/tests
              |
              v
   Approve acceptance contract
              |
       +------+------+
       v             v
  Service change   Test plan
       \             /
        v           v
       Focused verification
              |
              v
        Full diff review
```

## Parallel work

Independent research (for example, a second reviewer locating existing callers) can be performed separately. Do not ask two agents to edit the same service or test files concurrently. Integrate evidence before approving a design.

## Conditional branch

If existing tests define a conflicting public contract, stop and ask the human to resolve the contract before implementation. If no conflict exists, proceed with the approved plan. Do not silently choose one behavior.
