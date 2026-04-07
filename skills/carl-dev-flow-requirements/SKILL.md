---
name: carl-dev-flow-requirements
description: Run the requirements-development stage where Hephaestus leads discovery, Oracle reviews, and the user converges on a final requirements document
version: 2.1.0
compatibility: opencode
license: CC-BY-4.0
metadata:
  audience: individual-developer
  domain: requirements
---

## Purpose

Use this skill when business intent, behavior boundaries, edge cases, or acceptance expectations are still being shaped.
This skill is the authoritative source for the detailed procedure of the `requirements-development` stage inside the Hephaestus-led workflow family.

For the shortest Chinese invocation form, see `templates/minimal-zh.md`.

## Required lifecycle

The requirements artifact must evolve through:

- `requirements draft`
- `requirements revised draft`
- `requirements final`

## Workflow

1. `Hephaestus` leads discovery with the user and writes the initial draft.
2. `Oracle` reviews the draft without being the original author.
3. The reviewer normalizes structure, checks logic flow, and hunts for missing edge cases.
4. If delivery complexity is material, `Sisyphus` contributes implementation-feasibility input before promotion.
5. `Hephaestus` revises the document in writing and synthesizes open issues.
6. The user, `Hephaestus`, and `Oracle` align on the revised draft, consulting `Sisyphus` when implementation constraints matter.
7. Produce the final requirements document only after open issues are resolved or explicitly deferred.

The reviewer of record is `Oracle` (the review lane owner), not an outside reviewer.

## What the reviewer must check

- missing actors or scenarios
- ambiguous triggering conditions
- inconsistent terminology
- stateful interaction behavior when conversations, edits, or branching flows exist
- side effects, suppression rules, or failure semantics when external actions or notifications exist
- explicit non-goals
- testable acceptance conditions

## Output contract

Always state:

- who authored the current draft
- who is reviewing it
- whether `Sisyphus` implementation-feasibility input was consulted
- unresolved questions
- what changed since the last draft
- what conditions are needed to promote to final

## Promotion rule

Do not call the document final until:

- major terms are defined
- edge cases are either resolved or explicitly deferred
- the user confirms the behavior matches intent
- `Oracle` has had a review opportunity and `Hephaestus` has synthesized the resulting open issues
- any material implementation-feasibility blocker raised by `Sisyphus` is resolved or explicitly deferred
- any external advice is treated as advisory only, not as a substitute for `Oracle` review

When promoting the artifact within this stage (draft to revised, or revised to final), proceed automatically when the promotion conditions are clearly met and the user has already expressed agreement. Use the `ask question` interaction only when unresolved product or scope decisions still require user input.

## Artifact location

Store `draft.md`, `revised.md`, and `final.md` under `.carl/requirements/`.

## Requirements format guidance

For testable requirements, consider EARS (Easy Approach to Requirements Syntax):

- Ubiquitous: "The `<system>` shall `<response>`."
- Event-driven: "When `<trigger>`, the `<system>` shall `<response>`."
- State-driven: "While `<state>`, the `<system>` shall `<response>`."
- Unwanted: "If `<condition>`, then the `<system>` shall `<response>`."

Each EARS requirement maps directly to one acceptance criterion.
This format is recommended but not mandatory.

## Pre-draft interrogation

Before writing any requirements draft, run a structured interrogation to surface unknowns.

### Question categories

Separate questions into three pools:

- **user-answerable**: questions only the user can answer (intent, priority, constraints)
- **codebase-answerable**: questions the agent can resolve by reading the repository (existing APIs, conventions, data models)
- **deferred**: questions that can be safely postponed without blocking the draft

### Interrogation procedure

1. Read the user's initial description and the relevant codebase context.
2. Organize unknowns into the three question pools.
3. Resolve codebase-answerable questions in the repository before asking the user.
4. Ask the highest-impact user-answerable questions, then repeat until no draft-blocking unknown remains.

### Convergence rule

Do not begin writing the requirements draft until:

- all user-answerable questions with draft-blocking impact have been answered
- codebase-answerable questions have been investigated and findings confirmed
- remaining unknowns are explicitly moved to the deferred pool

### Shortcut

If the user already has a clear, detailed specification or explicitly asks to skip interrogation, proceed directly to drafting. Record the skip in `.carl/state.md`.

## Default behavior when loaded

1. Identify the current stage from artifacts and conversation context.
2. Restate the artifact expected at this stage.
3. Name who authored the current draft, who is reviewing it, and whether `Sisyphus` input is needed.
4. If no draft exists yet, begin the Pre-draft interrogation procedure.
5. Drive the next discovery, review, or promotion step forward.
6. When the requirements document reaches `final` and the stage is complete, automatically enter `technical-confirmation` when no unresolved product, scope, or shortcut decision remains. If input is still required, use the `ask question` interaction in the same response to keep the workflow moving.
