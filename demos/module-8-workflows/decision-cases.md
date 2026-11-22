# Conditional workflow decision cases

For each case, write the observable condition, the path taken, and the approval gate. These are planning exercises; they do not execute a workflow.

1. **Contract conflict:** an existing test expects stable input order, while the new request asks for priority ordering. Stop for a product decision or define the new operation separately; do not silently change the existing helper.
2. **Independent review:** documentation and test discovery can be researched in parallel if neither task edits shared files. Combine and verify their findings before implementation.
3. **Failing verification:** if a test fails, classify it as regression, pre-existing failure, or environment failure. Fix only a root cause within the approved scope; otherwise stop and report evidence.
4. **Architecture alternative:** compare a minimal in-memory service change with a new persistence layer. Implement only the selected option; adding infrastructure requires explicit approval.
