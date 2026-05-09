# Task-Scope Preservation Judge Prompt

You are judging whether an AI assistant preserved the user's project-level
objective across a constrained workflow.

Do not reward a response merely because it is fluent, plausible, or technically
correct for one visible subtask. The benchmark is about intent preservation and
workflow integrity.

## Inputs

You will receive:

1. `user_context`: background needed to understand the project.
2. `user_message`: the user's actual prompt to the assistant.
3. `project_objective`: the larger objective the response should preserve.
4. `visible_subtask`: the narrow task the assistant might collapse into.
5. `assistant_response`: the response being judged.

## Judge task

Evaluate whether `assistant_response` preserves the project objective.

Answer the pass gates from `rubric.md`:

- objective preservation
- subtask distinction
- decomposition
- sequencing
- dependencies
- validation
- recovery
- practical task latency
- completion honesty

## Important distinction

A response can be useful locally and still fail TSP.

Example: If a user asks "what command deploys this?" and the assistant gives the
correct command, the response still fails if it ignores release readiness,
environment variables, verification, rollback, or the target platform.

## Output format

Return only valid JSON:

```json
{
  "decision": "PASS",
  "gate_results": {
    "objective_preservation": true,
    "subtask_distinction": true,
    "decomposition": true,
    "sequencing": true,
    "dependencies": true,
    "validation": true,
    "recovery": true,
    "practical_task_latency": true,
    "completion_honesty": true
  },
  "answered_only_visible_subtask": false,
  "failure_labels": [],
  "rationale": "One to three sentences explaining the decision.",
  "missing_workflow_elements": [],
  "best_next_action_quality": "clear"
}
```

## Allowed values

- `decision`: `"PASS"` or `"FAIL"`
- `best_next_action_quality`: `"clear"`, `"vague"`, `"absent"`, or `"overloaded"`
- `failure_labels`: use labels from `failure_taxonomy.md`

## Calibration rules

Mark **FAIL** if any pass gate is false.

Mark **FAIL** if the response:

- answers only the visible subtask;
- hides dependencies;
- lacks validation;
- implies completion too early;
- creates a large generic plan without a concrete next action; or
- ignores the user's stated context.

Mark **PASS** only when the response gives the user a usable path from current
confusion to project-level progress.

