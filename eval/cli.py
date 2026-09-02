from __future__ import annotations

import argparse
import json
from pathlib import Path

from .adapters import fixture_adapter
from .core import evaluate, file_sha256, load_cases


def main() -> int:
    parser = argparse.ArgumentParser(description="Run ResumeApex/Goldcanstaytoday evaluation harness")
    parser.add_argument("--data", required=True)
    parser.add_argument("--runs", type=int, default=1)
    parser.add_argument("--seed", type=int, default=20260902)
    parser.add_argument("--bootstrap-resamples", type=int, default=1000)
    parser.add_argument("--output", default="runlogs/evaluation.json")
    args = parser.parse_args()

    cases = load_cases(args.data)
    result = evaluate(cases, fixture_adapter, runs=args.runs, analysis_seed=args.seed, bootstrap_resamples=args.bootstrap_resamples)
    result["dataset_sha256"] = file_sha256(args.data)
    result["evaluator_version"] = "0.2.0"
    result["adapter"] = "fixture_adapter"
    result["claims_boundary"] = "Harness verification only; not model performance or empirical validation."
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"status": result["status"], "cases": result["cases"], "observations": result["observations"], "output": str(output)}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
