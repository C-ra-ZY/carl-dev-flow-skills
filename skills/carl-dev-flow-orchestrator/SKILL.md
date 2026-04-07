---
name: carl-dev-flow-orchestrator
description: Orchestrate the full multi-stage delivery workflow shared by Hephaestus, Oracle, Sisyphus, and the user, while routing stage-specific work to narrower skills
version: 2.1.0
compatibility: opencode
license: CC-BY-4.0
metadata:
  audience: individual-developer
  domain: workflow
---

## Purpose

Use this as the top-level contract for the workflow family.
It defines stage order, role boundaries, lane ownership, document lifecycle rules, and promotion logic.
Keep stage-specific procedures in the narrower subskills.

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
- `carl-dev-flow-bugfix`: bug-fix workflow orchestration, severity grading, and fix-path routing

If a rule is stage-specific, update the relevant subskill first.
If a rule changes the lifecycle, role contract, or promotion logic across the whole workflow family, update this skill.

## Role contract

### Hephaestus

- orchestration lead
- planner and task decomposer
- master agent for sub-agent delegation
- owner of sequencing, synthesis, integration, and stage transitions
- lead partner for turning review findings and execution results into the next workflow decision

### Oracle

- independent reviewer and technical challenger
- reviewer of record for requirements, technical design, integrated code, and bug-fix verification
- primary partner in recursive review loops
- review conclusions stay with `Oracle`, even when specialist advice is consulted
- `Hephaestus` must never delegate review work away from `Oracle`; specialist or consultation agents may advise, but they do not replace `Oracle` as reviewer of record

### Sisyphus

- technical striker and implementation specialist
- owner of hard coding, difficult debugging, refactors, and fix execution
- contributor of implementation-feasibility input during requirements and technical design when delivery risk is material
- does not own final review judgment or stage-transition authority

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
`delegated fixes` refers to implementation work, not delegation of review ownership.
Review ownership stays with `Oracle` throughout recursive improvement; `Hephaestus` must never delegate review work away from `Oracle` or treat advisory agents as review substitutes.

## Transition rules

- Do not move into coding-heavy execution until requirements and technical direction are aligned, unless the user explicitly chooses a shortcut.
- Do not close review after a single repair pass unless all three parties agree the code is deliverable.
- When disagreement appears, write it down as an explicit open issue and resolve it in the artifact.
- If `Hephaestus` and `Oracle` disagree on direction, present the disagreement clearly and let the user make the final decision.
- When a stage reaches its exit conditions and the next primary stage is unambiguous, automatically enter that stage in the same response.
- Pause at a stage boundary only when a fresh user decision, explicit arbitration, or shortcut choice is still required.

### Session continuity

When a primary workflow stage completes and the next primary stage is clear, `Hephaestus` should automatically enter that stage in the same response and start the first concrete next-step action.

Use the `ask question` interaction only when a stage boundary or workflow completion still requires user input, explicit arbitration, or a follow-up choice. When used, ask inside the same response to keep the current conversation alive rather than ending the turn.

These session-continuity rules apply to stage transitions and workflow completion only. They do not override intra-stage autonomous progression defined by the narrower stage skills.

At checkpoints that stay within the current stage (for example, promoting an artifact from draft to revised, or from revised to final), `Hephaestus` should proceed automatically when the promotion conditions are clearly met and the user has already expressed agreement. Use interactive questions inside a stage only when unresolved product, scope, or risk decisions still require user input.

## Routing rules

- For early product shaping, load `carl-dev-flow-requirements`.
- For architecture and implementation design, load `carl-dev-flow-tech-spec`.
- For active coding coordination, load `carl-dev-flow-implementation`.
- For review and fix loops, load `carl-dev-flow-review-loop`.
- For bug-fix workflows, load `carl-dev-flow-bugfix`.
- Keep the orchestration lane with `Hephaestus`, the review lane with `Oracle`, and the hard-execution lane with `Sisyphus`.

## Artifact location convention

Workflow artifacts are stored in the `.carl/` directory at the project root:

- `.carl/state.md` — workflow state tracker
- `.carl/requirements/` — requirements stage artifacts
- `.carl/tech-spec/` — technical-confirmation artifacts, including architecture decision records
- `.carl/implementation/` — task plans and delegation records
- `.carl/review/` — review memos per iteration
- `.carl/bugfix/` — bug-fix triage and path selection records

Each stage skill specifies its own file names within the relevant subdirectory.
Projects may override the default path by documenting the override in `.carl/state.md`.

## State convention

The workflow tracks its current position in `.carl/state.md` with these fields:

- `stage`: one of `requirements-development`, `technical-confirmation`, `development-execution`, `recursive-improvement`
- `artifact-status`: `draft`, `revised`, or `final`
- `last-updated-by`: `Hephaestus`, `Oracle`, `Sisyphus`, or `User`
- `open-blockers`: list of unresolved items, or `none`

The state file is descriptive, not prescriptive. Routing logic stays in `carl-dev-flow-stage-router`.

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
3. Name which lane should lead next (`Hephaestus`, `Oracle`, or `Sisyphus`) and load the matching subskill when needed.
4. Drive the workflow forward instead of stopping at description, automatically entering the next stage when the path is clear.
