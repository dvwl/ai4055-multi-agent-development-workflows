---
name: python-test-workflow
description: Find and run the relevant standard-library unittest tests for a Python change, then report the exact command and result. Use when validating Python code in this repository.
---

# Validate Python changes

1. Identify the changed Python files and the tests that cover their behavior.
2. Check the demo README for the correct working directory and test command.
3. Run the relevant tests. For the complete Module 1 demo suite, use:

   ```console
   python -m unittest discover -s tests -v
   ```

   Run this command from `demos/module-1-python/`.
4. Report the exact command, working directory, and observed pass/fail result.
5. If tests fail, summarize the relevant failure and stop. Do not describe a failed or unrun test as passing.
