---
name: carl-dev-flow-stage-router
description: Quickly identify the current stage of the Sisyphus and Hephaestus collaboration workflow and drive the next artifact or decision.
version: 1.4.0
compatibility: opencode
license: CC-BY-4.0
metadata:
  audience: individual-developer
  domain: routing
---

## Purpose

Use this skill as the fast entry point into the broader Sisyphus and Hephaestus workflow.
Use it for "start the workflow", "continue from here", or "which stage are we in" moments.

For Chinese invocation examples, see `templates/zh_CN_INVOCATION.md` and `templates/minimal-zh.md`.

## Default behavior when loaded

1. Identify the current stage.
2. Name the expected artifact for that stage.
3. State which role should lead next.
4. Drive the transition forward instead of stopping at summary.
5. When routing to a new stage, use interactive questions to confirm the transition with the user in the same response rather than ending the conversation.

## Stage classifier

Map the current work into exactly one primary stage:

- `requirements-development`
- `technical-confirmation`
- `development-execution`
- `recursive-improvement`

If no workflow artifacts exist yet, default to `requirements-development`.
If the user already has a stable requirements final and technical spec final, default to `development-execution`.
If the user is discussing review findings, fixes, or delivery quality, default to `recursive-improvement`.
If the user is reporting a bug, regression, or unexpected behavior, load `carl-dev-flow-bugfix` for severity grading and fix-path selection.

## Required output pattern

When this skill is loaded, produce a short workflow handoff block with:

- current stage
- lead role now (`Sisyphus`, `Hephaestus`, or user-led with agent support)
- current artifact
- next artifact
- immediate next action

## Routing rules

- For requirements work, use `carl-dev-flow-requirements`.
- For technical design work, use `carl-dev-flow-tech-spec`.
- For active coding coordination, use `carl-dev-flow-implementation`.
- For repeated review and fix cycles, use `carl-dev-flow-review-loop`.
- For the complete end-to-end process, use `carl-dev-flow-orchestrator`.
- For bug-fix workflows (bugs, regressions, unexpected behavior), use `carl-dev-flow-bugfix`.

## Guardrails

- Do not leave the user with only a stage label; move the workflow forward.
- Do not skip artifact naming.
- Do not merge requirement questions into implementation planning unless the user explicitly chooses a shortcut.
- When routing into `recursive-improvement`, keep `Hephaestus` as the reviewer of record.
