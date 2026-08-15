# ResumeApex Eval Suite

[![CI — Goldcanstaytoday](https://github.com/ndrorchestration/resumeapex-eval/actions/workflows/eval-goldcanstaytoday.yml/badge.svg)](https://github.com/ndrorchestration/resumeapex-eval/actions/workflows/eval-goldcanstaytoday.yml)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/)
[![Benchmark: Goldcanstaytoday](https://img.shields.io/badge/benchmark-Goldcanstaytoday-gold.svg)](docs/specs/goldcanstaytoday_spec_v1.md)
[![Status: Experimental](https://img.shields.io/badge/status-experimental-blue.svg)](#)

> **Epistemic status:** Experimental evaluation repository. Goldcanstaytoday is a repository-defined benchmark/protocol. Its existence, CI execution, or relationship to other projects does not by itself establish statistical validation, external certification, governance authority, or production readiness.

ResumeApex Eval Suite contains the **Goldcanstaytoday** evaluation protocol and supporting evaluation artifacts for AI assistance on resume and career tasks.

## Governance boundary

This repository may integrate with or provide outputs to other projects, including Junior Apogee, Driftwatch, DGAF-related work, and Amethyst-related evaluation work. Those integrations do not make this repository a certified or authoritative evaluation layer, and they do not establish mutual validation.

- **DGAF** — Dynamic Governance Agentic Formation, a related but separate governance/evaluation research track.
- **Amethyst** — related project-local evaluation/orchestration terminology.
- **Driftwatch** — separate drift-detection track.

## What Is Goldcanstaytoday?

Goldcanstaytoday is a three-layer, repository-defined evaluation protocol intended to assess AI assistance on resume and career tasks:

1. **Performance Layer (P)** — task success, completeness, formatting quality
2. **Reciprocity Layer (R)** — user-centered behavior, clarification, constraint respect
3. **Amethyst/Apogee Meta Layer (A)** — repository-defined checks for hallucination detection, epistemic humility, and governance-related behavior

Full protocol specification: `docs/specs/goldcanstaytoday_spec_v1.md`.

The layer names and criteria are project-local definitions. They should not be presented as industry-standard certification categories without independent evidence.

## Quick Start

```bash
git clone https://github.com/ndrorchestration/resumeapex-eval.git
cd resumeapex-eval
pip install -r requirements.txt
python eval/goldcanstaytoday_eval.py --data datasets/resumeapex_dataset1.json
```

## Repository Structure

```text
resumeapex-eval/
├── docs/
│   ├── specs/
│   │   ├── goldcanstaytoday_spec_v1.md
│   │   └── goldcanstaytoday_metrics_rubric_v1.md
│   ├── datasets/
│   │   └── resumeapex_dataset1_card_v1.md
│   └── cards/
│       └── resumeapex_eval_card_v1.md
├── eval/
│   └── goldcanstaytoday_eval.py
├── runlogs/
├── summaries/
├── .github/workflows/
│   └── eval-goldcanstaytoday.yml
└── LICENSE
```

## Evaluation Standards

The following are **target design parameters**, not claims that the benchmark has achieved these statistical properties:

- **Statistical target:** 95% confidence, ±3% CI half-width
- **Runs:** 50–100 independent runs per evaluation
- **Cross-validation:** k-fold (k≈10)
- **Dataset target:** Resume Apex Dataset 1, including real and synthetic cases

Current validation status must be established from the dated run logs, dataset provenance, evaluator implementation, and reproducible results. A CI badge only establishes that the associated workflow reported a result; it does not certify the benchmark.

## Evidence Standard

Claims should distinguish:

**DEFINED → IMPLEMENTED → COMPUTED → VERIFIED → ATTESTED → HISTORICAL → HYPOTHESIS → METAPHOR → UNSUPPORTED → DEPRECATED**

In particular, a benchmark specification is not evidence that the benchmark is validated, and a numerical target is not an achieved result until it is computed from reproducible data.

## Related Projects

- `junior-apogee-app` — related evaluation/QA track
- `DGAF-Framework` — related governance/evaluation research track
- `Amethyst-Governance-Eval-Stack` — related evaluation/orchestration track
- `ai-prompt-systems-portfolio` — prompt-engineering/evaluation portfolio
- `Driftwatch` — separate drift-detection track

Cross-repository references describe intended relationships or integrations; they do not establish mutual validation.

## License

Apache 2.0 — see `LICENSE`.

## Author

Ndr / Ender Hensel (`ndrorchestration`)
