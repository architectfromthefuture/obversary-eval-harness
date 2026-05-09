obversary-eval-harness/
│
├── README.md
│
├── benchmarks/
│   ├── classification/
│   │   └── sentiment_v0.jsonl
│   ├── memory/
│   │   └── recall_v0.jsonl
│   └── workflows/
│       └── file_pipeline_v0.jsonl
│
├── systems/
│   ├── baseline_classifier.py
│   ├── dummy_memory_agent.py
│   └── workflow_agent.py
│
├── evaluator/
│   ├── schemas.py
│   ├── task_loader.py
│   ├── runner.py
│   ├── metrics.py
│   ├── scorers.py
│   ├── report.py
│   └── failure_modes.py
│
├── results/
│   └── run_001.json
│
└── scripts/
    └── run_eval.py
The Core Custom Items
1. Task Schema

This defines what a single test looks like.

For a classifier:

{
  "id": "sentiment_001",
  "input": "This product is terrible.",
  "expected": "negative"
}

For a memory benchmark:

{
  "id": "memory_001",
  "setup_event": "Brian saved the project notes under LifeOS.",
  "query": "Where were the project notes saved?",
  "expected": "LifeOS"
}

For an agent workflow:

{
  "id": "workflow_001",
  "goal": "Convert notes.txt into markdown.",
  "expected_artifact": "notes.md"
}

This is custom because you decide what a valid task is.

2. Dataset / Benchmark Tasks

These are the actual examples your system gets tested on.

benchmarks/
  memory/
    recall_tasks.jsonl
  classification/
    sentiment_tasks.jsonl
  grid_reasoning/
    simple_transform_tasks.json

A benchmark task set is basically:

test case 1
test case 2
test case 3
...

Your custom job is deciding:

What examples matter?
What failure cases matter?
What difficulty levels exist?

For your direction, you might create task categories like:

memory recall
event ordering
source attribution
tool-use correctness
grid transformation
workflow completion
3. System Interface

This defines how the harness talks to whatever is being tested.

For a classifier:

prediction = system.predict(input_text)

For an agent:

result = agent.run(goal)

For a memory system:

answer = memory_agent.query(question)

The harness needs a standard contract:

class SystemUnderTest:
    def run(self, task):
        ...

This is custom because different systems behave differently. A classifier returns a label. An agent may return logs, files, tool calls, or a final answer. Naturally, machines refuse to be convenient.

4. Scoring Function

This defines what “good” means.

For exact match:

def exact_match(prediction, expected):
    return prediction == expected

For classification accuracy:

def accuracy(results):
    correct = sum(r["correct"] for r in results)
    return correct / len(results)

For agent workflows:

def artifact_exists(result, expected_artifact):
    return expected_artifact in result["created_files"]

For memory systems, you may score:

correct answer
source cited
no hallucinated source
uses latest event
preserves chronology

This is one of the most important custom pieces.

The score tells the system what reality cares about. Dangerous concept. Humans should try it sometime.

5. Metric Definitions

A metric is the named measurement your report saves.

Examples:

accuracy
exact_match_rate
average_latency
tool_success_rate
memory_recall_score
hallucination_rate
artifact_validity

For your systems, useful custom metrics would be:

Metric	What it measures
exact_match	Did output equal expected answer?
partial_match	Was it close enough?
source_accuracy	Did it cite the right source/event?
chronology_score	Did it preserve event order?
tool_success_rate	Did tool calls complete correctly?
artifact_validity	Did the created file/output meet requirements?
latency_ms	How long did it take?
failure_rate	How often did it crash or refuse?

Metrics are custom because your benchmark decides what behavior matters.

6. Runner Logic

The runner is the part that executes each task.

def run_evaluation(tasks, system, scorer):
    results = []

    for task in tasks:
        prediction = system.run(task)
        score = scorer(prediction, task["expected"])

        results.append({
            "task_id": task["id"],
            "prediction": prediction,
            "expected": task["expected"],
            "score": score,
        })

    return results

The generic structure is reusable.

The custom part is:

How do I prepare each task?
How do I call the system?
What do I capture?
What does failure look like?

For an agent, you might capture:

steps taken
tool calls
files created
errors
final answer
runtime
7. Result Schema

This defines what gets saved after each test.

Example:

{
  "task_id": "memory_001",
  "input": "Where were the notes saved?",
  "expected": "LifeOS",
  "prediction": "They were saved under LifeOS.",
  "score": 1.0,
  "passed": true,
  "latency_ms": 431,
  "metadata": {
    "system": "memory_agent_v1",
    "benchmark": "memory_recall_v0"
  }
}

This matters because later you want to inspect:

What failed?
Why did it fail?
Did it improve after changes?
Was the improvement real?

Without saved results, you are just doing ritualistic Python. Very popular, regrettably.

8. Failure Categories

This is underrated.

Do not only save “wrong.”

Save how it failed.

Example categories:

wrong_answer
missing_source
wrong_source
format_error
timeout
tool_error
hallucination
partial_completion
invalid_artifact

For your memory-first systems, failure categories are especially important:

forgot_event
confused_two_events
used_stale_memory
invented_memory
ignored_source_event
wrong_timestamp_order

This is how you turn evaluation into diagnosis.


You’re now talking about one of the most important layers in real AI work:

A benchmark defines the test.
An evaluation harness runs the test, scores the system, and records what happened.

This is where you stop asking “does my AI seem smart?” and start asking:

“Under controlled conditions, what behavior can this system reliably reproduce?”

Which is annoying, because now the machine demands evidence instead of vibes. Tragic. 🧪

1. What is a benchmark?

A benchmark is a standardized challenge.

It defines:

Inputs
Expected outputs
Rules
Scoring method
Difficulty levels
Failure cases

Examples:

Benchmark type	What it tests
Classification benchmark	Can the model pick the right label?
Regression benchmark	Can the model predict the right number?
RL benchmark	Can the agent maximize reward?
ARC-style benchmark	Can the system infer transformations?
Agent benchmark	Can the agent complete tasks reliably?
Memory benchmark	Can the system recall/use previous events correctly?

So for your world:

benchmark = controlled test environment for intelligence behavior
2. What is an evaluation harness?

The evaluation harness is the machine that runs the benchmark.

It does this:

Load tasks
Run system
Collect outputs
Score outputs
Save results
Generate report

Think of it like:

Benchmark = exam
Evaluation harness = exam proctor + grader + report card
Model/agent = poor little creature being judged
3. Why this matters for your AI map

This puts you in:

AI Systems Architecture
  ↓
Evaluation Infrastructure
  ↓
Agent / Model Behavior Testing
  ↓
Memory-first / Cognitive System Validation

This is a serious layer.

Most people build demos.
You are talking about building measurement infrastructure.

That matters because any real AI system needs to answer:

Did it work?
How well?
Compared to what?
Under what conditions?
Did it fail consistently?
Can we reproduce the result?

Without evaluation, it is just a chatbot wearing a lab coat. 🧠

4. The core architecture

A benchmark/eval harness repo should look like this:

ai-evaluation-harness/
│
├── README.md
│
├── benchmarks/
│   ├── classification/
│   │   └── sample_tasks.jsonl
│   │
│   ├── grid_reasoning/
│   │   └── sample_tasks.json
│   │
│   └── memory/
│       └── memory_recall_tasks.jsonl
│
├── systems/
│   ├── baseline_classifier.py
│   ├── random_agent.py
│   └── rule_based_solver.py
│
├── evaluator/
│   ├── task_loader.py
│   ├── runner.py
│   ├── metrics.py
│   ├── report.py
│   └── schemas.py
│
├── results/
│   └── run_001.json
│
└── scripts/
    └── run_eval.py

Translated into your document model:

TOOLS
  Python
  JSON / CSV
  scoring functions

ARCHITECTURE
  benchmark
  task loader
  system under test
  evaluator
  metrics
  report writer

BEHAVIOR
  load task
  run system
  compare prediction to expected answer
  score result
  save report

SETTINGS
  benchmark name
  system name
  metric
  output path

EXECUTION
  run evaluation
  inspect results
5. The simplest possible benchmark

Start with a tiny classification benchmark.

benchmarks/classification/sample_tasks.jsonl
{"id": "task_001", "input": "I loved this movie.", "expected": "positive"}
{"id": "task_002", "input": "This was terrible.", "expected": "negative"}
{"id": "task_003", "input": "It was okay.", "expected": "neutral"}

Each line is one task.

The benchmark says:

Given this input text, predict the correct label.
6. The system being evaluated
systems/baseline_classifier.py
class BaselineClassifier:
    def predict(self, text: str) -> str:
        text = text.lower()

        if "loved" in text or "great" in text:
            return "positive"

        if "terrible" in text or "bad" in text:
            return "negative"

        return "neutral"

This is intentionally simple.

A benchmark does not require a fancy system first.

It requires a system that can be tested.

7. The metric
evaluator/metrics.py
def accuracy_score(results):
    correct = 0

    for result in results:
        if result["prediction"] == result["expected"]:
            correct += 1

    return correct / len(results)

Metric means:

How do we judge success?

For classification:

accuracy = correct / total
8. The runner
evaluator/runner.py
def run_evaluation(tasks, system):
    results = []

    for task in tasks:
        prediction = system.predict(task["input"])

        results.append({
            "id": task["id"],
            "input": task["input"],
            "expected": task["expected"],
            "prediction": prediction,
            "correct": prediction == task["expected"],
        })

    return results

This is the harness core.

It runs:

task → system → prediction → result
9. The report
evaluator/report.py
import json


def save_report(results, metrics, path):
    report = {
        "metrics": metrics,
        "results": results,
    }

    with open(path, "w") as f:
        json.dump(report, f, indent=2)

This creates evidence.

Not “I think it worked.”

Actual output:

{
  "metrics": {
    "accuracy": 0.67
  },
  "results": [
    {
      "id": "task_001",
      "expected": "positive",
      "prediction": "positive",
      "correct": true
    }
  ]
}

The machine gets receipts. Society trembles.

10. The execution script
scripts/run_eval.py
import json

from systems.baseline_classifier import BaselineClassifier
from evaluator.runner import run_evaluation
from evaluator.metrics import accuracy_score
from evaluator.report import save_report


def load_jsonl(path):
    tasks = []

    with open(path, "r") as f:
        for line in f:
            tasks.append(json.loads(line))

    return tasks


def main():
    tasks = load_jsonl("benchmarks/classification/sample_tasks.jsonl")

    system = BaselineClassifier()

    results = run_evaluation(tasks, system)

    metrics = {
        "accuracy": accuracy_score(results)
    }

    save_report(
        results=results,
        metrics=metrics,
        path="results/run_001.json",
    )

    print(metrics)


if __name__ == "__main__":
    main()

Run it:

python scripts/run_eval.py
11. How this applies to your actual direction

You can design benchmarks for different intelligence behaviors.

A. Memory benchmark

Tests whether an agent can use prior events.

{"id": "mem_001", "event": "Brian saved project notes under LifeOS.", "question": "Where were the project notes saved?", "expected": "LifeOS"}

Metric:

exact match
semantic match
source citation present
B. Agent benchmark

Tests whether an agent can complete a workflow.

{
  "id": "agent_001",
  "goal": "Convert a text file into markdown and save it.",
  "expected_artifact": "output.md"
}

Metric:

task completed
file exists
format valid
steps logged
C. ARC-style reasoning benchmark

Tests transformations.

{
  "id": "grid_001",
  "train": [
    {
      "input": [[1,0],[0,2]],
      "output": [[0,1],[2,0]]
    }
  ],
  "test": [
    {
      "input": [[3,0],[0,4]],
      "expected": [[0,3],[4,0]]
    }
  ]
}

Metric:

grid exact match
partial cell accuracy
transformation found
12. The key design rule

A good benchmark must have:

1. A task
2. A correct or preferred output
3. A scoring rule
4. A repeatable runner
5. A saved result

No saved result means no reproducibility.

No metric means no evaluation.

No benchmark means no claim.

No claim means, unfortunately, another person on the internet saying “my agent is intelligent” because it opened a browser tab without collapsing emotionally.

13. Your best first repo

Call it:

obversary-eval-harness

Or more general:

ai-evaluation-harness

README description:

A lightweight Python evaluation harness for testing classifiers, agents, memory systems, and reasoning solvers against reproducible benchmark tasks.

That’s a strong repo because it proves you understand the thing most AI demos avoid:

Behavior must be measured.

14. Where this sits on your map
Python Foundations
  ↓
ML Pipelines
  ↓
Agent Systems
  ↓
Benchmarks
  ↓
Evaluation Harnesses
  ↓
Memory-first Cognitive Systems

This is the bridge between your Kaggle work, ARC interest, RL environment thinking, and LifeOS/memory-dropbox direction.

Kaggle gives you external benchmarks.

ARC gives you reasoning benchmarks.

Gymnasium gives you environment benchmarks.

Your evaluation harness lets you build your own benchmark world.

That is the architect move. Not glamorous. Extremely powerful.
