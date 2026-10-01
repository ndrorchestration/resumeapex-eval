import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, os.path.join(ROOT, "_deps", "dgaf"))

from scripts.claimgraph_v0 import VALID, validate_claim_graph_receipt

FIXTURE = ROOT / "tests" / "fixtures" / "claimgraph_resumeapex_example.json"


def main() -> None:
    graph = json.loads(FIXTURE.read_text(encoding="utf-8"))
    receipt = validate_claim_graph_receipt(graph)

    assert receipt.valid is True
    assert receipt.reason_code == VALID
    assert receipt.graph_id == "EGRAPH-RESUME-EVAL-001"
    assert receipt.claim_count == 1
    assert receipt.evidence_count == 3
    assert receipt.relation_count == 4
    assert receipt.truth_effect == "NONE"
    assert receipt.authorization_effect == "NONE"

    print("CLAIMGRAPH_EXTERNAL_CONSUMER=PASS")


if __name__ == "__main__":
    main()
