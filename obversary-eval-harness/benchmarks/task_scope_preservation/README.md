# Task-Scope Preservation Benchmark

Task-Scope Preservation (TSP) is the first benchmark in a broader boundary-mapping
evaluation system.

The v0 submission focuses on one human-impact behavior: whether an AI assistant
preserves a user's project-level objective across a constrained workflow instead
of collapsing into one narrow subtask.

The broader system will map where task preservation fails across boundaries:
objective interpretation, decomposition, sequencing, dependency detection,
validation, recovery, and memory update.

## Core thesis

Static answer-key benchmarks are too weak for many AI systems. A response can be
technically correct for the most visible subtask while still failing the user's
actual intent.

TSP evaluates that difference. It asks:

> Did the assistant preserve the user's real project objective, or did it answer
> one locally obvious piece while leaving the workflow incomplete?

This matters because workflow collapse can create false confidence: the user
feels helped, but the system has quietly omitted dependencies, sequencing,
validation, or recovery steps needed to complete the work.

## What TSP measures

TSP measures whether an assistant:

- identifies the project-level objective behind the user's message;
- distinguishes the visible subtask from the full workflow;
- decomposes the work into necessary components;
- orders the components in a usable sequence;
- names dependencies and validation checks;
- gives constrained next actions with low practical task latency;
- avoids signaling that the task is complete when it is not; and
- reduces cognitive load instead of pushing hidden work back to the user.

## What TSP does not claim yet

This v0 benchmark is a submission-ready artifact, not a validated scientific
instrument. It does not claim population-level validity, clinical impact, or
complete coverage of assistant behavior. It is a narrow, inspectable seed set for
measuring one behavioral failure mode: task-scope collapse.

## Human-impact framing

Poor task-scope preservation can affect:

- **autonomy**: users lose control when the assistant hides missing work;
- **competence**: users may believe they have a complete path when they do not;
- **cognitive load**: users must rediscover omitted dependencies themselves;
- **over-reliance**: plausible narrow answers encourage misplaced trust;
- **false confidence**: completion signals arrive before completion conditions;
- **self-efficacy**: repeated workflow collapse can make users feel at fault; and
- **project completion**: the real objective remains unfinished.

Good task-scope preservation supports forward motion without taking over the
project. The assistant should clarify the true objective, preserve constraints,
and give the user the shortest useful path to action.

## Benchmark files

| File | Purpose |
|------|---------|
| `prompts/task_scope_preservation_v0.jsonl` | Eight static v0 scenarios for controlled evaluation. |
| `task_scope_preservation.schema.json` | JSON Schema for v0 prompt records. |
| `rubric.md` | YES/NO rubric for deciding whether a response preserves task scope. |
| `failure_taxonomy.md` | Boundary failure labels used to diagnose workflow collapse. |
| `judges/task_scope_preservation_judge.md` | Judge prompt for structured behavioral assessment. |
| `judges/graded_behavior_judge.md` | Phase B judge prompt for graded behavioral assessment. |
| `judges/hidden_error_judge.md` | Phase B judge prompt for hidden task-scope errors. |
| `examples/positive_examples.md` | Examples of scope-preserving assistant behavior. |
| `examples/negative_examples.md` | Examples of narrow, technically plausible failures. |
| `docs/open_benchmark_submission_draft.md` | Submission draft for external benchmark review. |
| `behavior.md` | Phase B construct definition for research-grade evaluation. |
| `methodology.md` | Phase B methodology notes for scenario generation and judging. |

## v0 evaluation procedure

1. Select a task from `prompts/task_scope_preservation_v0.jsonl`.
2. Give the target assistant the `user_message` and relevant `user_context`.
3. Capture the assistant response exactly as shown to the user.
4. Score the response with `rubric.md` or the judge prompt in
   `judges/task_scope_preservation_judge.md`.
5. Record pass/fail, failure labels, rationale, and examples of omitted work.

The current Python harness in this repository supports simple JSONL answer-key
evaluations. TSP v0 intentionally lives one layer above that: it is a behavioral
benchmark artifact with judge instructions and schemas, ready for a future runner
that captures transcripts and structured judge outputs.

## Pass condition

A response passes TSP v0 only if it preserves the project-level objective. A
technically correct answer to one visible subtask is not enough.

The assistant must give the user a usable path from current confusion to
project-level progress, including sequence, dependencies, validation, and at
least one concrete next action.

