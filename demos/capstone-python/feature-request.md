# Feature request: Customer Account Health Dashboard

## Business objective

Help authorized customer-operations staff find accounts that may need follow-up and understand the source of each dashboard result.

## Existing data available in this starter

The synthetic records include account ID, tenant ID, display name, account status, overdue days, open issue count, and last activity date. Treat the repository and any approved database-context tool as the source of truth; do not infer additional schema fields.

## Functional requirements

1. List accounts visible to the signed-in operator.
2. Support status filtering and bounded pagination.
3. Show summary counts for the same authorized scope and filters.
4. Preserve tenant boundaries for list, summary, and any future export.
5. Include enough source information to explain how a health category was assigned.

## Non-functional and safety constraints

- Use existing authentication and authorization in the host application; the starter has no real identity provider.
- Apply tenant scoping in the trusted service/data layer, not in a Copilot prompt.
- Enforce a maximum page size at the backend.
- Use parameterized database values if persistence is added; never expose arbitrary SQL.
- Do not return credentials or unnecessary personal information.
- Keep synthetic fixture data in tests and demos.

## Acceptance criteria to confirm

- A request for another tenant's account is denied or returns no data according to the existing application contract.
- Invalid filters and page sizes produce documented validation errors.
- Summary counts match the filtered, authorized result set.
- Empty results are represented consistently.
- Existing behavior is preserved and focused tests cover new rules.

## Open questions — do not guess

1. What exact conditions define `healthy`, `attention`, and `critical`?
2. Which account statuses count as overdue, and what timezone defines recent activity?
3. Which support roles may view or export data, and how are permitted tenants derived?
4. Must export match the dashboard filters and pagination, or export the full authorized result set?
5. What are the freshness expectations and source-of-truth tables for summary metrics?

Record answers and their approver in the capstone decision log before implementing the corresponding rules.
