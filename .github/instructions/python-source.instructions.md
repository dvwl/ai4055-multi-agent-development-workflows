---
name: Python source conventions
description: Rules for Python source files in course demo projects.
applyTo: "demos/**/*.py"
---

- Use clear, focused functions and type hints for public functions.
- Keep I/O at boundaries; keep business rules easy to test without external services.
- Validate external input at the boundary and return explicit errors using the existing project pattern.
- Do not mutate caller-owned collections unless the function contract requires it.
- Do not add a dependency without explaining why it is needed.
