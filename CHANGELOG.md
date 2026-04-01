# Changelog

All notable changes to the carl-dev-flow-skills family will be documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [2.0.0] - 2026-04-01

### Changed

- Workflow contract inverted for the Copilot-first workflow model:
  - `Hephaestus` is now the orchestration lead and stage-transition owner
  - `Oracle` is now the reviewer of record for requirements, technical design,
    integrated code, and bug-fix verification
  - `Sisyphus` is now the technical striker for hard implementation and repair
    execution
- Orchestrator, stage router, and all stage skills rewritten around explicit
  orchestration / review / execution lanes
- Drift checker updated to enforce `Oracle` review ownership and
  `Hephaestus` orchestration wording across the full seven-skill family
- Public documentation and Chinese invocation templates updated to describe the
  new role contract
- `GLOBAL_SISYPHUS_CONTINUITY_OVERRIDE.md` renamed to
  `LEAD_AGENT_CONTINUITY_OVERRIDE.md` for role-neutral naming
- Orchestration semantics fit within existing skill bodies; no companion skill
  was needed

## [1.4.0] - 2026-03-20

### Changed

- Skill family compressed for lower token usage while preserving the staged
  artifact workflow
- Review ownership clarified around `Hephaestus` across the pre-2.0 workflow
  line
- Session continuity rules added so stage transitions use interactive questions
  while intra-stage progression remains autonomous

## [1.3.0] - 2025-03-18

### Added

- Pre-draft interrogation procedure in `carl-dev-flow-requirements`: structured
  question categories (user-answerable, codebase-answerable, deferred),
  convergence rule, and shortcut mechanism for experienced users
- Execution modes in `carl-dev-flow-implementation`: `tdd-first`,
  `characterization-first`, and `direct` modes with TDD loop procedure and
  anti-patterns
- Slice decomposition in `carl-dev-flow-implementation`: vertical slice
  breakdown with behavior, dependency, and verification attributes
- New `slices.md` template for delivery slice breakdowns

### Changed

- Requirements draft template enriched with problem statement, success signals,
  constraints/assumptions/resolved decisions sections (consolidated to stay
  within 30-line template limit)
- Task plan template updated with execution mode, slice-ref, first behavior to
  prove, test boundary, and refactor follow-up fields
- Chinese templates updated for requirements and implementation skills
- Drift checker updated with new required wording and template validation
- CI template size check updated to include `slices.md`

## [1.2.0] - 2025-03-13

### Added

- New `carl-dev-flow-bugfix` skill: severity grading (lightweight vs complex),
  fix-path routing, minimal-change principles, and regression-first exit criteria
- Bug-fix adaptation sections in three stage skills:
  - `carl-dev-flow-tech-spec` — root cause analysis, blast radius assessment
  - `carl-dev-flow-implementation` — minimal fix principle, regression baseline
  - `carl-dev-flow-review-loop` — regression verification primary, fix effectiveness
- Orchestrator updated with bugfix ownership model, routing rules, and artifact
  location convention (`.carl/bugfix/`)
- Stage router updated with bug-fix detection in stage classifier
- Drift checker updated for 7-skill family validation (9 templates)


## [1.1.0] - 2025-03-11

### Added

- Artifact location convention: `.carl/` directory structure prescribed by orchestrator,
  with per-stage paths in each stage skill (`requirements/`, `tech-spec/`,
  `implementation/`, `review/`)
- State tracking convention: lightweight `.carl/state.md` with four fields
  (stage, artifact-status, last-updated-by, open-blockers)
- Structured fill-in templates for each stage:
  - `requirements-draft.md` (requirements skeleton)
  - `tech-spec-draft.md` (tech spec skeleton)
  - `adr-template.md` (MADR-derived decision record)
  - `task-plan.md` (implementation task plan)
  - `review-memo.md` (review memo skeleton)
- ADR guidance section in tech-spec skill with MADR-derived compact format
- Pre-edit checklist in implementation skill (verify requirements and tech spec
  are finalized before code changes)
- EARS format guidance in requirements skill (optional ubiquitous/event-driven/
  state-driven/unwanted-behavior syntax patterns)
- Drift checker now validates template file existence (8 templates across 6 skills)
- Drift checker now enforces new required wording for v1.1.0 additions
- CI workflows: drift checker, SKILL.md style checks, markdownlint, and link
  validation via GitHub Actions (`ci.yml`, `links.yml`)
- Markdownlint configuration (`.markdownlint-cli2.jsonc`) scoped to repo files
- Link checker configuration (`.lychee.toml`) with fragment validation

## [1.0.0] - 2025-01-01

### Added

- Initial skill family with six skills:
  - `carl-dev-flow-orchestrator` — master lifecycle and role contract
  - `carl-dev-flow-stage-router` — stage detection and routing
  - `carl-dev-flow-requirements` — requirements-development procedure
  - `carl-dev-flow-tech-spec` — technical-confirmation procedure
  - `carl-dev-flow-implementation` — development-execution procedure
  - `carl-dev-flow-review-loop` — recursive-improvement procedure
- Chinese invocation templates (`zh_CN_INVOCATION.md`, `minimal-zh.md`)
- Drift checker script (`check-workflow-skills.py`)
- Anti-drift ownership model separating orchestrator from stage details