---
name: carl-dev-flow-review-loop
description: Run repeated code review, discussion, repair, and re-review cycles until Hephaestus, Oracle, and the user agree the code is ready for delivery
version: 2.1.0
compatibility: opencode
license: CC-BY-4.0
metadata:
  audience: individual-developer
  domain: review
---

## Purpose

Use this skill after implementation exists and the goal is to iterate until delivery quality is accepted.
This skill is the authoritative source for the detailed procedure of the `recursive-improvement` stage inside the Hephaestus-led workflow family.

For the shortest Chinese invocation form, see `templates/minimal-zh.md`.

## Core loop

1. `Oracle` and the user review the current code.
2. `Oracle` produces the review memo draft and owns the first review judgment.
3. `Hephaestus` triages that memo, states agreement, disagreement, and the planned repair sequence.
4. The user and `Hephaestus` align on the agreed review memo.
5. `Hephaestus` decomposes approved fixes and delegates them to `Sisyphus` or other execution sub-agents.
6. Fixes are implemented and then re-reviewed by `Oracle`.
7. Repeat until all three parties accept the code as deliverable.

## Automation boundary

Within the review-fix-re-review cycle, `Hephaestus` proceeds autonomously through each iteration.
Do not pause for user confirmation between memo refinement, fix delegation, implementation integration, and re-review.
Use the `ask question` interaction only when the loop is exiting toward delivery, a new stage-level decision is required, or workflow completion needs a follow-up choice.

## Review ownership constraint

`Oracle` is the reviewer of record for this stage. This is non-negotiable.

- `Oracle` must personally inspect the code, write the findings, and stand behind the review memo.
- Do not delegate the review itself away from `Oracle` to any other agent. `Hephaestus` must not rewrite or override `Oracle` findings before the user sees them.
- Specialist agents may advise on narrow technical questions after `Oracle` has written the findings, but their input is advisory only and does not replace `Oracle` as author of the review memo.
- If `Hephaestus` needs to invoke review, it must invoke `Oracle` directly, never route the review through another agent.

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

`code-review-expert` or `requesting-code-review` may help with memo formatting or repair tracking after `Oracle` has written the findings.
They do not replace `Oracle` as reviewer of record. See the review ownership constraint above.

## Exit criteria

Do not stop the loop until:

- approved findings are fixed
- no unresolved blocking issue remains
- remaining issues are explicitly deferred and accepted
- `Hephaestus`, `Oracle`, and the user all agree the code is at delivery level

When all exit criteria are met and the loop is ready to exit toward delivery, use the `ask question` interaction to summarize delivery readiness and keep the conversation alive unless the user has already explicitly ended the workflow. This is recommended when deferred issues exist or when the review involved multiple iteration rounds.

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
5. When all exit criteria are met and the code is accepted as deliverable, use the `ask question` interaction to confirm follow-up or closeout options in the same response and summarize the overall workflow outcome.
