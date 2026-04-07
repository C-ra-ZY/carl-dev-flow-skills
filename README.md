# carl-dev-flow-skills

A reusable AI workflow skill family for the [OpenCode](https://github.com/nicholasgriffintn/opencode) platform. It coordinates a multi-stage collaboration model between a user, **Hephaestus** (orchestration lead), **Oracle** (reviewer/challenger), and **Sisyphus** (technical striker).

The current contract favors automatic cross-stage advancement when the next step is clear, while reserving the `ask question` interaction for true boundary decisions and workflow closeout.

## What it does

The skill family breaks software delivery into four explicit stages, each with its own artifact lifecycle:

| Stage | Skill | Artifact Flow |
|---|---|---|
| Requirements Development | `carl-dev-flow-requirements` | draft → revised → final |
| Technical Confirmation | `carl-dev-flow-tech-spec` | draft → revised → final |
| Development Execution | `carl-dev-flow-implementation` | slices → tasks → integrated code |
| Recursive Improvement | `carl-dev-flow-review-loop` | review memo → fixes → re-review |

Three additional skills provide coordination:

- **`carl-dev-flow-orchestrator`** — master lifecycle contract, role boundaries, transition rules
- **`carl-dev-flow-stage-router`** — fast stage detection and routing entry point
- **`carl-dev-flow-bugfix`** — bug-fix severity grading, fix-path routing, and minimal-change principles

## Quick start

1. Install the skills into your OpenCode skill directory:

```bash
# Copy the skill family into your OpenCode skills location
cp -r skills/carl-dev-flow-* ~/.config/opencode/skills/
```

2. In an OpenCode session, load the orchestrator or router:

```
Load carl-dev-flow-orchestrator and let Hephaestus drive the workflow forward.
```

Or start from stage detection:

```
Load carl-dev-flow-stage-router to identify the current stage and next action.
```

3. Chinese invocation templates are available in each skill's `templates/` directory.

## Repository layout

```
skills/
  carl-dev-flow-orchestrator/       # Master lifecycle and role contract
    SKILL.md
    scripts/check-workflow-skills.py
    templates/minimal-zh.md
  carl-dev-flow-stage-router/       # Stage detection and routing
    SKILL.md
    templates/zh_CN_INVOCATION.md
    templates/minimal-zh.md
  carl-dev-flow-requirements/       # Requirements-development procedure
    SKILL.md
    templates/minimal-zh.md
    templates/requirements-draft.md
  carl-dev-flow-tech-spec/          # Technical-confirmation procedure
    SKILL.md
    templates/minimal-zh.md
    templates/tech-spec-draft.md
    templates/adr-template.md
  carl-dev-flow-implementation/     # Development-execution procedure
    SKILL.md
    templates/minimal-zh.md
    templates/task-plan.md
    templates/slices.md
  carl-dev-flow-review-loop/        # Recursive-improvement procedure
    SKILL.md
    templates/minimal-zh.md
    templates/review-memo.md
  carl-dev-flow-bugfix/              # Bug-fix workflow orchestration
    SKILL.md
    templates/minimal-zh.md
```

## Verification

Run the drift checker to validate skill family consistency:

```bash
python3 skills/carl-dev-flow-orchestrator/scripts/check-workflow-skills.py
```

Expected output:

```
Workflow skill family check passed: 7 files verified, 10 templates validated,
required wording present, forbidden wording absent, versions consistent.
```

Requires **Python >= 3.9** (no third-party dependencies).

## Key design principles

1. Every stage has a named artifact and explicit promotion rule
2. The user is the final decision-maker when agents disagree
3. The orchestrator is structural — stage details live in sub-skills only
4. The skill family must be easy to publish and understand at a glance

For full design history, see [docs/HISTORY.md](docs/HISTORY.md).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on making changes, running
verification, and version management.

## License

[CC-BY-4.0](LICENSE)
