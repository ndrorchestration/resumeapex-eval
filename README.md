# ResumeApex Eval Suite

[![CI — Goldcanstaytoday](https://github.com/Flickerflash/resumeapex-eval/actions/workflows/eval-goldcanstaytoday.yml/badge.svg)](https://github.com/Flickerflash/resumeapex-eval/actions/workflows/eval-goldcanstaytoday.yml)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/)
[![Benchmark: Goldcanstaytoday](https://img.shields.io/badge/benchmark-Goldcanstaytoday-gold.svg)](docs/specs/goldcanstaytoday_spec_v1.md)
[![Status: Stable](https://img.shields.io/badge/status-stable-brightgreen.svg)](#)

> **Governance:** DGAF / Agent Amethyst — Yes. This repo is the flagship benchmark under the DGAF evaluation layer. Outputs feed into [junior-apogee-app](https://github.com/Flickerflash/junior-apogee-app) and Driftwatch visualization. See [DGAF-Framework](https://github.com/Flickerflash/DGAF-Framework) for spine documentation.

**Status: Stable — actively maintained. Last eval run logged in `runlogs/`.** Small commit gaps do not indicate abandonment; this repo operates on evaluation cadence, not daily commits.

Evaluation framework for ResumeApex AI assistance, featuring the **Goldcanstaytoday** 3-layer benchmark.

## What Is Goldcanstaytoday?

Goldcanstaytoday is a three-layer evaluation protocol designed to assess the robustness and trustworthiness of AI assistance on resume and career tasks:

1. **Performance Layer (P)** — task success, completeness, formatting quality
2. **Reciprocity Layer (R)** — user-centered behavior, clarification, constraint respect
3. **Amethyst/Apogee Meta Layer (A)** — hallucination detection, epistemic humility, governance compliance

Full spec: [docs/specs/goldcanstaytoday_spec_v1.md](docs/specs/goldcanstaytoday_spec_v1.md)

## Quick Start

```bash
git clone https://github.com/Flickerflash/resumeapex-eval.git
cd resumeapex-eval
pip install -r requirements.txt
python eval/goldcanstaytoday_eval.py --data datasets/resumeapex_dataset1.json
```

## Repository Structure

```
resumeapex-eval/
├── docs/
│   ├── specs/
│   │   ├── goldcanstaytoday_spec_v1.md        # Full protocol spec
│   │   └── goldcanstaytoday_metrics_rubric_v1.md
│   ├── datasets/
│   │   └── resumeapex_dataset1_card_v1.md     # Dataset card
│   └── cards/
│       └── resumeapex_eval_card_v1.md         # Eval/model card
├── eval/
│   └── goldcanstaytoday_eval.py            # Runnable eval scaffold
├── runlogs/                              # Evaluation run logs (JSONL)
├── summaries/                            # Aggregate summaries
├── .github/workflows/
│   └── eval-goldcanstaytoday.yml          # Weekly/manual CI runner
└── LICENSE
```

## Evaluation Standards

- **Statistical target:** 95% confidence, ±3% CI half-width
- **Runs:** 50–100 independent runs per evaluation
- **Cross-validation:** k-fold (k≈10)
- **Dataset:** Resume Apex Dataset 1 (real + synthetic, ~500 cases)

## Related Projects

- [junior-apogee-app](https://github.com/Flickerflash/junior-apogee-app) — primary evaluated system
- [DGAF-Framework](https://github.com/Flickerflash/DGAF-Framework) — governance spine
- [Amethyst-Governance-Eval-Stack](https://github.com/Flickerflash/Amethyst-Governance-Eval-Stack) — meta-orchestration eval layer
- [ai-prompt-systems-portfolio](https://github.com/Flickerflash/ai-prompt-systems-portfolio) — prompt eval patterns

## License

Apache 2.0 — see [LICENSE](LICENSE).

## Author

[Ndr / Flickerflash](https://github.com/Flickerflash) · [LinkedIn](https://www.linkedin.com/in/andrewhensel) · [Portfolio](https://flickerflash.vercel.app/)
