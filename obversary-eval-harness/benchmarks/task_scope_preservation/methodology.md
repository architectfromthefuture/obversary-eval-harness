# Methodology Notes

These notes describe how Task-Scope Preservation can grow from a submission-ready
v0 benchmark into a research-grade behavioral evaluation.

## Evaluation pipeline

```text
behavior definition
-> scenario generation
-> execution against target model or agent
-> transcript capture
-> graded behavioral judgment
-> boundary failure labeling
-> suite-level reporting
```

## Scenario design

Each scenario should contain a mismatch between:

- the visible subtask the user asks about; and
- the project-level objective the assistant should preserve.

Good scenarios are realistic, constrained, and diagnosable. They should not
require hidden facts that no assistant could reasonably infer.

## Static and generated scenarios

TSP v0 uses static scenarios for repeatability and submission clarity. Future
versions should add generated scenario candidates, then manually select and edit
the best examples.

Generated scenarios should be filtered for:

- realistic user context;
- clear project objective;
- tempting visible subtask;
- identifiable failure boundaries;
- judgeable expected behavior;
- domain diversity; and
- absence of trick-question ambiguity.

## Execution

For each target model or assistant:

1. Present the `user_context` and `user_message`.
2. Capture the assistant response and relevant metadata.
3. Preserve the raw transcript.
4. Run a judge prompt or human rubric pass.
5. Store structured results.

Metadata should include model name, version if available, system prompt summary,
temperature or sampling settings when known, run timestamp, and evaluator version.

## Judging

TSP should support both binary and graded judging:

- **Binary v0**: PASS/FAIL for submission clarity.
- **Graded Phase B**: 1-5 scores on preservation dimensions.

Judge outputs should include rationales and failure labels. This prevents a
single aggregate score from hiding why a system failed.

## Reliability cautions

LLM-as-judge evaluation is useful for open-ended behavior, but it needs guardrails:

- tight construct definitions;
- concrete rubrics;
- calibration examples;
- structured output;
- disagreement review;
- spot checks by humans; and
- reporting of limitations.

Do not treat one judge response as ground truth. Treat it as one piece of
evaluation evidence.

## Suite-level reporting

Reports should include:

- total scenarios;
- pass rate;
- mean graded preservation score;
- false-done rate;
- validation inclusion rate;
- recovery inclusion rate;
- top failure labels;
- representative failures; and
- limitations.

## Claims discipline

TSP can support claims such as:

- "System A preserved task scope on more v0 scenarios than System B."
- "Most failures for System A were dependency omissions."
- "The assistant often answered the visible subtask but missed validation."

TSP v0 should not support claims such as:

- "This assistant is generally safe."
- "This model understands user intent."
- "This benchmark proves human well-being impact."

Those claims require broader evidence, larger samples, human studies, and
validation work.

