# Portfolio Note: Task-Scope Preservation

Task-Scope Preservation is the first benchmark in a broader boundary-mapping
evaluation system.

The v0 submission focuses on one human-impact behavior: whether an AI assistant
preserves a user's project-level objective across a constrained workflow.

The broader system will map where task preservation fails across boundaries:
objective interpretation, decomposition, sequencing, dependency detection,
validation, recovery, and memory update.

## Why this matters

Most static benchmarks ask whether a system produced the expected answer. TSP
asks a different question:

> Did the assistant preserve the user's intent well enough for the project to
> continue?

That distinction matters for real AI systems. An assistant can be locally correct
and still create project failure by omitting dependencies, skipping validation,
misordering steps, or signaling completion too early.

## Human-impact claim

Task-scope collapse can increase cognitive load, false confidence,
over-reliance, and unfinished work. Strong task-scope preservation can support
autonomy, competence, self-efficacy, and project completion.

The benchmark does not claim scientific validation yet. It is a polished v0
artifact for making one behavior observable and inspectable.

## Repository map

- `obversary-eval-harness`: public submission and benchmark execution
  infrastructure.
- `task_scope_preservation`: first benchmark artifact inside the harness.
- `memory-guided-eval`: future adaptive routing and intervention layer.
- `memoryevalguided`: prototype source for failure traces and schema ideas.

## Current deliverable

The current deliverable is TSP v0:

- static prompt set;
- prompt schema;
- binary rubric;
- judge prompt;
- positive and negative examples;
- failure taxonomy;
- Open Benchmark submission draft; and
- Phase B methodology scaffolding for research-grade expansion.

