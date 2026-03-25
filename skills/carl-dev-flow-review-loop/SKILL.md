---
name: carl-dev-flow-review-loop
description: Run repeated code review, discussion, repair, and re-review cycles until Sisyphus, Hephaestus, and the user agree the code is ready for delivery.
version: 1.4.0
compatibility: opencode
license: CC-BY-4.0
metadata:
  audience: individual-developer
  domain: review
---

## Purpose

Use this skill after implementation exists and the goal is to iterate until delivery quality is accepted.
This skill is the authoritative source for the detailed procedure of the `recursive-improvement` stage inside the Sisyphus and Hephaestus workflow family.

For the shortest Chinese invocation form, see `templates/minimal-zh.md`.

## Core loop

1. `Hephaestus` and the user review the current code.
2. `Hephaestus` produces the review memo draft and owns the first review judgment.
3. `Sisyphus` reviews that memo independently and states agreement, disagreement, and additions.
4. The user and `Sisyphus` align on the agreed review memo.
5. `Sisyphus` decomposes approved fixes and delegates them to sub-agents.
6. Fixes are implemented and then re-reviewed.
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

`code-review-expert` or `requesting-code-review` may help with memo formatting or repair tracking after `Hephaestus` has written the findings.
They do not replace `Hephaestus` as reviewer of record.
Do not delegate the review itself to `Oracle` or any other agent; `Hephaestus` must inspect the code, write the findings, and stand behind the memo.

## Exit criteria

Do not stop the loop until:

- approved findings are fixed
- no unresolved blocking issue remains
- remaining issues are explicitly deferred and accepted
- `Sisyphus`, `Hephaestus`, and the user all agree the code is at delivery level

When all exit criteria are met, consider using interactive questions to confirm delivery readiness with the user. This is recommended when deferred issues exist or when the review involved multiple iteration rounds.

## Artifact location

Store numbered review memos under `.carl/review/`, such as `memo-NNN.md`.


## Bug-fix adaptation

When this stage is entered as part of a bug-fix workflow (routed from `carl-dev-flow-bugfix`):

- **Regression verification is the primary review objective.** Confirm that the regression baseline recorded before the fix still holds after the fix.
- Review findings must distinguish between: fix effectiveness (does it resolve the reported bug?), regression status (did the fix break anything else?), and blast radius accuracy (were the affected components correctly identified?).
- If the fix introduces new regressions, escalate immediately rather than continuing the normal review loop.

## Default behavior when loaded

1. Identify the current fix-review iteration.
2. Summarize what changed since the last review.
3. Produce or refine the review memo.
4. Drive the next repair or re-review step.
5. When all exit criteria are met and the code is accepted as deliverable, use interactive questions to confirm delivery with the user and summarize the overall workflow outcome in the same response.
