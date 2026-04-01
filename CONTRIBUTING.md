# Contributing to carl-dev-flow-skills

## Overview

This repository contains a family of seven OpenCode workflow skills. All changes
must keep the family consistent and pass the drift checker.

## Making changes

### Skill content (SKILL.md)

1. Identify the correct file to edit:
   - **Stage-specific** detail → edit the relevant sub-skill (`requirements`, `tech-spec`, `implementation`, `review-loop`)
   - **Lifecycle, role contract, or transition rules** → edit `carl-dev-flow-orchestrator`
   - **Stage detection or routing** → edit `carl-dev-flow-stage-router`
   - Do not duplicate stage-specific detail in the orchestrator
   - If the role contract changes, update the orchestrator, drift checker, and published docs together

2. Preserve required frontmatter keys: `name`, `description`, `version`, `compatibility`, `license`, `metadata`

3. Run verification after every change:

```bash
python3 skills/carl-dev-flow-orchestrator/scripts/check-workflow-skills.py
```

### Version bumps

All seven SKILL.md files must declare the same `version`. When bumping:

1. Update `version:` in all seven `SKILL.md` files
2. Update `SKILL_VERSION` in `scripts/check-workflow-skills.py`
3. Run the drift checker to confirm consistency
4. Update `CHANGELOG.md`

### Python script (check-workflow-skills.py)

- Standard library only — no third-party dependencies
- Type hints on all function signatures
- `pathlib.Path` for filesystem operations
- Run with Python >= 3.9

## Pull request process

1. Create a branch from `main`
2. Make your changes
3. Run the drift checker — it must pass
4. Open a PR with a clear description of what changed and why

## Reporting issues

Open a GitHub issue. Include:
- Which skill file is affected
- What behavior you expected vs. what you observed
- Drift checker output if relevant