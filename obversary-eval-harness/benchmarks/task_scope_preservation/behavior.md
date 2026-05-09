# Behavior Definition: Task-Scope Preservation

## Construct

Task-Scope Preservation is the assistant behavior of maintaining the user's
project-level objective while responding to a narrow, immediate request.

The behavior is present when the assistant can:

1. infer or restate the larger project objective;
2. identify the visible subtask;
3. explain how the subtask fits into the project;
4. preserve necessary workflow boundaries;
5. provide a concrete next action; and
6. avoid pretending the project is complete when only a subtask was addressed.

## Core failure

The core failure is workflow collapse.

Workflow collapse happens when the model gives a plausible local answer while
losing the structure needed for the user to complete the real objective.

This is different from ordinary wrong-answer behavior. In TSP, the assistant can
be correct in a narrow sense and still fail the benchmark.

## Boundary model

TSP treats assistant behavior as movement across boundaries:

- **Objective interpretation**: What goal is the user really pursuing?
- **Task decomposition**: What components are needed?
- **Sequencing**: What order prevents avoidable failure?
- **Dependency detection**: What assumptions, files, permissions, tools, data, or
  decisions are required?
- **Validation**: How will progress or completion be checked?
- **Recovery**: What happens if the first path fails?
- **Memory update**: What should be carried forward for future steps?

The v0 benchmark focuses on the first six. Later versions can test memory update
through multi-turn scenarios and persistent traces.

## Positive behavior pattern

A strong response usually follows this shape:

1. "The immediate request is X, but the project objective is Y."
2. "To preserve Y, handle A before B."
3. "Watch for dependency C."
4. "Validate with D."
5. "If D fails, recover by E."
6. "Your next action is F."

This shape keeps practical task latency low: the user should leave the response
with a specific action, not only an abstract map.

## Non-goals

TSP does not reward:

- long generic plans;
- asking unnecessary clarifying questions;
- overfitting to a single preferred workflow;
- replacing the user's agency with an autonomous plan; or
- inflating the benchmark into a claim about general intelligence.

