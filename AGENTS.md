# AGENTS.md

## Project Overview

This repository contains a family of AI workflow skills for the OpenCode platform.
The skills coordinate a multi-stage collaboration model between a user, `Sisyphus`
(orchestration lead), and `Hephaestus` (reviewer/challenger). There is no runtime
application code — the primary artifacts are Markdown skill definitions and one
Python validation script.

## Repository Layout

```
carl-dev-flow-skills/
  .github/
    workflows/
      ci.yml                            # Drift checker + style checks + markdownlint
      links.yml                         # Link validation (PR internal + weekly full)
  .markdownlint-cli2.jsonc               # Markdownlint config scoped to repo files
  .lychee.toml                           # Link checker config
  README.md                              # Project history and design rationale
  AGENTS.md                              # This file
  skills/
    carl-dev-flow-orchestrator/          # Master lifecycle, role contract, transition rules
      SKILL.md
      scripts/check-workflow-skills.py   # Drift checker (only code file in repo)
      templates/minimal-zh.md
    carl-dev-flow-stage-router/          # Stage detection and routing entry point
      SKILL.md
      templates/zh_CN_INVOCATION.md
      templates/minimal-zh.md
    carl-dev-flow-requirements/          # Requirements-development stage procedure
      SKILL.md
      templates/minimal-zh.md
      templates/requirements-draft.md    # Fill-in skeleton for requirements draft
    carl-dev-flow-tech-spec/             # Technical-confirmation stage procedure
      SKILL.md
      templates/minimal-zh.md
      templates/tech-spec-draft.md       # Fill-in skeleton for tech spec draft
      templates/adr-template.md          # MADR-derived decision record template
    carl-dev-flow-implementation/        # Development-execution stage procedure
      SKILL.md
      templates/minimal-zh.md
      templates/task-plan.md             # Fill-in skeleton for task plan
      templates/slices.md               # Fill-in skeleton for delivery slices
    carl-dev-flow-review-loop/           # Recursive-improvement stage procedure
      SKILL.md
      templates/minimal-zh.md
      templates/review-memo.md           # Fill-in skeleton for review memo
    carl-dev-flow-bugfix/              # Bug-fix workflow orchestration
      SKILL.md
      templates/minimal-zh.md
```

## Build / Lint / Test Commands

There is no build step. The only verification command is the drift checker:

```bash
# Run the full skill-family validation (the only "test" in this repo)
python3 skills/carl-dev-flow-orchestrator/scripts/check-workflow-skills.py
```

The checker validates:
- All seven skill directories exist with a `SKILL.md`
- Each `SKILL.md` has required YAML frontmatter keys and required values
- Versions are consistent across the family (currently `1.3.0`)
- Required wording is present in each skill
- Forbidden wording is absent
- Expected Chinese invocation templates and stage skeleton templates exist
There is no single-test mode — the script is all-or-nothing. Run it after every
change to any `SKILL.md` file.

## CI Workflows

Two GitHub Actions workflows gate pull requests and monitor link health:

- **`ci.yml`** — Runs on PRs and pushes to `main` when `*.md`, `*.py`, or CI
  config files change. Steps: drift checker → SKILL.md style checks → template
  size check → markdownlint.
- **`links.yml`** — Checks internal links (fragment-aware) on PRs. Runs a full
  external link check weekly (Monday 03:00 UTC).

Configuration files:
- `.markdownlint-cli2.jsonc` — scoped to repo Markdown files only (excludes
  external directories)
- `.lychee.toml` — link checker settings (accept codes, exclude patterns,
  fragment validation)

## SKILL.md Format (Mandatory)

Every skill file uses this structure:

```markdown
---
name: carl-dev-flow-{slug}
description: One-line description of the skill.
version: 1.3.0
compatibility: opencode
license: CC-BY-4.0
metadata:
  audience: individual-developer
  domain: {domain-value}
---

## Purpose

(What the skill does and when to load it.)

## Workflow / Core model / Core loop

(Stage-specific procedure.)

...additional sections as needed...
```

### Frontmatter Rules

| Key             | Required | Notes                                                  |
|-----------------|----------|--------------------------------------------------------|
| `name`          | Yes      | Must match directory name exactly                      |
| `description`   | Yes      | Single line, no period at end                          |
| `version`       | Yes      | Must match across all seven skills                     |
| `compatibility` | Yes      | Always `opencode`                                      |
| `license`       | Yes      | `CC-BY-4.0`                                            |
| `metadata`      | Yes      | Must include `audience` and `domain`                   |

### Version Consistency

All seven SKILL.md files must declare the same `version`. The drift checker enforces
this. When bumping the version, update all seven files in a single change.

## Content Conventions

### Ownership Model (Anti-Drift Rule)

- The **orchestrator** skill owns lifecycle, role boundaries, stage order, and routing.
  It must stay short and structural. No stage-specific step-by-step detail.
- Each **stage skill** is the authoritative source for its own detailed procedure.
  Stage-specific content must not be duplicated in the orchestrator.
- If a rule is stage-specific, update the relevant subskill first.
- If a rule changes lifecycle or role contract, update the orchestrator.

### Naming

- Skill directories: `carl-dev-flow-{slug}` (lowercase, hyphen-separated)
- Stage names in prose: backtick-quoted, e.g. `` `requirements-development` ``
- Role names in prose: backtick-quoted, e.g. `` `Sisyphus` ``, `` `Hephaestus` ``

### Markdown Style

- Use `##` for top-level sections inside SKILL.md (not `#` — that level is unused)
- Use `-` for unordered lists, `1.` for ordered procedure steps
- No trailing whitespace, no blank lines at end of file
- One blank line between sections
- Wrap prose at reasonable line length (no strict column limit observed)
- No emojis in skill definitions

### Template Files

- Chinese templates live in `templates/` subdirectory per skill
- Template filenames: `minimal-zh.md` (minimal Chinese prompt) or
  `zh_CN_INVOCATION.md` (Chinese invocation examples)
- Structured templates (fill-in skeletons): `requirements-draft.md`,
  `tech-spec-draft.md`, `adr-template.md`, `task-plan.md`, `slices.md`,
  `review-memo.md`
- Templates are short (target <= 30 lines)

## Python Script Style (check-workflow-skills.py)

The single Python file follows these conventions:

- `#!/usr/bin/env python3` shebang
- `from __future__ import annotations` at top
- Standard library only (no third-party dependencies)
- Type hints on all function signatures (including `-> NoReturn`, `-> int`)
- `Path` from `pathlib` for filesystem operations (not `os.path`)
- `fail()` helper for fatal errors (prints message, raises `SystemExit(1)`)
- Constants as module-level `UPPER_SNAKE_CASE`
- Functions as `lower_snake_case`
- `if __name__ == "__main__": sys.exit(main())` entry pattern

## Key Design Principles

1. Workflow is explicit — every stage has a named artifact and promotion rule
2. Artifacts are stage-based — `draft -> revised -> final` lifecycle
3. The user is the final decision-maker when agents disagree
4. The master skill is structural — stage details live in subskills only
5. The family must be easy to publish and understand at a glance

## Workflow Stages (Reference)

| Stage                      | Skill                          | Artifact Flow                      |
|----------------------------|--------------------------------|------------------------------------|
| requirements-development   | carl-dev-flow-requirements     | draft → revised → final            |
| technical-confirmation     | carl-dev-flow-tech-spec        | draft → revised → final            |
| development-execution      | carl-dev-flow-implementation   | tasks → integrated code            |
| recursive-improvement      | carl-dev-flow-review-loop      | review memo → fixes → re-review    |

## Common Pitfalls

- **Duplicating stage detail in orchestrator**: Violates ownership model; update
  the stage subskill instead.
- **Version mismatch**: Editing one SKILL.md version without updating all seven
  will fail the drift checker.
- **Adding forbidden wording**: The checker blocks specific phrases in certain
  skills (e.g., "requirements draft" in orchestrator). Check `EXPECTED` dict in
  `check-workflow-skills.py` before adding content.
- **Missing required wording**: Each skill has required phrases that must appear
  somewhere in the file. See `EXPECTED["required"]` in the checker script.
