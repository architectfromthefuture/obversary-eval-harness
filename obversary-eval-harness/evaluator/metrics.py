"""Aggregate metrics over per-task results."""

from __future__ import annotations

from evaluator.schemas import TaskResult


def summarize(results: list[TaskResult]) -> dict:
    """Return summary statistics; safe for an empty result list."""
    total = len(results)
    if total == 0:
        return {
            "total_tasks": 0,
            "passed": 0,
            "failed": 0,
            "pass_rate": 0.0,
            "average_score": 0.0,
            "average_latency_ms": 0.0,
        }

    passed = sum(1 for r in results if r.passed)
    failed = total - passed
    pass_rate = passed / total
    average_score = sum(r.score for r in results) / total
    average_latency_ms = sum(r.latency_ms for r in results) / total

    return {
        "total_tasks": total,
        "passed": passed,
        "failed": failed,
        "pass_rate": pass_rate,
        "average_score": average_score,
        "average_latency_ms": average_latency_ms,
    }
