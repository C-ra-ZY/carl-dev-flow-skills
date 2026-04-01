# Workflow-aware lead-agent continuity override

This file keeps its legacy filename for compatibility, but the override below is
role-neutral and intended for whichever agent currently owns workflow-level
continuity. In the current contract, that lead agent is `Hephaestus`.

## Prompt text

When no workflow-specific skill family is active, keep the default continuity behavior: avoid ending the conversation early and prefer interactive handoff at the end of the response.

When the active workflow is the `carl-dev-flow` family (for example, a `carl-dev-flow-*` skill is loaded, `.carl/state.md` is active, or the current stage is explicitly tracked), apply continuity rules only at stage boundaries and workflow completion.

Do not let the continuity optimization override intra-stage autonomous progression defined by the workflow skills. In particular:

- use interactive questions for cross-stage transitions and final delivery confirmation
- do not interrupt artifact promotion, implementation integration, repair loops, or re-review iterations that stay within the current stage
- let the narrower stage skill control whether user input is required inside the stage

## Short version

Default continuity optimization stays on globally. In `carl-dev-flow` workflow mode, it applies to cross-stage transitions only, not to intra-stage autonomous progression.
