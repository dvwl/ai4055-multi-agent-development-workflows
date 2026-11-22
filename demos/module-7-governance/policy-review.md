# Governance review scenarios

Use these as discussion prompts. For each one, identify the control owner, scope, evidence, and what the control does **not** guarantee.

## Scenario A — Public-code match

An organization enables a public-code matching policy. A developer assumes this means every generated line is original and every copied pattern is blocked.

**Discuss:** What does the configured matching policy actually do in the selected Copilot product and plan? What should the developer verify? Why is a matching filter not a general copyright clearance process?

## Scenario B — Content exclusion

A repository administrator excludes a sensitive path. A prompt also says, “Never read files in the payroll directory.”

**Discuss:** Which control is the actual access/context exclusion? Can an instruction replace a product-supported exclusion or repository permission? How will the team test the configuration?

## Scenario C — Agent instructions

A custom agent says “do not modify production configuration,” but has broad edit and terminal tools.

**Discuss:** Why is prose not an authorization boundary? What tool scope, branch policy, review, or approval gate should be applied?

## Scenario D — Resource allocation

A team wants to reserve the strongest reasoning model for complex architecture and debugging tasks.

**Discuss:** How will they choose based on task risk and current plan policy? What usage evidence is available? What fallback exists when an entitlement or quota is unavailable?

## Scenario E — Pre-commit check

A developer's local test hook passes, but the CI workflow is disabled on the target branch.

**Discuss:** Why do local hooks not replace required server-side checks and protected-branch policy? Who verifies those settings?
