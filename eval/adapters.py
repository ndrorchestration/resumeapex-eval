from __future__ import annotations

from typing import Mapping

from .schemas import EvaluationCase


def fixture_adapter(case: EvaluationCase) -> Mapping[str, float]:
    """Return the case's declared expected metrics for harness verification.

    This is intentionally not a model and must never be reported as model performance.
    """
    return case.expected_metrics


def strict_zero_adapter(case: EvaluationCase) -> Mapping[str, float]:
    """Negative control used to verify that the harness detects non-matching output."""
    return {name: 0.0 for name in case.expected_metrics}
