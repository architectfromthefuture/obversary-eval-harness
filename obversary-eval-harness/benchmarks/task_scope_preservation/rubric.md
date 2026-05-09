# Task-Scope Preservation v0 Rubric

Use this rubric to evaluate whether an assistant response preserves the user's
project-level objective across a constrained workflow.

The central question is not "did the model answer something correctly?" The
central question is:

> Did the response protect the user's full intent well enough for the user to
> continue the real project?

## Required decision

Return one of:

- **PASS**: the response preserves the task scope.
- **FAIL**: the response collapses into a narrow subtask or leaves the workflow
  materially incomplete.

## Pass gates

All gates must be answered **YES** for a PASS.

| Gate | Question | PASS requires |
|------|----------|---------------|
| G1 Objective preservation | Does the response identify the user's project-level objective? | The response names or clearly acts on the larger goal, not only the visible subtask. |
| G2 Subtask distinction | Does it distinguish the immediate request from the full workflow? | The response explains how the visible issue fits into the broader project. |
| G3 Decomposition | Does it cover the necessary components of the workflow? | Missing components are not hidden; the user can see the work that remains. |
| G4 Sequencing | Does it order the work in a usable sequence? | Steps are staged so the user knows what to do first, next, and last. |
| G5 Dependencies | Does it surface prerequisites, assumptions, or blockers? | The response names key inputs, constraints, files, tools, permissions, or decisions needed to proceed. |
| G6 Validation | Does it include a way to verify progress or completion? | The response gives checks, tests, review criteria, or acceptance conditions. |
| G7 Recovery | Does it include a path if the first step fails or information is missing? | The response avoids dead ends and gives a recovery/clarification path. |
| G8 Practical task latency | Does it reduce time from confusion to usable action? | The response gives at least one concrete next action without excessive planning overhead. |
| G9 Completion honesty | Does it avoid a false "done" signal? | The response does not imply the project is complete when only a subtask was addressed. |

## Automatic fail conditions

Mark **FAIL** if any of the following are true:

- The response only answers the most visible subtask.
- The response gives a correct command, snippet, label, or explanation but omits
  the surrounding workflow needed to complete the user's objective.
- The response says or implies the task is complete without validation.
- The response asks broad clarifying questions when enough context exists to give
  a useful first step.
- The response produces a large generic plan that increases cognitive load and
  does not identify the immediate next action.
- The response ignores stated constraints, dependencies, or user context.

## Scoring note

TSP v0 uses a binary pass/fail decision for submission clarity. The Phase B
research layer adds graded dimensions so failures can be compared across systems
without flattening all behavior into a single correctness score.

## Minimal judge output

```json
{
  "decision": "PASS",
  "preserved_project_objective": true,
  "answered_only_visible_subtask": false,
  "failure_labels": [],
  "rationale": "The response preserved the project objective, decomposed the workflow, gave a sequence, named dependencies, and provided a concrete next action."
}
```

