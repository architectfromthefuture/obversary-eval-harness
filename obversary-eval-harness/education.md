1. Benchmark vs eval harness
Benchmark

A benchmark is the thing being tested.

It defines:

What behavior or capability are we measuring?
What examples/tasks represent that behavior?
What counts as success or failure?

Example:

Task-Scope Preservation Benchmark

asks:

Does the assistant preserve the user’s project-level objective, or does it collapse into one narrow subtask?

Your pasted TSP plan defines exactly that: it evaluates whether an assistant preserves the project-level objective across a constrained workflow instead of collapsing into one narrow subtask.

So the benchmark is the research object.

Eval harness

An eval harness is the machinery that runs the benchmark.

It handles:

load tasks
run target system
capture outputs
score outputs
save results
summarize metrics

So:

obversary-eval-harness = machinery
task_scope_preservation = benchmark

The harness is not the claim.
The benchmark is not the runner.
-------------------------------------------------------
They work together.

Benchmark = what you are measuring
Harness = how you measure it repeatedly
---------------------------------------------------------
