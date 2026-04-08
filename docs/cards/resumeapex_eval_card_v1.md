# ResumeApex Evaluation Card v1

**Date:** 2026-04-08  
**Status:** Production  
**Version:** 1.0.0

## Benchmarks Featured

### Goldcanstaytoday (Primary)
- **Spec:** [docs/specs/goldcanstaytoday_spec_v1.md](docs/specs/goldcanstaytoday_spec_v1.md)
- **Protocol:** 3-layer audit (Performance / Reciprocity / Lavender-Apogee)
- **Dataset:** Resume Apex Dataset 1
- **Confidence target:** 95%, ±3% CI half-width
- **Runs:** 50–100 with k-fold CV
- **Status:** Spec live; runs pending implementation

## Metrics Summary

| Layer | Key Metric | Target |
|-------|-----------|--------|
| Performance | task_success | ≥0.85 |
| Reciprocity | constraint_respect | ≥0.90 |
| Lavender/Apogee | hallucination_flag | ≤0.05 |
| Lavender/Apogee | epistemic_humility | ≥0.80 |

## Honest Constraints
- Results above are targets, not yet confirmed from completed run logs.
- Actual results will be logged in `runlogs/` and summarized in `summaries/` once runs complete.
