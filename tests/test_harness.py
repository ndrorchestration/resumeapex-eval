from pathlib import Path

import pytest

from eval.adapters import fixture_adapter, strict_zero_adapter
from eval.core import evaluate, load_cases
from eval.metrics import validate_metrics

DATA = Path(__file__).parents[1] / "datasets" / "fixture_v1.json"


def test_fixture_loads_and_scores():
    cases = load_cases(DATA)
    result = evaluate(cases, fixture_adapter, runs=2, analysis_seed=7, bootstrap_resamples=200, verify_expected=True)
    assert result["status"] == "VERIFIED"
    assert result["known_answer_verification"] is True
    assert result["cases"] == 3
    assert result["observations"] == 6
    assert result["aggregate"]["task_success"]["mean"] == 1.0
    assert result["aggregate"]["hallucination_flag"]["mean"] == 0.0


def test_fixture_is_deterministic():
    cases = load_cases(DATA)
    a = evaluate(cases, fixture_adapter, runs=2, analysis_seed=99, bootstrap_resamples=200, verify_expected=True)
    b = evaluate(cases, fixture_adapter, runs=2, analysis_seed=99, bootstrap_resamples=200, verify_expected=True)
    assert a["confidence_intervals"] == b["confidence_intervals"]
    assert a["results"] == b["results"]


def test_negative_control_is_rejected():
    cases = load_cases(DATA)
    with pytest.raises(ValueError, match="known-answer mismatch"):
        evaluate(cases, strict_zero_adapter, runs=1, analysis_seed=1, bootstrap_resamples=50, verify_expected=True)


def test_metric_bounds_and_completeness():
    cases = load_cases(DATA)
    assert set(validate_metrics(fixture_adapter(cases[0]))) == {
        "task_success", "completeness", "formatting_quality", "clarification_rate",
        "constraint_respect", "user_centered", "hallucination_flag", "epistemic_humility",
        "governance_compliance", "meta_alignment",
    }
