---
name: carl-dev-flow-implementation
description: Run the development-execution stage where Sisyphus decomposes implementation into fine-grained tasks, delegates coding work, and integrates results against the agreed requirements and technical spec.
version: 1.3.0
compatibility: opencode
license: CC-BY-4.0
metadata:
  audience: individual-developer
  domain: implementation
---

## Purpose

Use this skill after requirements and technical direction are aligned and the work is ready to move into coding execution.

This skill is the authoritative source for the detailed procedure of the `development-execution` stage inside the Sisyphus and Hephaestus workflow family.

For the shortest Chinese invocation form, see `templates/minimal-zh.md`.

## Core model

`Sisyphus` is the master agent for this stage.

Sub-agents do the focused implementation work.
`Hephaestus` reviews integrated changes in parallel, challenges drift from the agreed documents, and helps prepare the codebase for the next review stage.
This skill is about turning agreed documents into well-scoped execution units and keeping the resulting code integrated and reviewable.

## Workflow

1. Confirm that requirements final and technical spec final exist, or that the user explicitly chose to proceed with an accepted shortcut.
2. Break the implementation into fine-grained tasks using feature span, module boundaries, coupling, and verification needs.
3. Order tasks by dependency and execution risk.
4. Delegate concrete coding tasks to sub-agents with clear scope and acceptance criteria.
5. Integrate the resulting changes into a coherent working state.
6. Verify the integrated result against requirements and technical spec.
7. Prepare the codebase for recursive improvement rather than treating first-pass implementation as done.

## Task-splitting rules

- split by function or module boundary when possible
- keep each task small enough to review independently
- separate foundational work from dependent work
- pair implementation with relevant verification work
- avoid mixing unrelated concerns into one delegated task

## Delegation contract

Every delegated implementation task should state:

- objective
- exact files or modules in scope
- constraints from requirements and technical spec
- acceptance criteria
- required verification
- forbidden shortcuts

## Exit criteria

Do not declare this stage complete until:

- delegated work is integrated
- the code matches the agreed documents closely enough for review
- verification has been run for the changed scope
- the result is ready to enter `recursive-improvement`
- if a sub-agent task fails while others succeed, integrate the successful parts, record the failure explicitly in the task plan, and re-delegate the failed task before declaring integration complete
- do not silently drop failed task results or retry without documenting what went wrong


## Artifact location

Store implementation artifacts in `.carl/implementation/`:

- `.carl/implementation/task-plan.md` — task breakdown and delegation records

## Pre-edit checklist

Before any source code edit, verify:

- requirements document exists and is `final` or user-approved
- technical spec exists and is `final` or user-approved
- if neither exists, the user has explicitly chosen a shortcut and this is recorded in `.carl/state.md`


## Execution modes

Each implementation task must declare one of these execution modes:

- **tdd-first**: write a failing test for the expected behavior, implement until the test passes, then refactor. Use this mode for new behavior or when test boundaries are clear.
- **characterization-first**: write tests that capture existing behavior before modifying it. Use this mode for brownfield work, regression-prone areas, or when the current behavior is poorly documented.
- **direct**: implement without writing tests first. Use this mode only when tests are impossible or not meaningful for the change (e.g., configuration changes, pure wiring). Record the reason for choosing direct mode.

### TDD loop

When using `tdd-first` or `characterization-first`:

1. Pick one slice or behavior to prove.
2. Write a test that fails (red).
3. Write the minimum code to pass (green).
4. Refactor only after the test passes.
5. Move to the next slice or behavior.

### Anti-patterns

- Do not implement an entire horizontal layer before testing any vertical behavior.
- Do not write tests after all implementation is done and call it TDD.
- Do not test implementation details (private methods, internal state) when behavior tests are possible.

## Slice decomposition

Break finalized requirements and technical spec into independently deliverable vertical slices.

### Slice definition

Each slice must deliver a user-visible or system-observable behavior. A slice cuts through all necessary layers (UI, logic, data, infrastructure) rather than completing one layer at a time.

### Slice attributes

For each slice, define:

- title
- behavior delivered (one sentence describing the observable outcome)
- requirements and spec references
- dependencies on other slices
- expected verification approach

Store slice breakdowns in `.carl/implementation/slices.md` using the template in `templates/slices.md`.

### Ordering

Order slices by:

1. dependency (blocked slices come after their blockers)
2. risk (uncertain or complex slices earlier)
3. value (high-value behaviors earlier when dependencies allow)

## Bug-fix adaptation

When this stage is entered as part of a bug-fix workflow (routed from `carl-dev-flow-bugfix`):

- Apply the **minimal fix principle**: change only what is necessary to resolve the defect. Do not refactor, improve, or extend nearby code.
- Before applying the fix, establish a **regression baseline**: record which tests pass, which behaviors are correct, and what observable state exists before the change.
- Task-splitting favors isolation: separate the fix itself from any necessary test additions.
- Exit criteria add: regression baseline recorded, fix scope matches root cause analysis, no unrelated changes included.

## Default behavior when loaded

The agent should:

1. Confirm that requirements final and technical spec final exist or that an accepted shortcut is in effect.
2. Assess current implementation progress against the task breakdown.
3. Identify the next task to delegate or integrate.
4. Drive execution forward rather than stopping at planning.
