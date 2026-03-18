---
name: carl-dev-flow-tech-spec
description: Run the technical-confirmation stage where the user, Sisyphus, and Hephaestus converge on a final technical spec through draft, feasibility review, and revision.
version: 1.3.0
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
- explicit tradeoffs and rejected alternatives documented as ADR

## Output contract

Always state:

- the primary technical decision under review
- why the proposed design was chosen
- what risks remain
- what changed from draft to revised
- what blocks promotion to final
- rejected alternatives as ADR files when architectural decisions are involved

## Promotion rule

Do not call the spec final until:

- implementation path is concrete enough to split into tasks
- operational and failure behavior is defined
- major alternatives have been considered, rejected, and recorded as ADRs with status `accepted`
- the user accepts the tradeoffs


## Artifact location

Store technical spec artifacts in `.carl/tech-spec/`:

- `.carl/tech-spec/draft.md`
- `.carl/tech-spec/revised.md`
- `.carl/tech-spec/final.md`
- `.carl/tech-spec/decisions/` — architecture decision records

## ADR guidance

Record major architectural decisions as ADR files in `.carl/tech-spec/decisions/` using the template in `templates/adr-template.md`.
Each ADR tracks status (`proposed`, `accepted`, `rejected`), the options considered, and the chosen outcome with consequences.
Do not promote the technical spec to `final` until all referenced ADRs have status `accepted`.

## Bug-fix adaptation

When this stage is entered as part of a bug-fix workflow (routed from `carl-dev-flow-bugfix`):

- Replace architecture design with **root cause analysis**: identify what broke and why.
- Replace interface and module design with **blast radius assessment**: determine which components are affected.
- The review checklist shifts to: root cause confidence, blast radius completeness, minimal fix feasibility, and regression risk.
- The output contract shifts to: root cause explanation, affected components, proposed minimal fix strategy, and remaining uncertainty.
- Promotion rule: do not promote until root cause is confirmed and blast radius is bounded.

## Default behavior when loaded

The agent should:

1. Confirm that requirements are stable enough to design against.
2. Identify whether a draft, revised draft, or final spec exists.
3. Restate the primary technical decision under review.
4. Drive the next discussion, review, or promotion step forward.
