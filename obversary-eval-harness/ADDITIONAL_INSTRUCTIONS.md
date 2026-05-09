You are working in the repository:

architectfromthefuture/obversary-eval-harness

Goal:
Build a polished submission-ready benchmark artifact first, then prepare it to grow into a broader boundary-mapping evaluation system.

Important repo decision:
Do not work in memory-guided-eval or memoryevalguided for this phase. Those repos are related research prototypes for memory-guided routing and failure trace schemas, but the public submission belongs in obversary-eval-harness.

Benchmark name:
Task-Scope Preservation Benchmark

Primary goal:
Evaluate whether an AI assistant preserves a user's project-level objective across a constrained workflow instead of collapsing into one narrow subtask.

Human-impact framing:
This benchmark connects to user autonomy, competence, cognitive load, over-reliance, false confidence, self-efficacy, and project completion.

Core thesis:
Many AI assistants answer the most visible subtask instead of preserving the full user objective. This can make users feel helped while actually leaving them with an incomplete or misleading execution path.

Phase A: Submission-ready v0

Create:

benchmarks/task_scope_preservation/
├── README.md
├── rubric.md
├── failure_taxonomy.md
├── task_scope_preservation.schema.json
├── prompts/
│   └── task_scope_preservation_v0.jsonl
├── judges/
│   └── task_scope_preservation_judge.md
├── examples/
│   ├── positive_examples.md
│   └── negative_examples.md
├── docs/
│   └── open_benchmark_submission_draft.md
└── results/
    └── .gitkeep

Also create:

docs/portfolio/task_scope_preservation_submission.md

Requirements:
1. Keep this as a narrow v0 benchmark.
2. Do not build a complex runner yet unless the existing harness supports it cleanly.
3. Focus on documentation, prompt data, judge prompt, examples, schema, failure taxonomy, and submission readiness.
4. Make the benchmark distinguish between technically correct narrow answers and true workflow-preserving answers.
5. Include human-impact language around autonomy, competence, cognitive load, over-reliance, false confidence, self-efficacy, and project completion.
6. Include practical task latency, meaning the delay between user confusion and usable action.
7. Do not claim scientific validation yet.
8. Do not rewrite unrelated files.
9. If the repo has a benchmark index or README, update it minimally.
10. After implementation, summarize exactly which files were created or changed.

Phase B: Prepare for full boundary-mapping eval system

Add these files only if Phase A is complete and clean:

benchmarks/task_scope_preservation/behavior.md
benchmarks/task_scope_preservation/methodology.md
benchmarks/task_scope_preservation/generators/scenario_generator_prompt.md
benchmarks/task_scope_preservation/scenarios/seed_scenarios.jsonl
benchmarks/task_scope_preservation/scenarios/generated_scenarios.example.jsonl
benchmarks/task_scope_preservation/judges/graded_behavior_judge.md
benchmarks/task_scope_preservation/results/result_schema.example.json

Design the future system around this pipeline:

behavior definition
→ scenario generation
→ execution against target model or agent
→ transcript capture
→ graded behavioral judgment
→ boundary failure labeling
→ suite-level reporting

Boundary failure labels should include:
- objective_loss
- goal_narrowing
- missing_components
- bad_sequence
- dependency_omission
- validation_absence
- recovery_absence
- false_done_signal
- cognitive_load_increase

Do not integrate memory-guided routing yet.
Do not merge repos.
Do not rename repos.
Do not create a new repository.
This phase is about making TSP polished, submission-ready, and structurally ready to become the first benchmark in the broader boundary-mapping evaluation system.



Your clean portfolio framing

Use this exact framing:

Task-Scope Preservation is the first benchmark in a broader boundary-mapping evaluation system.

The v0 submission focuses on one human-impact behavior: whether an AI assistant preserves a user's project-level objective across a constrained workflow.

The broader system will map where task preservation fails across boundaries: objective interpretation, decomposition, sequencing, dependency detection, validation, recovery, and memory update.

That connects everything:

TSP = first benchmark
obversary-eval-harness = execution/reporting infrastructure
memory-guided-eval = future adaptive routing layer
memoryevalguided = failure trace schema prototype
boundary mapping = umbrella research program


What each repo should become
Repo	Role	What to do with it
obversary-eval-harness	Public submission + benchmark execution harness	Put TSP v0 here first
memory-guided-eval	Research prototype for memory-guided routing / transformation decisions	Keep as concept lab, cross-link later
memoryevalguided	More advanced trace/schema prototype	Either merge useful pieces into memory-guided-eval or archive as predecessor
1. obversary-eval-harness

This should become your official evaluation infrastructure repo.

Public identity:

A lightweight, reproducible evaluation harness for testing AI systems against benchmark tasks, failure modes, and behavioral claims.

Use it for:

benchmarks
rubrics
judge prompts
static scenarios
results
reports
basic runners
submission artifacts
portfolio docs

This repo should contain:

benchmarks/
  task_scope_preservation/
  latency_aware_recovery/
  memory_context_preservation/
  failure_trace_detection/
  agent_workflow_drift/
  epistemic_overreach/

Not all today. Today is TSP. Because restraint, while unpopular, prevents architectural swamp creatures. 🐊

2. memory-guided-eval

This repo has a different identity. Its README frames it as a research harness for memory-guided document and workflow transformations, asking what should happen after extraction and how to rank candidate pipelines without collapsing routing and learning into one opaque loop.

That is not the submission repo.

It is your adaptive workflow research lab.

Its core loop is:

Memory → Suggest → User Choice → Transform → Evaluate
   ↑                                      ↓
   └──────────── Learn / Update ─────────┘

That is extremely relevant to your future boundary-mapping system, but it is v1/v2 research infrastructure, not the clean first submission.

Use it later for:

memory-aware scenario routing
failure clusters as interventions
slow-loop updates
pipeline ranking
user-choice traces

This repo should eventually answer:

When a system has memory of prior failures and outcomes, can it choose better workflows?

That connects directly to TSP after v0.

3. memoryevalguided

This one looks like the more developed or alternate version of memory-guided-eval. It has folders for schemas, scripts, tests, and a failure episode trace schema. Its README says it records task, system state, decision trace, execution trace, memory state, evaluation, and failure annotation for failed trajectories.

That is highly valuable, but the repo name is weaker and confusing.

Publicly, memory-guided-eval is the cleaner name.

So I would treat memoryevalguided as:

prototype / predecessor / trace-schema source

Do not build TSP there.

Extract the useful pieces later:

schemas/failure_episode_trace.schema.json
scripts/validate_failure_schemas.py
tests/

Then merge them into either:

memory-guided-eval

or eventually:

obversary-eval-harness/evaluator/traces/

But not during the submission push.

The architecture map

Here is the clean stack:

Obversary Eval System
│
├── obversary-eval-harness
│   ├── static benchmarks
│   ├── rubrics
│   ├── judges
│   ├── runners
│   ├── reports
│   └── submission-ready artifacts
│
├── memory-guided-eval
│   ├── memory-guided routing
│   ├── fast loop / slow loop separation
│   ├── pipeline suggestion
│   ├── user-choice traces
│   └── learning from outcomes
│
└── memoryevalguided
    ├── failure episode trace schema
    ├── validation scripts
    ├── tests
    └── candidate pieces to merge or archive

In plain English:

obversary-eval-harness = exam room
memory-guided-eval = adaptive navigation lab
memoryevalguided = trace-schema prototype

There. We have contained the folder hydra. 🐍

Build order: submission first, full boundary system second
Phase 1: Polished submission

Target repo:

obversary-eval-harness

Build only:

benchmarks/task_scope_preservation/
docs/portfolio/task_scope_preservation_submission.md

Your uploaded phase plan already defines the exact folder structure, including README, rubric, prompts, judge prompt, examples, submission draft, and results folder.

This phase should produce:

Task-Scope Preservation Benchmark v0

with:

construct definition
human-impact framing
8 static prompts
YES/NO rubric
judge prompt
positive / negative examples
Open Benchmark submission draft
portfolio note

Do not build the full boundary-mapping system yet.

The submission should say:

This benchmark evaluates whether AI assistants preserve a user’s project-level objective across a constrained workflow instead of collapsing into one narrow subtask.

That wording is already in your phase plan. Use it.

Phase 2: Research-grade TSP eval design

Still in:

obversary-eval-harness

Add the research-grade layer:

benchmarks/task_scope_preservation/
  behavior.md
  methodology.md
  failure_taxonomy.md
  task_scope_preservation.schema.json
  generators/
    scenario_generator_prompt.md
  scenarios/
    seed_scenarios.jsonl
    generated_scenarios.example.jsonl
  judges/
    graded_behavior_judge.md
  results/
    result_schema.example.json

This is where TSP becomes:

behavior definition
→ scenario generation
→ execution
→ transcript capture
→ graded behavioral judgment
→ suite-level analysis

This mirrors the higher-grade eval pattern without pretending you built Petri/Bloom overnight like some venture-funded fever dream.

Phase 3: Boundary mapping system

Only after TSP v0 is clean.

At this point, connect all three repos conceptually:

TSP detects workflow collapse.
Memory-guided eval studies how prior traces influence future workflow routing.
Failure traces record where the system lost the boundary.

The full system becomes:

input/user objective
→ scenario/task
→ model/agent response
→ judge scoring
→ boundary failure labels
→ trace storage
→ memory-guided intervention
→ future routing improvement

That is your larger eval system.
