---
name: carl-dev-flow-requirements
description: Run the requirements-development stage where the user, Sisyphus, and Hephaestus converge on a final requirements document through draft, review, and revision.
version: 1.1.0
compatibility: opencode
license: CC-BY-4.0
metadata:
  audience: individual-developer
  domain: requirements
---

## Purpose

Use this skill when the user is still shaping business intent, behavior boundaries, edge cases, and acceptance expectations.

This skill is the authoritative source for the detailed procedure of the `requirements-development` stage inside the Sisyphus and Hephaestus workflow family.

For the shortest Chinese invocation form, see `templates/minimal-zh.md`.

## Required lifecycle

The requirements artifact must evolve through:

- `requirements draft`
- `requirements revised draft`
- `requirements final`

## Workflow

1. One agent leads the Q and A discovery with the user.
2. The discussion leader writes the initial requirements draft.
3. The other agent reviews the draft without being the original author.
4. The reviewer normalizes structure, checks logic flow, and hunts for missing edge cases.
5. The document becomes a revised draft.
6. The user, `Sisyphus`, and `Hephaestus` review the revised draft together.
7. Resolve disagreements in the document.
8. Produce the final requirements document.

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
- unresolved questions
- what changed from draft to revised
- what conditions are needed to promote to final

## Promotion rule

Do not call the document final until:

- major terms are defined
- edge cases are either resolved or explicitly deferred
- the user confirms the behavior matches intent
- both `Sisyphus` and `Hephaestus` have had a review opportunity


## Artifact location

Store requirements artifacts in `.carl/requirements/`:

- `.carl/requirements/draft.md`
- `.carl/requirements/revised.md`
- `.carl/requirements/final.md`

## Requirements format guidance

For testable requirements, consider EARS (Easy Approach to Requirements Syntax):

- Ubiquitous: "The `<system>` shall `<response>`."
- Event-driven: "When `<trigger>`, the `<system>` shall `<response>`."
- State-driven: "While `<state>`, the `<system>` shall `<response>`."
- Unwanted: "If `<condition>`, then the `<system>` shall `<response>`."

Each EARS requirement maps directly to one acceptance criterion.
This format is recommended but not mandatory.

## Default behavior when loaded

The agent should:

1. Identify the current stage from available artifacts and conversation context.
2. Restate the artifact expected at this stage.
3. Name who authored the current draft and who is reviewing it.
4. Drive the next discovery, review, or promotion step forward.
