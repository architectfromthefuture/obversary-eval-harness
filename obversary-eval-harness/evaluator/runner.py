"""Run a system under test over benchmark tasks and collect scored results."""

from __future__ import annotations

import time
from collections.abc import Callable
from typing import Protocol

from evaluator.schemas import ScoreResult, SystemOutput, Task, TaskResult


class System(Protocol):
    """Anything implementing run(task) -> SystemOutput can be evaluated."""

    def run(self, task: Task) -> SystemOutput:
        ...


def run_evaluation(
    tasks: list[Task],
    system: System,
    scorer: Callable[[str, str], ScoreResult],
) -> list[TaskResult]:
    """Execute the system on each task, score with ``scorer``, and record latency and errors."""
    results: list[TaskResult] = []
    for task in tasks:
        t0 = time.perf_counter()
        try:
            output = system.run(task)
        except Exception as e:  # noqa: BLE001 — capture any system failure for the report
            latency_ms = (time.perf_counter() - t0) * 1000.0
            results.append(
                TaskResult(
                    task_id=task.id,
                    input=task.input,
                    expected=task.expected,
                    prediction=None,
                    passed=False,
                    score=0.0,
                    failure_type="error",
                    latency_ms=latency_ms,
                    error=str(e),
                )
            )
            continue

        latency_ms = (time.perf_counter() - t0) * 1000.0
        scored = scorer(output.prediction, task.expected)
        results.append(
            TaskResult(
                task_id=task.id,
                input=task.input,
                expected=task.expected,
                prediction=output.prediction,
                passed=scored.passed,
                score=scored.score,
                failure_type=scored.failure_type,
                latency_ms=latency_ms,
                error=None,
            )
        )

    return results
