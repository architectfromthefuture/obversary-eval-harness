#!/usr/bin/env python3
"""Run an evaluation from the repo root: python3 scripts/run_eval.py"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Repo root must be on sys.path when invoked as scripts/run_eval.py
_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from evaluator import (  # noqa: E402 — imports after path fix
    build_report,
    case_insensitive_exact_match,
    exact_match,
    load_jsonl,
    run_evaluation,
    save_report,
    summarize,
)
from systems.baseline_classifier import BaselineClassifier  # noqa: E402
from systems.dummy_memory_system import DummyMemorySystem  # noqa: E402

_SCORERS = {
    "exact": exact_match,
    "case-insensitive": case_insensitive_exact_match,
}

_SYSTEMS = {
    "baseline": BaselineClassifier,
    "dummy-memory": DummyMemorySystem,
}


def main() -> None:
    parser = argparse.ArgumentParser(description="Run evaluation harness on a JSONL benchmark.")
    parser.add_argument(
        "--benchmark",
        default="benchmarks/classification/sentiment_v0.jsonl",
        help="Path to JSONL benchmark file",
    )
    parser.add_argument(
        "--output",
        default="results/run_001.json",
        help="Path to write JSON report",
    )
    parser.add_argument(
        "--system",
        default="baseline",
        choices=["baseline", "dummy-memory"],
        help="System under test",
    )
    parser.add_argument(
        "--scorer",
        default="exact",
        choices=["exact", "case-insensitive"],
        help="How to compare prediction to expected",
    )
    args = parser.parse_args()

    tasks = load_jsonl(_ROOT / args.benchmark)
    system = _SYSTEMS[args.system]()
    scorer = _SCORERS[args.scorer]
    results = run_evaluation(tasks, system, scorer=scorer)
    metrics = summarize(results)
    report = build_report(
        benchmark_path=args.benchmark,
        system_name=args.system,
        metrics=metrics,
        results=results,
    )
    out_path = _ROOT / args.output
    save_report(out_path, report)

    total = metrics["total_tasks"]
    passed = metrics["passed"]
    rate = metrics["pass_rate"]
    print(f"Evaluation complete: {passed}/{total} passed, pass_rate={rate}")
    print(f"Report saved to: {out_path}")


if __name__ == "__main__":
    main()
