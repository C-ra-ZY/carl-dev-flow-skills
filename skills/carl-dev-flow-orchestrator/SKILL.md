---
name: carl-dev-flow-orchestrator
description: Orchestrate the full multi-stage delivery workflow shared by Sisyphus, Hephaestus, and the user, while routing stage-specific work to narrower skills.
version: 1.0.0
compatibility: opencode
license: CC-BY-4.0
metadata:
  audience: individual-developer
  domain: workflow
---

## Purpose

Use this as the top-level workflow contract for the entire collaboration model.

This skill is the canonical source of truth for:

- the overall stage sequence
- role boundaries
- document lifecycle rules
- handoff and promotion rules between stages

This skill is not the canonical place for stage-specific step-by-step detail. That detail belongs in the narrower subskills.

For maintenance helpers and Chinese invocation examples, see the companion resources in this workflow family.

## Workflow family

The workflow has four stages:

1. `requirements-development`
2. `technical-confirmation`
3. `development-execution`
4. `recursive-improvement`

## Ownership model

Use these skills as the authoritative source for each scope:

- `carl-dev-flow-orchestrator`: overall lifecycle, role contract, transition rules
- `carl-dev-flow-stage-router`: stage detection and next-step routing
- `carl-dev-flow-requirements`: authoritative details for requirements-development
- `carl-dev-flow-tech-spec`: authoritative details for technical-confirmation
- `carl-dev-flow-implementation`: authoritative details for development-execution
- `carl-dev-flow-review-loop`: authoritative details for recursive-improvement

If a rule is stage-specific, update the relevant subskill first.
If a rule changes the lifecycle, role contract, or promotion logic across the whole workflow family, update this skill.

## Role contract

### Sisyphus

- orchestration lead
- planner and task decomposer
- master agent for sub-agent delegation
- owner of integration, sequencing, and repair coordination

### Hephaestus

- independent reviewer and technical challenger
- second-pass critic for requirements, specs, and code
- primary partner in recursive review loops

### User

- product and decision authority
- participant in all major discussions
- final consensus partner for requirements, spec, and review outcomes

## Document lifecycle rules

Requirements and technical design must follow:

- `draft -> revised -> final`

Recursive improvement must follow:

- `review memo draft -> agreed review memo -> delegated fixes -> re-review`

Do not treat verbal agreement as sufficient. The artifact must be updated.

## Transition rules

- Do not move into coding-heavy execution until requirements and technical direction are aligned, unless the user explicitly chooses a shortcut.
- Do not close review after a single repair pass unless all three parties agree the code is deliverable.
- When disagreement appears, write it down as an explicit open issue and resolve it in the artifact.
- If `Sisyphus` and `Hephaestus` disagree on direction, present the disagreement clearly and let the user make the final decision.

## Routing rules

- For early product shaping, load `carl-dev-flow-requirements`.
- For architecture and implementation design, load `carl-dev-flow-tech-spec`.
- For active coding coordination, load `carl-dev-flow-implementation`.
- For review and fix loops, load `carl-dev-flow-review-loop`.

## Maintenance rule

To minimize drift inside this skill family:

- keep this skill short and structural
- keep detailed stage procedures only in subskills
- avoid restating the same numbered process in both the master skill and a subskill
- when adding a new stage, update the stage list here and then create or update its dedicated subskill

## Companion resources

- `scripts/check-workflow-skills.py`: drift checker for this workflow skill family
- `../carl-dev-flow-stage-router/templates/zh_CN_INVOCATION.md`: Chinese invocation templates for common workflow entry points
- `templates/minimal-zh.md`: minimal Chinese prompt for using this orchestrator directly

## Default behavior when loaded

1. Identify the current stage.
2. Restate the artifact expected at that stage.
3. Load or follow the correct stage-specific skill when appropriate.
4. Drive the workflow forward instead of stopping at description.
