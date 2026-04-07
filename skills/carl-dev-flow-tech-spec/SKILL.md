---
name: carl-dev-flow-tech-spec
description: Run the technical-confirmation stage where Hephaestus leads design, Oracle reviews, and the user converges on a final technical spec
version: 2.1.0
compatibility: opencode
license: CC-BY-4.0
metadata:
  audience: individual-developer
  domain: technical-spec
---

## Purpose

Use this skill after product requirements are stable enough to design the implementation strategy.
This skill is the authoritative source for the detailed procedure of the `technical-confirmation` stage inside the Hephaestus-led workflow family.

For the shortest Chinese invocation form, see `templates/minimal-zh.md`.

## Required lifecycle

The technical artifact must evolve through:

- `technical spec draft`
- `technical spec revised draft`
- `technical spec final`

## Workflow

1. `Hephaestus` leads the technical discussion with the user and writes the initial technical spec draft.
2. Cover architecture, interfaces, storage, performance, operability, failure handling, and maintenance burden.
3. `Oracle` reviews for feasibility, hidden assumptions, and missing constraints.
4. If delivery complexity is material, `Sisyphus` contributes implementation-feasibility input before promotion.
5. `Hephaestus` revises the document in writing and synthesizes unresolved issues.
6. The user, `Hephaestus`, and `Oracle` align on the revised spec, consulting `Sisyphus` when implementation constraints matter.
7. Produce the final technical spec only after unresolved issues are explicitly closed or deferred.

The reviewer of record is `Oracle` (the review lane owner), not an outside reviewer.

## Review checklist

- feasibility with current stack
- migration or rollout strategy
- failure modes and recovery behavior
- observability and health signals
- performance and rate-limit assumptions
- maintenance cost and operator burden
- interfaces between modules or services
- explicit tradeoffs and rejected alternatives documented as ADR

## Output contract

Always state:

- the primary technical decision under review
- why the proposed design was chosen
- whether `Sisyphus` implementation-feasibility input was consulted
- what risks remain
- what changed since the last draft
- what blocks promotion to final
- rejected alternatives documented as ADR when architectural decisions are involved

## Promotion rule

Do not call the spec final until:

- implementation path is concrete enough to split into tasks
- operational and failure behavior is defined
- major alternatives have been considered, rejected, and recorded as ADRs with status `accepted`
- the user accepts the tradeoffs
- `Oracle` has had a review opportunity and `Hephaestus` has synthesized the resulting open issues
- any material implementation-feasibility blocker raised by `Sisyphus` is resolved or explicitly deferred
- any external advice is treated as advisory only, not as a substitute for `Oracle` review

When promoting the artifact within this stage (draft to revised, or revised to final), proceed automatically when the promotion conditions are clearly met and the user has already expressed agreement. Use the `ask question` interaction only when unresolved tradeoff, scope, or risk decisions still require user input.

## Artifact location

Store `draft.md`, `revised.md`, and `final.md` under `.carl/tech-spec/`.
Store architecture decision records under `.carl/tech-spec/decisions/`.

## ADR guidance

Record major architectural decisions as ADR files in `.carl/tech-spec/decisions/` using the template in `templates/adr-template.md`.
Each ADR tracks status (`proposed`, `accepted`, `rejected`), options considered, and the chosen outcome with consequences.
Default decision-makers are `Hephaestus`, `Oracle`, and the user; `Sisyphus` is consulted when implementation constraints materially affect the decision.
Do not promote the technical spec to `final` until all referenced ADRs have status `accepted`.

## Bug-fix adaptation

When this stage is entered as part of a bug-fix workflow (routed from `carl-dev-flow-bugfix`):

- Replace architecture design with **root cause analysis** and **blast radius assessment**.
- The review checklist shifts to: root cause confidence, blast radius completeness, minimal fix feasibility, and regression risk.
- The output contract shifts to: root cause explanation, affected components, proposed minimal fix strategy, and remaining uncertainty.
- Promotion rule: do not promote until root cause is confirmed and blast radius is bounded.

## Default behavior when loaded

1. Confirm that requirements are stable enough to design against.
2. Identify whether a draft, revised draft, or final spec exists.
3. Restate the primary technical decision under review.
4. Drive the next discussion, review, or promotion step forward.
5. When the technical spec reaches `final` and the stage is complete, automatically enter `development-execution` when no unresolved tradeoff, scope, or risk decision remains. If input is still required, use the `ask question` interaction in the same response to keep the workflow moving.
