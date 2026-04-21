"""Evaluation harness: load tasks, run systems, score, summarize, report."""

from __future__ import annotations

from evaluator.report import build_report, save_report
from evaluator.runner import System, run_evaluation
from evaluator.schemas import ScoreResult, SystemOutput, Task, TaskResult
from evaluator.scorers import case_insensitive_exact_match, exact_match
from evaluator.task_loader import load_jsonl
from evaluator.metrics import summarize

__all__ = [
    "Task",
    "SystemOutput",
    "ScoreResult",
    "TaskResult",
    "System",
    "exact_match",
    "case_insensitive_exact_match",
    "load_jsonl",
    "run_evaluation",
    "summarize",
    "build_report",
    "save_report",
]
