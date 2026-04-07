---
name: carl-dev-flow-bugfix
description: Coordinate bug-fix workflows by grading severity, selecting the appropriate fix path, and routing to existing stage skills with bug-fix context
version: 2.1.0
compatibility: opencode
license: CC-BY-4.0
metadata:
  audience: individual-developer
  domain: bugfix
---

## Purpose

Use this skill when the starting point is a defect, regression, or unexpected behavior rather than a new feature request.
This skill owns severity grading, path selection, and stage sequencing. It does not replace the stage skills; each one keeps its own `Bug-fix adaptation` section.

For the shortest Chinese invocation form, see `templates/minimal-zh.md`.

## Bug severity grading

Classify every incoming bug before choosing a path:

- **lightweight**: root cause is obvious or strongly suspected, change scope is small (single module, few files), no cross-system risk
- **complex**: root cause is unclear, multiple modules or services may be involved, blast radius is uncertain, or the bug is a regression of a previous fix

When severity is ambiguous, default to complex.

## Fix paths

### Lightweight path

1. Write a brief reproduction note (inline, no formal artifact needed).
2. Proceed directly to `development-execution` with bug-fix context.
3. Enter `recursive-improvement` for regression verification with `Oracle` as reviewer of record.
4. Record the shortcut in `.carl/state.md`.

### Complex path

1. **Bug report** — use `carl-dev-flow-requirements` in bug-fix mode: capture reproduction steps, expected vs actual behavior, and acceptance criteria for the fix.
2. **Root cause analysis** — use `carl-dev-flow-tech-spec` in bug-fix mode: identify root cause, assess blast radius, and define a minimal fix strategy.
3. **Fix implementation** — use `carl-dev-flow-implementation` in bug-fix mode: apply the minimal fix through `Sisyphus` or another execution agent, avoid unrelated refactoring, and establish a regression baseline.
4. **Fix verification** — use `carl-dev-flow-review-loop` in bug-fix mode: verify the fix resolves the reported behavior, confirm no regressions, check blast radius assumptions, and keep `Oracle` as reviewer of record.

## Routing rules

- For bug report and reproduction, load `carl-dev-flow-requirements`.
- For root cause analysis and blast radius, load `carl-dev-flow-tech-spec`.
- For minimal fix implementation, load `carl-dev-flow-implementation`.
- For regression verification and fix review, load `carl-dev-flow-review-loop`.

Each of these skills has a `Bug-fix adaptation` section that describes how its standard procedure adjusts for bug-fix work.

## Bug-fix principles

- Fix the bug, not the neighborhood. Do not refactor while fixing.
- Reproduce before fixing. A fix without a reproduction is a guess.
- Establish a regression baseline before applying the fix.
- Assess blast radius before committing to a fix strategy.
- If the fix introduces new risk, escalate severity from lightweight to complex.
- Review ownership stays with `Oracle`; `Hephaestus` selects the path and `Sisyphus` executes the fix. Outside advice is supplemental.

## Artifact location

Store bug-fix orchestration artifacts under `.carl/bugfix/`, including `triage.md`.
Stage-specific artifacts remain in their standard locations (`.carl/requirements/`, `.carl/tech-spec/`, and so on).

## Exit criteria

Do not declare a bug-fix complete until:

- the reported behavior is verified as resolved
- regression verification has passed
- no new issues were introduced by the fix
- `Hephaestus`, `Oracle`, and the user agree the fix is deliverable

## Default behavior when loaded

1. Confirm that the trigger is a bug, regression, or unexpected behavior.
2. Grade the severity as lightweight or complex.
3. Select the appropriate fix path.
4. Drive the first step of that path forward.
5. At each path transition that changes the primary workflow stage or severity handling path (for example, moving from bug report to root cause analysis, or from fix implementation to fix verification), automatically enter the next stage when the path is clear and no new user decision is required. For internal steps that stay within the current stage, continue automatically. Use the `ask question` interaction only when the transition involves a severity change, ambiguous path selection, or workflow-closeout input.
