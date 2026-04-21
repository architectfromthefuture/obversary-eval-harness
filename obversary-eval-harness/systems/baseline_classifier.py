"""A tiny rule-based sentiment classifier for demonstration and baseline scoring."""

from __future__ import annotations

from evaluator.schemas import SystemOutput, Task

_POSITIVE_KEYWORDS = frozenset(
    {
        "love",
        "loved",
        "fantastic",
        "great",
        "excellent",
        "amazing",
    }
)
_NEGATIVE_KEYWORDS = frozenset(
    {
        "terrible",
        "bad",
        "awful",
        "hate",
        "hated",
        "worst",
    }
)


class BaselineClassifier:
    """Classify sentiment using keyword lists; negative overrides positive."""

    def run(self, task: Task) -> SystemOutput:
        label = _predict(task.input)
        return SystemOutput(prediction=label)


def _predict(text: str) -> str:
    lower = text.lower()
    if any(kw in lower for kw in _NEGATIVE_KEYWORDS):
        return "negative"
    if any(kw in lower for kw in _POSITIVE_KEYWORDS):
        return "positive"
    return "neutral"
