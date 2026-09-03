from __future__ import annotations

from statistics import mean, stdev
from typing import Mapping

from .schemas import METRICS

def validate_metrics(metrics: Mapping[str, float]) -> dict[str, float]:
    out = {}
    for name in METRICS:
        if name not in metrics:
            raise ValueError(f"missing metric: {name}")
        value = float(metrics[name])
        if not 0 <= value <= 1:
            raise ValueError(f"metric {name} must be in [0,1]")
        out[name] = value
    return out

def aggregate(case_results: list[Mapping[str, float]]) -> dict[str, dict[str, float]]:
    if not case_results:
        raise ValueError("cannot aggregate empty results")
    rows = [validate_metrics(r) for r in case_results]
    result: dict[str, dict[str, float]] = {}
    for metric in METRICS:
        values = [r[metric] for r in rows]
        result[metric] = {
            "n": float(len(values)),
            "mean": mean(values),
            "stdev": stdev(values) if len(values) > 1 else 0.0,
        }
    return result
