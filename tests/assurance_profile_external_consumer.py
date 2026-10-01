import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, os.path.join(ROOT, "_deps", "dgaf"))

from components.assurance_profile_v0 import (
    AUTHORIZATION_EFFECT_NONE,
    CERTIFICATION_EFFECT_NONE,
    AssuranceProfileInput,
    DimensionAssessment,
    DimensionStatus,
    IndependenceClass,
    evaluate_assurance_profile,
)

CONFIG = ROOT / "tests" / "fixtures" / "assurance_profile_resumeapex.json"


def _assessment(value: dict) -> DimensionAssessment:
    return DimensionAssessment(
        status=DimensionStatus(value["status"]),
        required=bool(value["required"]),
        evidence_refs=tuple(value.get("evidence_refs", [])),
        limitation=value.get("limitation"),
    )


def main() -> None:
    data = json.loads(CONFIG.read_text(encoding="utf-8"))
    dims = data["dimensions"]

    profile = AssuranceProfileInput(
        profile_id=data["profile_id"],
        profile_version=data["profile_version"],
        target_system=data["target_system"],
        source_identity=data["source_identity"],
        runtime_identity=data["runtime_identity"],
        environment_identity=data["environment_identity"],
        material_source_manifest_ref=data.get("material_source_manifest_ref"),
        measurement_apparatus=_assessment(dims["measurement_apparatus"]),
        runtime_source_environment_binding=_assessment(
            dims["runtime_source_environment_binding"]
        ),
        authorization_decision_separation=_assessment(
            dims["authorization_decision_separation"]
        ),
        custody_replay_integrity=_assessment(dims["custody_replay_integrity"]),
        readiness_preflight=_assessment(dims["readiness_preflight"]),
        trust_independence_review=_assessment(dims["trust_independence_review"]),
        independence_class=IndependenceClass(data["independence_class"]),
        claim_ceiling=tuple(data["claim_ceiling"]),
    )

    receipt = evaluate_assurance_profile(profile)

    assert receipt.passed is True
    assert receipt.target_system == "resumeapex-eval"
    assert receipt.independence_class is IndependenceClass.SAME_SYSTEM
    assert receipt.authorization_effect == AUTHORIZATION_EFFECT_NONE
    assert receipt.certification_effect == CERTIFICATION_EFFECT_NONE
    assert receipt.unresolved_blockers == ()

    print("ASSURANCE_PROFILE_EXTERNAL_CONSUMER=PASS")


if __name__ == "__main__":
    main()
