# Benchmark Borrowing Proposal

This document translates external workflow-skill ideas into a concrete upgrade
plan for the `carl-dev-flow-*` family.

It focuses on the three quality goals currently most important to this repo:

1. clarify requirements thoroughly through interaction
2. make artifacts guide development clearly
3. make the coding -> verify -> review loop high-quality and repeatable

## Why this proposal exists

The current family already has strong stage structure:

- `requirements` owns draft -> revised -> final requirements
- `tech-spec` owns draft -> revised -> final technical decisions plus ADRs
- `implementation` owns task decomposition and integration
- `review-loop` owns recursive review memos and repair cycles
- `bugfix` owns bug-fix routing, severity grading, and regression-focused adjustments

That structure is good and should be preserved.

The missing piece is not "more workflow" in general. The missing piece is a set
of sharper sub-procedures inside that workflow:

- a stronger pre-draft interrogation phase
- a stronger artifact-to-execution decomposition phase
- a stronger test-first execution mode for coding work
- a stronger architecture-quality companion for refactor and testability work

## Benchmark sources reviewed

### Primary benchmark set

- `mattpocock/skills@grill-me`
- `mattpocock/skills@write-a-prd`
- `mattpocock/skills@prd-to-issues`
- `mattpocock/skills@tdd`
- `mattpocock/skills@improve-codebase-architecture`

These are the exact or near-exact skills referenced by the public discussion we
investigated. They are useful because they form a coherent chain:

- interrogate the idea
- turn it into a document
- break the document into thin slices
- execute with TDD
- periodically improve architecture for testability

### Secondary benchmark set

- `github/awesome-copilot@prd`
- `github/awesome-copilot@gen-specs-as-issues`
- `github/awesome-copilot@review-and-refactor`
- `obra/superpowers@requesting-code-review`

These are valuable as scale or quality references. They are less tightly aligned
as a single delivery chain, but they confirm that the surrounding ecosystem also
values specification quality, issue decomposition, and explicit review loops.

## Current repo strengths

The current family already has several strong foundations worth preserving.

### 1. Stage ownership is clear

- `skills/carl-dev-flow-requirements/SKILL.md` already separates discovery,
  reviewer checks, output contract, and promotion rules.
- `skills/carl-dev-flow-tech-spec/SKILL.md` already separates feasibility,
  tradeoffs, ADR capture, and promotion to final.
- `skills/carl-dev-flow-implementation/SKILL.md` already requires scoped tasks,
  constraints, acceptance criteria, and verification.
- `skills/carl-dev-flow-review-loop/SKILL.md` already requires memo-driven,
  recursive repair instead of one-shot review.

### 2. Artifact discipline is strong

- `skills/carl-dev-flow-orchestrator/SKILL.md` defines explicit document
  lifecycles and `.carl/` locations.
- `skills/carl-dev-flow-implementation/templates/task-plan.md` already stores
  decomposition and delegation history.
- `skills/carl-dev-flow-tech-spec/templates/tech-spec-draft.md` already makes
  room for alternatives, risks, and rollout planning.

### 3. Bug-fix workflow already reflects good engineering instincts

- `skills/carl-dev-flow-bugfix/SKILL.md` already encodes reproduction,
  regression baseline, blast radius, and minimal fix thinking.

## Current gaps relative to the benchmark skills

### Gap A: Discovery is present, but not aggressive enough

`skills/carl-dev-flow-requirements/SKILL.md` says to lead Q and A discovery, but
it does not yet require a design-tree style interrogation before the first draft.

What is currently missing:

- explicit branching questions before drafting
- explicit option comparison before convergence
- a stop condition of "draft only after the unknown branches are surfaced"
- a distinction between questions that need user answers vs questions that can be
  resolved by reading the repo

This is the strongest lesson from `grill-me`.

### Gap B: Requirements and spec artifacts are good documents, but not yet strong enough as execution launchpads

The current family promotes artifacts to `final`, but there is no dedicated step
that turns those finalized artifacts into independently executable slices.

What is currently missing:

- a standard "vertical slice" decomposition artifact
- optional GitHub issue creation from approved slices
- explicit dependency mapping between slices
- traceability from slice -> requirement / user-visible behavior

This is the strongest lesson from `prd-to-issues`.

### Gap C: Verification is required, but implementation does not yet define a first-class TDD execution mode

`skills/carl-dev-flow-implementation/SKILL.md` requires verification and task
breakdown, but it does not yet prescribe:

- one behavior at a time
- test first where appropriate
- red -> green -> refactor discipline
- tracer-bullet vertical slices instead of horizontal layers
- the difference between behavior tests and implementation-detail tests

This is the strongest lesson from `tdd`.

### Gap D: Architecture quality is mentioned through ADRs, but not audited as its own repeatable improvement motion

`skills/carl-dev-flow-tech-spec/SKILL.md` captures architecture decisions, but
the family does not yet include a standing companion skill for:

- identifying shallow modules
- identifying poor test boundaries
- proposing deep-module refactors
- producing architecture hardening proposals outside feature delivery

This is the strongest lesson from `improve-codebase-architecture`.

## What to borrow, what to adapt, what to reject

### Borrow directly

- `grill-me`: design-tree questioning before drafting
- `prd-to-issues`: thin vertical slices and dependency-aware decomposition
- `tdd`: one-slice-at-a-time red -> green -> refactor loop
- `improve-codebase-architecture`: deep-module / testability framing
- `requesting-code-review`: review early, review often

### Adapt heavily

- `write-a-prd`: keep the interview and scoping value, but map it onto
  `requirements-development` instead of introducing PRD as the main local term
- GitHub issue generation: keep it optional, because the family should still work
  in repos that are not issue-driven
- architecture issue RFCs: keep the proposal mindset, but fit it into local
  artifacts rather than forcing a foreign issue template

### Reject

- replacing the current stage model with a PRD-centered model
- making GitHub issue creation mandatory for every project
- collapsing all quality logic into `orchestrator`
- importing slash-command naming directly into this repo's public API

## Proposed transformation plan

### Proposal 1: Strengthen requirement clarification with a formal interrogation mode

#### Goal

Make `requirements-development` reliably push vague ideas into a clarified,
reviewable, testable document before draft writing begins.

#### Changes

1. Update `skills/carl-dev-flow-requirements/SKILL.md`
   - Add `Pre-draft interrogation` section
   - Add rules for design-tree questioning
   - Require separation of:
     - user-answerable questions
     - codebase-answerable questions
     - explicitly deferred questions
   - Require convergence before initial draft writing

2. Update `skills/carl-dev-flow-requirements/templates/requirements-draft.md`
   - Add `Problem statement`
   - Add `Success signals`
   - Add `Constraints and assumptions`
   - Add `Resolved decisions`
   - Keep `Open questions`, but make it the residue after interrogation, not the
     main discovery engine

3. Update `skills/carl-dev-flow-stage-router/SKILL.md`
   - Clarify that vague feature ideas route to `requirements` in interrogation
     mode before any drafting or implementation planning

#### Why this is worth doing

This directly serves the goal of "through interaction, fully clarify the
requirements" without changing the current stage model.

### Proposal 2: Add a companion skill for artifact-to-slice decomposition

#### Goal

Turn `requirements final` plus `technical spec final` into actionable, parallel,
reviewable delivery slices.

#### New skill

Create a new companion skill with a local name aligned to this repo, for example:

- `carl-dev-flow-delivery-slices`

Recommended purpose:

- read `requirements final` and `technical spec final`
- derive thin vertical slices
- mark blockers and dependencies
- identify HITL vs AFK work where useful
- optionally create GitHub issues
- write an intermediate artifact even when GitHub issues are not created

#### New artifact

Recommended path:

- `.carl/implementation/slices.md`

Recommended contents:

- slice title
- user-visible behavior delivered
- requirements/spec references
- layers touched
- blockers
- expected verification
- whether the slice is safe for AFK execution

#### Related file changes

1. Add new skill directory and `SKILL.md`
2. Add `templates/slices.md`
3. Update `skills/carl-dev-flow-orchestrator/SKILL.md`
   - mention this companion as the bridge between `technical-confirmation` and
     `development-execution`
4. Update `skills/carl-dev-flow-implementation/templates/task-plan.md`
   - include `slice-ref`
   - include `behavior delivered`
   - include `verification boundary`

#### Why this is worth doing

This is the cleanest way to make the documents "guide development clearly"
instead of becoming passive paperwork.

### Proposal 3: Add a first-class TDD execution mode to implementation

#### Goal

Make `development-execution` reliably produce better code through a repeatable,
test-first loop when the project context supports it.

#### Changes

1. Update `skills/carl-dev-flow-implementation/SKILL.md`
   - Add `Execution modes`
   - Recommended modes:
     - `tdd-first` for new behavior or when test boundaries are clear
     - `characterization-first` for brownfield or regression-prone work
     - `direct implementation` only when tests are impossible or not meaningful,
       with an explicit explanation
   - Add a `Tracer-bullet loop` subsection
   - Add explicit anti-pattern: no horizontal slice execution

2. Update `skills/carl-dev-flow-implementation/templates/task-plan.md`
   - add `execution mode`
   - add `first behavior to prove`
   - add `test boundary`
   - add `refactor follow-up`

3. Update `skills/carl-dev-flow-review-loop/SKILL.md`
   - add review guidance for test quality:
     - verify tests target behavior, not implementation details
     - verify slice sequencing did not skip required proof steps
     - verify refactor happened only after green where TDD mode was chosen

4. Update `skills/carl-dev-flow-bugfix/SKILL.md`
   - clarify characterization-test preference for complex bugfixes where current
     behavior must be captured before changing it

#### Why this is worth doing

This is the highest-leverage change for the goal of a high-quality automated
coding -> verify -> review loop.

### Proposal 4: Add an optional architecture-hardening companion skill

#### Goal

Give the family a repeatable way to improve agent navigability, module depth, and
testability outside feature delivery.

#### New skill

Recommended local name:

- `carl-dev-flow-architecture-audit`

Recommended responsibilities:

- inspect a codebase for shallow module clusters
- identify test boundary problems
- identify high-friction integration seams
- propose 2-4 refactor candidates
- optionally create a refactor memo or issue set

#### Recommended artifact

- `.carl/tech-spec/architecture-audit.md`

#### Related file changes

1. Add new skill directory and template
2. Update `skills/carl-dev-flow-stage-router/SKILL.md`
   - route requests like "improve architecture", "improve testability", or
     "reduce coupling" to this companion skill
3. Update `skills/carl-dev-flow-tech-spec/SKILL.md`
   - link ADR work to this audit when the request is refactor- or quality-led,
     rather than feature-led

#### Why this is worth doing

This keeps architecture improvement explicit instead of hoping it emerges from
feature work.

## Recommended rollout order

### Phase 1: Immediate high-value upgrades

1. Proposal 1: interrogation mode in `requirements`
2. Proposal 3: TDD execution mode in `implementation`

These directly improve discovery quality and execution quality without requiring
new public skill names.

### Phase 2: Artifact-to-execution bridge

3. Proposal 2: `carl-dev-flow-delivery-slices`

This is the most important new companion skill because it turns finalized
artifacts into development guidance.

### Phase 3: Ongoing codebase quality companion

4. Proposal 4: `carl-dev-flow-architecture-audit`

This is strategically valuable, but it is less urgent than improving discovery
and execution inside the main delivery path.

## Minimal viable adaptation set

If we want the smallest possible change set with the biggest quality gain, do
only these three things first:

1. add interrogation mode to `requirements`
2. add TDD execution modes to `implementation`
3. add delivery-slice decomposition as a new companion skill

That trio covers the three user priorities directly:

- requirements become clearer
- documents become more executable
- coding and verification become more disciplined

## Proposed success criteria for the upgrade work

The borrowing effort should be considered successful if, after implementation:

1. vague feature requests spend longer in structured clarification before draft
2. finalized artifacts can be turned into slices without ad hoc replanning
3. implementation tasks consistently declare test boundary and execution mode
4. review memos can criticize poor verification quality, not just broken code
5. architecture-improvement requests have a first-class home in the family

## Recommendation

Proceed with a staged adaptation, not a copy.

The repo should preserve its existing identity:

- stage-based
- artifact-driven
- anti-drift
- user as final arbiter

But it should absorb four benchmark ideas aggressively:

- design-tree interrogation
- vertical-slice decomposition
- TDD execution modes
- architecture audit for deep modules and testability

The best next execution step is to implement Phase 1 and Phase 2 together as the
next version milestone, then add the architecture audit companion afterward.
