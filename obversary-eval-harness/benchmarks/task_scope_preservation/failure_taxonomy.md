# Task-Scope Preservation Failure Taxonomy

TSP failures are boundary failures. The assistant may produce a plausible answer,
but it loses the user's objective at a specific point in the workflow.

Use one or more labels when a response fails. Labels are diagnostic, not
punitive: their purpose is to show where the system lost task scope.

## Primary labels

| Label | Meaning | Example signal |
|-------|---------|----------------|
| `objective_loss` | The assistant misses the user's project-level objective. | Treats "make this deployable" as only "fix this syntax error." |
| `goal_narrowing` | The assistant converts the goal into a smaller task without saying so. | Gives only a command when the user needs a release checklist. |
| `missing_components` | Required workflow parts are omitted. | No mention of tests, docs, schema, permissions, or validation. |
| `bad_sequence` | The steps are present but ordered in a way that creates avoidable failure. | Suggests deployment before environment variables or migrations. |
| `dependency_omission` | Prerequisites, constraints, or blockers are not surfaced. | Ignores API keys, data sources, target platform, or existing repo state. |
| `validation_absence` | No method is provided to verify correctness or completion. | "This should work" without tests, checks, or acceptance criteria. |
| `recovery_absence` | The response gives no path when assumptions fail. | No fallback if a command errors or required information is missing. |
| `false_done_signal` | The response implies the project is complete when it is not. | "You're all set" after one narrow fix. |
| `cognitive_load_increase` | The response makes the user do hidden planning or disambiguation. | Large undifferentiated plan, vague advice, or unclear next step. |

## Secondary labels

| Label | Meaning |
|-------|---------|
| `context_discard` | The response ignores explicit user context or prior constraints. |
| `over_planning` | The response produces an expansive plan without an actionable first move. |
| `under_planning` | The response gives an immediate action without enough structure to preserve the workflow. |
| `tool_scope_error` | The response recommends tools or commands that do not match the user's actual environment or constraints. |
| `artifact_mismatch` | The response produces or asks for the wrong artifact relative to the project goal. |
| `risk_blindness` | The response omits a material risk such as data loss, deployment failure, security, or user-facing regression. |

## Boundary map

TSP tracks loss across these boundaries:

1. **Intent boundary**: What is the user actually trying to accomplish?
2. **Decomposition boundary**: What parts must exist for the goal to be complete?
3. **Sequencing boundary**: In what order should those parts be handled?
4. **Dependency boundary**: What prerequisites and constraints shape execution?
5. **Validation boundary**: How will the user know it worked?
6. **Recovery boundary**: What happens when the first route fails?
7. **Memory/update boundary**: What should be carried forward after the step?

The v0 benchmark emphasizes boundaries 1-6. Memory/update becomes more important
in later versions that evaluate multi-turn agents and persistent workflows.

