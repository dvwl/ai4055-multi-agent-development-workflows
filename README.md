# AI4055 — Pragmatic SDLC Automation

Course site and companion materials for **Pragmatic SDLC Automation: Implementing Multi-Agent Development Workflows with GitHub Copilot**. This single repository is intended to grow to hold the Jekyll site, exercises, and demo projects for Modules 1–9.

## Course information

- **Course code:** AI4055
- **SBL number:** 10001745100
- **Provider:** Dream Catcher Consulting Sdn Bhd
- **Course duration:** 3 days, 9:00 am–5:00 pm
- **Course page:** https://www.dreamcatcher.asia/training/4055?scroll=1
- **Current materials:** Exercises for Modules 1–9, Python demos, and Copilot workspace customizations.
- **Course structure:** Modules 1–9 across Day 1 (declarative workspace context and agent design), Day 2 (hosted tool extensibility), and Day 3 (governance and lifecycle workflows).

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

## Enable GitHub Pages

1. In repository **Settings → Pages → Build and deployment**, select **GitHub Actions** as the source.
2. Run **Deploy Jekyll site to GitHub Pages** from the Actions tab (or push a later commit) to start the first deployment.
3. The workflow in `.github/workflows/pages.yml` builds the Jekyll source in `docs/` with the Just the Docs theme and deploys it.

The current Jekyll configuration is prepared for `dvwl/ai4055-multi-agent-development-workflows` and uses the pinned Just the Docs theme release in the root `Gemfile`.

Theme and deployment references: [Just the Docs](https://just-the-docs.github.io/just-the-docs/), [MCP setup in VS Code](https://code.visualstudio.com/docs/agent-customization/mcp-servers), and the [Copilot MCP configuration reference](https://code.visualstudio.com/docs/agents/reference/mcp-configuration).

## Before using this with learners

- Review the course metadata and all lab instructions for publication.
- Choose and add a repository license if you intend to grant reuse rights. No license is included in this scaffold.

These labs target GitHub Copilot in VS Code. Agent and skill support can differ across Copilot surfaces and versions; verify the setup in the VS Code version used for delivery.
