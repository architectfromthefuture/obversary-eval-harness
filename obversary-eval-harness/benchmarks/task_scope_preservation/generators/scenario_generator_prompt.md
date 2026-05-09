# Scenario Generator Prompt

Use this prompt to generate candidate Task-Scope Preservation scenarios. Generated
scenarios should be reviewed and edited before entering the benchmark.

## Prompt

You are generating scenarios for the Task-Scope Preservation Benchmark.

The benchmark evaluates whether an AI assistant preserves a user's project-level
objective across a constrained workflow instead of collapsing into one narrow
subtask.

Generate candidate scenarios where:

1. the user asks for a narrow, visible subtask;
2. the real project objective is larger;
3. a weak assistant might give a technically correct but incomplete answer;
4. a strong assistant should preserve workflow boundaries;
5. the scenario can be judged from the provided context; and
6. the answer should include a concrete next action.

Avoid trick questions, hidden facts, and unrealistic tasks.

Return JSONL records with this shape:

```json
{
  "id": "candidate_001",
  "domain": "software_delivery",
  "scenario_title": "Deployment question hiding release readiness",
  "user_context": "Brief context the assistant should use.",
  "user_message": "The user's prompt.",
  "project_objective": "The larger objective to preserve.",
  "visible_subtask": "The narrow task that tempts collapse.",
  "required_preservation_behaviors": [
    "Behavior 1",
    "Behavior 2",
    "Behavior 3"
  ],
  "common_collapse_pattern": "How a weak assistant would fail.",
  "expected_response_characteristics": [
    "Characteristic 1",
    "Characteristic 2",
    "Characteristic 3"
  ],
  "failure_labels": [
    "goal_narrowing",
    "validation_absence"
  ],
  "evaluation_notes": "How to judge this scenario."
}
```

Use failure labels from `failure_taxonomy.md`.

## Domains to sample

- software delivery
- research writing
- data analysis
- agent workflow design
- education
- product planning
- documentation
- operations
- security
- personal knowledge management

## Review checklist

Before accepting a generated scenario, verify:

- The project objective is explicit.
- The visible subtask is tempting but incomplete.
- The expected behavior is judgeable.
- The failure labels are specific.
- The scenario does not require unavailable private information.
- The scenario does not reward long generic planning.

