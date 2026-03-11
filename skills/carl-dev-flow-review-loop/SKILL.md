---
name: carl-dev-flow-review-loop
description: Run repeated code review, discussion, repair, and re-review cycles until Sisyphus, Hephaestus, and the user agree the code is ready for delivery.
version: 1.1.0
compatibility: opencode
license: CC-BY-4.0
metadata:
  audience: individual-developer
  domain: review
---

## Purpose

Use this skill after implementation exists and the goal is not just to patch code once, but to iterate until delivery quality is accepted.

This skill is the authoritative source for the detailed procedure of the `recursive-improvement` stage inside the Sisyphus and Hephaestus workflow family.

For the shortest Chinese invocation form, see `templates/minimal-zh.md`.

## Core loop

1. `Hephaestus` and the user review the current code.
2. Produce a review memo draft.
3. `Sisyphus` reviews that memo independently and states agreement, disagreement, and additions.
4. The user and `Sisyphus` align on the final review memo.
5. `Sisyphus` decomposes approved fixes and delegates them to sub-agents.
6. Fixes are implemented.
7. Repeat until all three parties accept the code as deliverable.

## Review memo structure

For each finding, record:

- severity
- file reference
- concrete symptom
- why it matters
- expected fix direction
- acceptance condition after repair

## Rules for recursion

- Every new fix round must be followed by another review round.
- New review findings must be compared against previous findings so resolved issues are not reopened casually.
- If a fix introduces regressions, create a new memo section for regressions instead of mutating history silently.
- Keep the latest agreed review memo as the repair source of truth.

## Useful companion skills

When available, prefer loading `code-review-expert` or `requesting-code-review` to strengthen review quality, reporting clarity, and repair tracking during each review round.

## Exit criteria

Do not stop the loop until:

- approved findings are fixed
- no unresolved blocking issue remains
- remaining issues are explicitly deferred and accepted
- `Sisyphus`, `Hephaestus`, and the user all agree the code is at delivery level


## Artifact location

Store review artifacts in `.carl/review/`:

- `.carl/review/memo-NNN.md` — numbered review memos per iteration

## Default behavior when loaded

The agent should:

1. identify the current fix-review iteration
2. summarize what changed since the last review
3. produce or refine the review memo
4. drive the next repair or re-review step
