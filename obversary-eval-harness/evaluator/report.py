"""Build and persist JSON evaluation reports."""

from __future__ import annotations

import json
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path

from evaluator.schemas import TaskResult


def build_report(
    benchmark_path: str,
    system_name: str,
    metrics: dict,
    results: list[TaskResult],
) -> dict:
    """Assemble a JSON-serializable report with run_meta, metrics, and per-task rows."""
    return {
        "run_meta": {
            "benchmark_path": benchmark_path,
            "system_name": system_name,
            "created_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        },
        "metrics": metrics,
        "tasks": [asdict(tr) for tr in results],
    }


def save_report(path: str | Path, report: dict) -> None:
    """Write report to disk as indented JSON."""
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)
        f.write("\n")
