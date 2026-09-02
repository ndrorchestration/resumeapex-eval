from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Callable, Mapping

from .metrics import aggregate, validate_metrics
from .schemas import EvaluationCase, validate_cases
from .statistics import bootstrap_ci

Evaluator = Callable[[EvaluationCase], Mapping[str, float]]


def load_cases(path: str | Path) -> list[EvaluationCase]:
    raw = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(raw, list):
        raise ValueError("dataset JSON must be an array")
    cases = [EvaluationCase.from_dict(item) for item in raw]
    validate_cases(cases)
    return cases


def file_sha256(path: str | Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def evaluate(cases: list[EvaluationCase], evaluator: Evaluator, *, runs: int = 1, analysis_seed: int = 20260902, bootstrap_resamples: int = 10_000) -> dict:
    validate_cases(cases)
    if runs < 1:
        raise ValueError("runs must be positive")
    run_rows: list[dict] = []
    metric_samples: dict[str, list[float]] = {}
    for run_idx in range(runs):
        for case in cases:
            metrics = validate_metrics(evaluator(case))
            run_rows.append({"run": run_idx, "case_id": case.case_id, "metrics": metrics})
            for name, value in metrics.items():
                metric_samples.setdefault(name, []).append(value)
    aggregate_result = aggregate([row["metrics"] for row in run_rows])
    stats = {name: bootstrap_ci(values, seed=analysis_seed + idx, resamples=bootstrap_resamples) for idx, (name, values) in enumerate(sorted(metric_samples.items()))}
    return {
        "status": "COMPUTED",
        "runs": runs,
        "cases": len(cases),
        "observations": len(run_rows),
        "analysis_seed": analysis_seed,
        "bootstrap_resamples": bootstrap_resamples,
        "aggregate": aggregate_result,
        "confidence_intervals": stats,
        "results": run_rows,
    }
