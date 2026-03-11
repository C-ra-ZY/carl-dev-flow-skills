---
name: carl-dev-flow-tech-spec
description: Run the technical-confirmation stage where the user, Sisyphus, and Hephaestus converge on a final technical spec through draft, feasibility review, and revision.
version: 1.0.0
compatibility: opencode
license: CC-BY-4.0
metadata:
  audience: individual-developer
  domain: technical-spec
---

## Purpose

Use this skill after the product requirements are stable enough to design implementation strategy.

This skill is the authoritative source for the detailed procedure of the `technical-confirmation` stage inside the Sisyphus and Hephaestus workflow family.

For the shortest Chinese invocation form, see `templates/minimal-zh.md`.

## Required lifecycle

The technical artifact must evolve through:

- `technical spec draft`
- `technical spec revised draft`
- `technical spec final`

## Workflow

1. One agent leads the technical discussion with the user.
2. Cover architecture, interfaces, storage, performance, operability, failure handling, and maintenance burden.
3. The discussion leader writes the initial technical spec draft.
4. The other agent reviews for feasibility, hidden assumptions, and missing constraints.
5. The document becomes a revised technical spec.
6. The user, `Sisyphus`, and `Hephaestus` review the revised spec together.
7. Resolve disagreements in writing.
8. Produce the final technical spec.

## Review checklist

- feasibility with current stack
- migration or rollout strategy
- failure modes and recovery behavior
- observability and health signals
- performance and rate-limit assumptions
- maintenance cost and operator burden
- interfaces between modules or services
- explicit tradeoffs and rejected alternatives

## Output contract

Always state:

- the primary technical decision under review
- why the proposed design was chosen
- what risks remain
- what changed from draft to revised
- what blocks promotion to final

## Promotion rule

Do not call the spec final until:

- implementation path is concrete enough to split into tasks
- operational and failure behavior is defined
- major alternatives have been considered or rejected
- the user accepts the tradeoffs

## Default behavior when loaded

The agent should:

1. Confirm that requirements are stable enough to design against.
2. Identify whether a draft, revised draft, or final spec exists.
3. Restate the primary technical decision under review.
4. Drive the next discussion, review, or promotion step forward.
