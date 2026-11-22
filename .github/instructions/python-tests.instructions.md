---
name: Python test conventions
description: Rules for tests in course demo projects.
applyTo: "demos/**/tests/**/*.py"
---

- Prefer focused tests for observable behavior and important edge cases.
- Use synthetic fixtures; do not use real credentials or personal data.
- Keep tests deterministic and independent of network access unless the task explicitly calls for an integration test.
- For database-backed tests, use a disposable local test schema and document the setup separately.
- Never report a test as passing unless its command completed successfully.
