# ResumeApex Evaluation Card v1

**Original date:** 2026-04-08  
**Current epistemic status:** Experimental / defined; empirical validation pending  
**Version:** 1.0.0  
**Last epistemic review:** 2026-08-30

## Benchmarks Featured

### Goldcanstaytoday (Primary)
- **Spec:** `docs/specs/goldcanstaytoday_spec_v1.md`
- **Protocol:** 3-layer audit (Performance / Reciprocity / Amethyst-Apogee)
- **Dataset:** Resume Apex Dataset 1
- **Confidence target:** 95%, approximately ±3 percentage-point CI half-width
- **Runs:** 50–100 target runs where justified, with approximately 10-fold CV where applicable
- **Current status:** Specification defined; evaluator scaffold incomplete; empirical runs/results not established in this repository

## Metrics Summary

| Layer | Key Metric | Target |
|-------|-----------|--------|
| Performance | task_success | ≥0.85 |
| Reciprocity | constraint_respect | ≥0.90 |
| Amethyst/Apogee | hallucination_flag | ≤0.05 |
| Amethyst/Apogee | epistemic_humility | ≥0.80 |

Targets are design thresholds, not observed results.

## Evidence State

- **DEFINED:** Goldcanstaytoday protocol and target metrics.
- **IMPLEMENTED:** Evaluation scaffold and repository documentation.
- **COMPUTED:** No validated aggregate benchmark result established here.
- **VERIFIED:** No independent empirical verification established here.
- **ATTESTED:** Not claimed.
- **PRODUCTION:** Not claimed.

## Honest Constraints

- The evaluator currently contains unimplemented dataset-loading and model/case-execution hooks.
- Aggregate confidence-interval computation is not yet implemented in the scaffold.
- The repository does not establish the real-case count or a completed ~500-case dataset.
- CI success, if observed, establishes workflow execution rather than scientific validation.
- Cross-references to DGAF, Amethyst, Apogee, Reciprocity, Driftwatch, or other projects do not establish mutual certification or validation.
