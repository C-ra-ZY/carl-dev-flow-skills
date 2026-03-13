# Changelog

All notable changes to the carl-dev-flow-skills family will be documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

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