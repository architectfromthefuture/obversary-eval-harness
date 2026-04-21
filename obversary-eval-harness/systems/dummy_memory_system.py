"""A trivial 'memory' system that extracts known facts by substring lookup."""

from __future__ import annotations

from evaluator.schemas import SystemOutput, Task

# Check order: first matching token wins if multiple appear.
_TOKENS = ("memory-dropbox", "FastAPI", "Qdrant")


class DummyMemorySystem:
    """Returns a stored fact token if it appears in the task input; otherwise 'unknown'."""

    def run(self, task: Task) -> SystemOutput:
        text = task.input
        for token in _TOKENS:
            if token in text:
                return SystemOutput(prediction=token)
        return SystemOutput(prediction="unknown")
