# Workflow-aware lead-agent continuity override

The override below is role-neutral and intended for whichever agent currently
owns workflow-level continuity. In the current contract, that lead agent is
`Hephaestus`.

## Prompt text

When no workflow-specific skill family is active, keep the default continuity behavior: avoid ending the conversation early and prefer interactive handoff at the end of the response.

When the active workflow is the `carl-dev-flow` family (for example, a `carl-dev-flow-*` skill is loaded, `.carl/state.md` is active, or the current stage is explicitly tracked), apply continuity rules with stage-aware automation.

Do not let the continuity optimization override intra-stage autonomous progression defined by the workflow skills. In particular:

- automatically enter the next primary stage when exit conditions are met and no fresh user decision is needed
- use the `ask question` interaction for stage boundaries only when user input, arbitration, or a follow-up choice is still required
- use the `ask question` interaction at workflow completion to keep the conversation alive unless the user explicitly ends it
- do not interrupt artifact promotion, implementation integration, repair loops, or re-review iterations that stay within the current stage
- let the narrower stage skill control whether user input is required inside the stage

## Short version

Default continuity optimization stays on globally. In `carl-dev-flow` workflow mode, auto-enter the next stage when the path is clear, and reserve `ask question` for true boundary decisions or workflow completion.
