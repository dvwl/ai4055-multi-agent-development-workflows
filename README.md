# AI4055 — Pragmatic SDLC Automation

Course site and companion materials for **Pragmatic SDLC Automation: Implementing Multi-Agent Development Workflows with GitHub Copilot**. This single repository is intended to grow to hold the Jekyll site, exercises, and demo projects for Modules 1–9.

## Course information

- **Course code:** AI4055
- **SBL number:** 10001745100
- **Provider:** Dream Catcher Consulting Sdn Bhd
- **Course duration:** 3 days, 9:00 am–5:00 pm
- **Course page:** [AI4055 course outline](https://www.dreamcatcher.asia/training/4055?scroll=1)
- **Current materials:** Exercises for Modules 1–9, Python demos, and Copilot workspace customizations.
- **Course structure:** Modules 1–9 across Day 1 (declarative workspace context and agent design), Day 2 (hosted tool extensibility), and Day 3 (governance and lifecycle workflows).

[Start Module 1 →](https://dvwl.github.io/ai4055-multi-agent-development-workflows/exercises/module-1/) · [Browse all exercises](https://dvwl.github.io/ai4055-multi-agent-development-workflows/exercises/) · [Course Info](https://www.dreamcatcher.asia/training/4055?scroll=1)

## Start here

New learners should:

1. Review the [AI4055 course outline](https://www.dreamcatcher.asia/training/4055?scroll=1).
2. Begin with [Module 1: Introduction to Copilot Multi-Agent Architecture](https://dvwl.github.io/ai4055-multi-agent-development-workflows/exercises/module-1/). Its labs introduce the Python demo, custom agents, and skills before later modules add more tooling.
3. Install VS Code with GitHub Copilot enabled and Python 3.9 or later. Modules 1–3 and the capstone need no database; Modules 4–6 list their extra requirements in the demo README.
4. Clone this repository and open its root folder in VS Code so workspace agents, instructions, prompts, and skills are available.
5. Before coding, run the Module 1 baseline tests from `demos/module-1-python/`:

   ```console
   python -m unittest discover -s tests -v
   ```

## Table of contents

### Day 1 — Declarative workspace context and agent design

1. [Introduction to Copilot Multi-Agent Architecture](https://dvwl.github.io/ai4055-multi-agent-development-workflows/exercises/module-1/)
2. [Rules and Constraints Engineering](https://dvwl.github.io/ai4055-multi-agent-development-workflows/exercises/module-2/)
3. [Grounding and Prompt Templates](https://dvwl.github.io/ai4055-multi-agent-development-workflows/exercises/module-3/)

### Day 2 — Hosted agent customization and tool extensibility

4. [The Extensibility Architecture of Copilot](https://dvwl.github.io/ai4055-multi-agent-development-workflows/exercises/module-4/)
5. [Bridging the Database Context](https://dvwl.github.io/ai4055-multi-agent-development-workflows/exercises/module-5/)
6. [Hands-On Technical Lab](https://dvwl.github.io/ai4055-multi-agent-development-workflows/exercises/module-6/)

### Day 3 — Lifecycle management, governance, and capstone

7. [Governance, Licensing, and Resource Allocations](https://dvwl.github.io/ai4055-multi-agent-development-workflows/exercises/module-7/)
8. [Multi-File Declarative Workflow Orchestration](https://dvwl.github.io/ai4055-multi-agent-development-workflows/exercises/module-8/)
9. [The Integrated Capstone Project](https://dvwl.github.io/ai4055-multi-agent-development-workflows/exercises/module-9/)

## Contents

- `docs/` — Jekyll course landing page and module exercise pages.
- `demos/` — runnable demos and guided activities organized by module.
- `demos/module-1-python/` — small, dependency-free Python project for Module 1.
- `demos/module-4-6-python/` — shared progressive FastAPI/MySQL/MCP demo (Modules 4–6).
- `demos/capstone-python/` — synthetic multi-file starter for Module 9.
- `.github/agents/` — workspace custom-agent examples for VS Code.
- `.github/skills/` — a workspace Agent Skill example.
- `.github/prompts/` — reusable workflow and planning prompts.

The PowerPoint decks, course profile, and other course-authoring reference files are intentionally outside this repository.

## Use the Python demo

Open the repository root in VS Code so the workspace customizations are available. In the integrated terminal, change to `demos/module-1-python/` and run:

```powershell
python -m unittest discover -s tests -v
```

The Module 1 and capstone starters use Python's standard library; no package installation is required. Modules 4–6 document their own dependencies and local MySQL setup.

## GitHub Pages publishing

This repository's Pages site is configured to publish from branch `main` and folder `/ (root)`. The learner-facing home page is [`index.md`](index.md); `README.md` is the repository guide. Module exercise pages under `docs/exercises/` use explicit permalinks.

To change the source, open repository **Settings → Pages → Build and deployment** and select the branch and folder you want. The project-page URLs and links in this README are currently set for `dvwl/ai4055-multi-agent-development-workflows`.

Theme and deployment references: [Just the Docs](https://just-the-docs.github.io/just-the-docs/), [MCP setup in VS Code](https://code.visualstudio.com/docs/agent-customization/mcp-servers), and the [Copilot MCP configuration reference](https://code.visualstudio.com/docs/agents/reference/mcp-configuration).

## Before using this with learners

- Review the course metadata and all lab instructions for publication.
- Choose and add a repository license if you intend to grant reuse rights. No license is included in this scaffold.

These labs target GitHub Copilot in VS Code. Agent and skill support can differ across Copilot surfaces and versions; verify the setup in the VS Code version used for delivery.
