from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping

METRICS = (
    "task_success",
    "completeness",
    "formatting_quality",
    "clarification_rate",
    "constraint_respect",
    "user_centered",
    "hallucination_flag",
    "epistemic_humility",
    "governance_compliance",
    "meta_alignment",
)

@dataclass(frozen=True)
class EvaluationCase:
    case_id: str
    prompt: str
    expected_metrics: Mapping[str, float]
    metadata: Mapping[str, Any] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, raw: Mapping[str, Any]) -> "EvaluationCase":
        case_id = raw.get("case_id")
        prompt = raw.get("prompt")
        expected = raw.get("expected_metrics", {})
        if not isinstance(case_id, str) or not case_id:
            raise ValueError("case_id must be a non-empty string")
        if not isinstance(prompt, str):
            raise ValueError(f"{case_id}: prompt must be a string")
        if not isinstance(expected, Mapping):
            raise ValueError(f"{case_id}: expected_metrics must be an object")
        for name, value in expected.items():
            if name not in METRICS:
                raise ValueError(f"{case_id}: unknown metric {name!r}")
            if not isinstance(value, (int, float)) or not 0 <= float(value) <= 1:
                raise ValueError(f"{case_id}: metric {name} must be in [0,1]")
        return cls(case_id, prompt, dict(expected), dict(raw.get("metadata", {})))

def validate_cases(cases: list[EvaluationCase]) -> None:
    ids = [c.case_id for c in cases]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate case_id detected")
    if not cases:
        raise ValueError("dataset must contain at least one case")
