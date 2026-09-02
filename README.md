# ResumeApex Eval Suite

[![CI — Goldcanstaytoday](https://github.com/ndrorchestration/resumeapex-eval/actions/workflows/eval-goldcanstaytoday.yml/badge.svg)](https://github.com/ndrorchestration/resumeapex-eval/actions/workflows/eval-goldcanstaytoday.yml)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/)
[![Benchmark: Goldcanstaytoday](https://img.shields.io/badge/benchmark-Goldcanstaytoday-gold.svg)](docs/specs/goldcanstaytoday_spec_v1.md)
[![Status: Experimental](https://img.shields.io/badge/status-experimental-blue.svg)](#status)

> **Epistemic status:** Experimental evaluation repository. Goldcanstaytoday is a repository-defined benchmark/protocol. The executable harness is now testable against a public known-answer fixture, but this does not establish model performance, statistical validation of the private Dataset 1 corpus, external certification, governance authority, or production readiness.

ResumeApex Eval Suite contains the **Goldcanstaytoday** evaluation protocol and a reproducible evaluation harness for AI assistance on resume and career tasks.

## What is implemented

The repository now separates four maturity states:

| State | Meaning |
|---|---|
| **DEFINED** | Protocol/rubric is specified. |
| **IMPLEMENTED** | Evaluation code exists and is executable. |
| **VERIFIED** | Evaluator behavior passes known-answer and deterministic-repeatability tests. |
| **EMPIRICALLY EXECUTED** | A real model/corpus run has produced reproducible results. |

The current fixture path reaches **VERIFIED**. Real-model and private-corpus benchmark execution remains a separate gate.

## Goldcanstaytoday layers

1. **Performance (P)** — task success, completeness, formatting quality
2. **Reciprocity (R)** — clarification, constraint respect, user-centered behavior
3. **Amethyst/Apogee Meta (A)** — hallucination detection, epistemic humility, governance-related behavior

These are project-local definitions, not industry-standard certification categories.

## Quick Start

```bash
git clone https://github.com/ndrorchestration/resumeapex-eval.git
cd resumeapex-eval
python -m pip install -r requirements.txt
python -m pytest -q
python -m eval.cli --data datasets/fixture_v1.json --runs 2 --seed 20260902 --bootstrap-resamples 1000 --verify-expected --output runlogs/fixture-verification.json
```

The fixture adapter is a **known-answer harness adapter**, not an AI model. Its output must never be presented as model performance.

## Reproducibility

A run records the dataset hash, evaluator version, run count, analysis seed, bootstrap resample count, metrics, confidence intervals, and epistemic boundary. Deterministic fixture runs are repeated in CI and their artifacts compared byte-for-byte.

## Dataset boundary

`datasets/fixture_v1.json` is public synthetic/known-answer data used to verify the machinery. Resume Apex Dataset 1 is a separate governed corpus and is not represented as publicly released by this repository. Dataset size and empirical benchmark results must come from dated evidence rather than targets in the specification.

## Evaluation targets

The specification's statistical parameters remain **design targets**: 95% confidence, approximately ±3 percentage-point CI half-width, and 50–100 runs with cross-validation. Those targets are not achieved-result claims.

## Evidence Standard

Claims should distinguish:

**DEFINED → IMPLEMENTED → COMPUTED → VERIFIED → ATTESTED → HISTORICAL → HYPOTHESIS → METAPHOR → UNSUPPORTED → DEPRECATED**

A benchmark specification is not benchmark validation. A green CI run demonstrates only the checks executed by that workflow.

## Related Projects

- `junior-apogee-app` — related evaluation/QA track
- `DGAF-Framework` — related governance/evaluation research track
- `Amethyst-Governance-Eval-Stack` — related evaluation/orchestration track
- `ai-prompt-systems-portfolio` — prompt-engineering/evaluation portfolio
- `Driftwatch` — separate drift-detection track

Cross-repository references do not establish mutual validation.

## Status

**Active / experimental.** The public fixture harness is executable and CI-verifiable. Real benchmark execution, private Dataset 1 validation, inter-rater validation, and model-performance claims remain separate evidence gates.

## License

Apache 2.0 — see `LICENSE`.

## Author

Ndr / Ender Hensel (`ndrorchestration`)
