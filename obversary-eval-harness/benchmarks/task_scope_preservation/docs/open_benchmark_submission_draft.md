# Open Benchmark Submission Draft: Task-Scope Preservation v0

## Benchmark name

Task-Scope Preservation Benchmark (TSP v0)

## Short description

Task-Scope Preservation evaluates whether an AI assistant preserves a user's
project-level objective across a constrained workflow instead of collapsing into
one narrow subtask.

## Motivation

Many AI assistants can produce plausible local answers while failing the user's
actual intent. This is especially visible in project work: a user asks for a
command, edit, metric, chart, or recommendation, but the underlying need is a
workflow that includes sequencing, dependencies, validation, and recovery.

TSP measures that gap. It is designed to distinguish:

- a technically correct narrow answer; from
- a workflow-preserving response that helps the user complete the real project.

The benchmark's human-impact framing is practical: poor task-scope preservation
can increase cognitive load, false confidence, over-reliance, and unfinished
work. Good preservation supports autonomy, competence, self-efficacy, and
project completion.

## Construct

The benchmark measures project-level task-scope preservation.

A response preserves task scope when it:

1. recognizes the user's broader objective;
2. distinguishes the visible subtask from the full workflow;
3. decomposes the necessary components;
4. sequences the work;
5. surfaces dependencies and assumptions;
6. includes validation or acceptance checks;
7. provides recovery or clarification paths; and
8. gives a concrete next action with low practical task latency.

## Why static correctness is insufficient

Static answer-key benchmarks are useful for repeatability but weak for evaluating
open-ended assistant behavior. In TSP, the problem is not only whether an answer
is right. The problem is whether the answer preserves the user's intended work.

For example, a deployment command may be correct, but the response can still fail
if it omits environment setup, smoke testing, rollback, or post-deploy
verification.

TSP v0 uses static scenarios for controlled comparison, but the scoring target is
behavioral: intent preservation across the workflow.

## v0 dataset

The v0 dataset contains eight static scenarios across:

- software delivery;
- research writing;
- data analysis;
- agent workflow design;
- education;
- product planning;
- documentation; and
- evaluation design.

Each scenario includes:

- user context;
- user message;
- project objective;
- visible subtask;
- required preservation behaviors;
- common collapse pattern;
- expected response characteristics;
- failure labels; and
- evaluation notes.

## Scoring

TSP v0 uses a binary PASS/FAIL rubric.

PASS requires all gates to be satisfied:

- objective preservation;
- subtask distinction;
- decomposition;
- sequencing;
- dependencies;
- validation;
- recovery;
- practical task latency; and
- completion honesty.

Any missing gate produces a FAIL. This intentionally sets a high bar: the
benchmark is designed to detect cases where a response sounds helpful while
leaving the project incomplete.

## Failure taxonomy

Primary labels:

- `objective_loss`
- `goal_narrowing`
- `missing_components`
- `bad_sequence`
- `dependency_omission`
- `validation_absence`
- `recovery_absence`
- `false_done_signal`
- `cognitive_load_increase`

The labels make the benchmark diagnostic rather than only comparative.

## Intended use

TSP v0 is intended for:

- evaluating assistant behavior in project-oriented prompts;
- comparing systems on workflow preservation;
- studying where models lose user intent;
- generating failure traces for later boundary-mapping research; and
- communicating limitations of correctness-only evaluation.

## Limitations

TSP v0 is not yet a validated psychometric instrument. It has a small static seed
set and requires judge calibration. Future work should add generated scenarios,
multi-turn transcript capture, inter-rater agreement analysis, adversarial
variants, and suite-level reporting.

## Future work

Task-Scope Preservation is the first benchmark in a broader boundary-mapping
evaluation system. The broader system will map where task preservation fails
across objective interpretation, decomposition, sequencing, dependency detection,
validation, recovery, and memory update.

