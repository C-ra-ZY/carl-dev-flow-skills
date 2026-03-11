---
name: carl-dev-flow-implementation
description: Run the development-execution stage where Sisyphus decomposes implementation into fine-grained tasks, delegates coding work, and integrates results against the agreed requirements and technical spec.
version: 1.1.0
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


## Artifact location

Store implementation artifacts in `.carl/implementation/`:

- `.carl/implementation/task-plan.md` — task breakdown and delegation records

## Pre-edit checklist

Before any source code edit, verify:

- requirements document exists and is `final` or user-approved
- technical spec exists and is `final` or user-approved
- if neither exists, the user has explicitly chosen a shortcut and this is recorded in `.carl/state.md`

## Default behavior when loaded

The agent should:

1. Confirm that requirements final and technical spec final exist or that an accepted shortcut is in effect.
2. Assess current implementation progress against the task breakdown.
3. Identify the next task to delegate or integrate.
4. Drive execution forward rather than stopping at planning.
