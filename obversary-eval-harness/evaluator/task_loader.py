"""Load benchmark tasks from JSONL files."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from evaluator.schemas import Task

_REQUIRED_KEYS = frozenset({"id", "input", "expected"})


def load_jsonl(path: str | Path) -> list[Task]:
    """Load tasks from a JSONL file. Each non-blank line must be a JSON object with id, input, expected."""
    p = Path(path)
    if not p.is_file():
        raise FileNotFoundError(f"Benchmark file not found: {p}")

    tasks: list[Task] = []
    with p.open(encoding="utf-8") as f:
        for line_no, raw in enumerate(f, start=1):
            line = raw.strip()
            if not line:
                continue
            try:
                obj: Any = json.loads(line)
            except json.JSONDecodeError as e:
                raise ValueError(
                    f"Invalid JSON on line {line_no} of {p}: {e.msg}"
                ) from e

            if not isinstance(obj, dict):
                raise ValueError(
                    f"Line {line_no} of {p}: expected a JSON object, got {type(obj).__name__}"
                )

            missing = _REQUIRED_KEYS - obj.keys()
            if missing:
                raise ValueError(
                    f"Line {line_no} of {p}: missing required key(s): {sorted(missing)}"
                )

            tasks.append(
                Task(
                    id=str(obj["id"]),
                    input=str(obj["input"]),
                    expected=str(obj["expected"]),
                )
            )

    return tasks
