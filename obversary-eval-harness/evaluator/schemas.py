"""Dataclass models for tasks, system outputs, scores, and per-task results."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Task:
    id: str
    input: str
    expected: str


@dataclass
class SystemOutput:
    prediction: str


@dataclass
class ScoreResult:
    score: float
    passed: bool
    failure_type: str | None


@dataclass
class TaskResult:
    task_id: str
    input: str
    expected: str
    prediction: str | None
    passed: bool
    score: float
    failure_type: str | None
    latency_ms: float
    error: str | None
