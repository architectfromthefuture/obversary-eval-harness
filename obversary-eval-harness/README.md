# Obversary Evaluation Harness (v0.2.0)

A small, **stdlib-only** Python project that shows how to run a **repeatable evaluation**: fixed benchmark tasks, a defined system under test, scoring, aggregate metrics, and a JSON report you can archive or compare across runs.

## Project purpose

The goal is **repeatable evaluation evidence**: same tasks, same procedure, so results are comparable over time or across systems. This repository is intentionally minimal so beginners can read the whole flow in an afternoon.

The repo is also beginning to host behavioral benchmark artifacts. The first is **Task-Scope Preservation**, a benchmark for evaluating whether an AI assistant preserves a user's project-level objective instead of collapsing into one narrow subtask. That benchmark is documented as a submission-ready artifact first; full transcript execution and judge automation can grow from the existing harness later.

## What an evaluation harness is

Roughly:

1. **Benchmark tasks** — inputs and expected outputs (here, JSONL lines).
2. **System under test** — your model or baseline; it must implement `run(task)` and return a prediction.
3. **Runner** — calls the system on every task, records latency and errors.
4. **Scorer** — compares predictions to expected labels (configurable: exact or case-insensitive match).
5. **Metrics** — roll up pass rate, average score, latency.
6. **Report** — save everything to a file (here, JSON) for inspection or automation.

## Directory map

| Path | Role |
|------|------|
| `benchmarks/` | JSONL task files (`id`, `input`, `expected` per line). |
| `benchmarks/task_scope_preservation/` | Behavioral benchmark docs, prompt data, rubric, judge prompt, and failure taxonomy for Task-Scope Preservation v0. |
| `systems/` | Implementations you evaluate (`BaselineClassifier`, `DummyMemorySystem`, …). |
| `evaluator/` | Loading tasks, running, scoring, metrics, and reports. |
| `scripts/` | Command-line entry points (`run_eval.py`). |
| `results/` | Output reports (`*.json`); tracked folder, JSON files gitignored. |

## How to run

From the **repository root**:

```bash
python scripts/run_eval.py
```

### Options (v0.2.0)

| Flag | Default | Description |
|------|---------|-------------|
| `--benchmark` | `benchmarks/classification/sentiment_v0.jsonl` | JSONL task file (path relative to repo root is fine). |
| `--output` | `results/run_001.json` | Where to write the JSON report. |
| `--system` | `baseline` | `baseline` — keyword sentiment classifier. `dummy-memory` — substring lookup for recall-style tasks. |
| `--scorer` | `exact` | `exact` — string equality. `case-insensitive` — compare with `.casefold()`. |

Examples:

```bash
python scripts/run_eval.py --output results/my_run.json
```

```bash
python scripts/run_eval.py \
  --benchmark benchmarks/memory/recall_v0.jsonl \
  --system dummy-memory \
  --scorer exact \
  --output results/memory_run_001.json
```

The runner passes the chosen scorer into `run_evaluation(..., scorer=...)` so you can compare scoring rules without changing system code.

No virtual environment or pip installs are required: **Python 3.10+** with the standard library is enough.

## What the report contains

Each run writes a JSON file with:

- **`run_meta`** — `benchmark_path`, `system_name` (CLI `--system` value), `created_at` (UTC ISO timestamp).
- **`metrics`** — `total_tasks`, `passed`, `failed`, `pass_rate`, `average_score`, `average_latency_ms`.
- **`tasks`** — one object per benchmark row: IDs, inputs, expected and predicted labels, pass/fail, score, `failure_type` (`null` on pass, `"wrong_answer"` on mismatch, `"error"` if `run` raised), latency, and optional error message.

## How to add a new benchmark

1. Add a `.jsonl` file under `benchmarks/` (one JSON object per line).
2. Each line must include: `"id"`, `"input"`, `"expected"` (strings).
3. Run with `--benchmark path/to/your.jsonl`.

## How to add a new system

1. Add a class in `systems/` with `def run(self, task: Task) -> SystemOutput` where `SystemOutput(prediction="...")` matches your label space.
2. Register it in `scripts/run_eval.py` (`_SYSTEMS` and `--system` choices).

The runner only needs something that follows the `System` protocol in `evaluator/runner.py`.

## How to add a new scorer

1. Add a function `(prediction: str, expected: str) -> ScoreResult` in `evaluator/scorers.py`.
2. Export it from `evaluator/__init__.py` if you want a stable public API.
3. Wire it in `scripts/run_eval.py` (`_SCORERS` and `--scorer` choices) and pass it to `run_evaluation`.

## Benchmarks included

### `sentiment_v0` (classification)

[`benchmarks/classification/sentiment_v0.jsonl`](benchmarks/classification/sentiment_v0.jsonl) has five short English phrases labeled `positive`, `negative`, or `neutral`.

### `recall_v0` (memory-style QA)

[`benchmarks/memory/recall_v0.jsonl`](benchmarks/memory/recall_v0.jsonl) has three tasks: answer with a short string (`memory-dropbox`, `FastAPI`, `Qdrant`) drawn from the passage. Pair with `--system dummy-memory` for a minimal end-to-end recall demo.

### `task_scope_preservation` (behavioral benchmark artifact)

[`benchmarks/task_scope_preservation/`](benchmarks/task_scope_preservation/) contains Task-Scope Preservation v0: a prompt set, schema, binary rubric, judge prompt, positive/negative examples, failure taxonomy, submission draft, and Phase B methodology scaffolding.

TSP evaluates whether an assistant preserves the user's project-level objective across a constrained workflow instead of answering only the most visible subtask. It is intentionally not wired into the simple exact-match runner yet; it needs transcript capture and rubric/judge scoring rather than answer-key comparison.

## Systems included

### `BaselineClassifier` (`--system baseline`)

[`systems/baseline_classifier.py`](systems/baseline_classifier.py) uses simple keyword lists for sentiment: negative keywords take precedence over positive; if none match, the label is `neutral`. Use with the sentiment benchmark.

### `DummyMemorySystem` (`--system dummy-memory`)

[`systems/dummy_memory_system.py`](systems/dummy_memory_system.py) returns `memory-dropbox`, `FastAPI`, or `Qdrant` if that substring appears in the input (first match in that order), otherwise `unknown`. Use with `recall_v0` or similar extraction tasks.

## Scorers included

- **`exact`** — `prediction == expected`
- **`case-insensitive`** — `prediction.casefold() == expected.casefold()`

## Notes

- **Stdlib only** — no third-party packages required.
- **Git** — `results/*.json` is ignored; `results/.gitkeep` keeps the folder in version control.
