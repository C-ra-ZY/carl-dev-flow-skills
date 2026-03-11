# Development History

This document preserves the full design history of the `carl-dev-flow-*` skill
family. It was extracted from the original internal README when the repository
was prepared for public release.

## Origin

These skills did not start as a public package. They were first created inside
the local OpenCode skill directory as a way to stabilize a personal but
high-leverage development workflow.

The original intent was:

1. Capture a repeatable way of working with two top-tier coding agents
2. Make the workflow explicit instead of relying on memory or ad hoc prompting
3. Break the workflow into stages so each step has a clear artifact and promotion rule
4. Reduce drift over time by turning the workflow into maintainable skills

## Timeline

### 1. Initial workflow capture

The workflow was first described as a collaboration model involving three parties:

- The user as product and decision authority
- `Sisyphus` as orchestration lead
- `Hephaestus` as independent reviewer and challenger

The workflow itself was split into four stages:

1. `requirements-development`
2. `technical-confirmation`
3. `development-execution`
4. `recursive-improvement`

### 2. Skill family creation

The workflow was then encoded into a skill family inside the local skill runtime
directory. At that stage, the family included:

- One master workflow skill
- One kickoff/router skill
- Several stage-specific sub-skills

### 3. Anti-drift refactor

An early review identified a long-term maintainability risk: the master skill and
the stage sub-skills were too close in scope and could drift apart.

That led to an anti-drift refactor with these rules:

- The master skill owns only lifecycle, role boundaries, stage order, and routing
- Sub-skills own stage-specific step-by-step procedures
- Stage-specific details should not be duplicated in the master skill
- Each sub-skill must clearly state that it is the authoritative source for its stage

### 4. Quality improvements

After review, several improvements were made:

- Generalized requirements checklist wording so it is not tied to one project domain
- Added a greenfield default in the stage router
- Clarified `Hephaestus`'s role during execution
- Made the user the explicit final arbiter when agents disagree
- Added `version: 1.0.0` to all six skills
- Added review-helper skill guidance for the review loop

### 5. Usability improvements

The family was then made easier to use in practice:

- Chinese invocation templates were added
- Minimal per-skill Chinese prompt templates were added
- A drift checker script was added to catch structural regressions

### 6. Naming refactor

The earlier names were not ideal because they mixed personae and workflow semantics
in a way that was hard to scan. The family was renamed to the current unified scheme:

- `carl-dev-flow-orchestrator`
- `carl-dev-flow-stage-router`
- `carl-dev-flow-requirements`
- `carl-dev-flow-tech-spec`
- `carl-dev-flow-implementation`
- `carl-dev-flow-review-loop`

This naming scheme is more semantic, easier to understand at a glance, and better
suited for publishing and marketplace distribution.

### 7. Standalone repository extraction

The skill family was copied out of the runtime config directory into its own
repository. From this point forward, this repository is the canonical editable
codebase, while local runtime installation can later become a derived step.

## Design principles

This repository follows a few important rules:

- Keep the workflow explicit
- Keep artifacts stage-based
- Keep promotion rules explicit
- Keep the user as final decision-maker
- Keep the master skill structural
- Keep stage details in stage skills
- Keep the family easy to publish and understand