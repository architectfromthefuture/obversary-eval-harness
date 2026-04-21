"""Scoring functions for comparing predictions to expected labels."""

from __future__ import annotations

from evaluator.schemas import ScoreResult


def exact_match(prediction: str, expected: str) -> ScoreResult:
    """Score 1.0 on exact string match; otherwise 0.0 with failure_type 'wrong_answer'."""
    if prediction == expected:
        return ScoreResult(score=1.0, passed=True, failure_type=None)
    return ScoreResult(score=0.0, passed=False, failure_type="wrong_answer")


def case_insensitive_exact_match(prediction: str, expected: str) -> ScoreResult:
    """Like exact_match, but compares strings case-insensitively."""
    if prediction.casefold() == expected.casefold():
        return ScoreResult(score=1.0, passed=True, failure_type=None)
    return ScoreResult(score=0.0, passed=False, failure_type="wrong_answer")
