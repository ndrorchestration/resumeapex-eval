# ResumeApex Evaluation Card v1

**Original date:** 2026-04-08  
**Current epistemic status:** Experimental / executable harness verified; empirical model validation pending  
**Version:** 1.0.0  
**Last epistemic review:** 2026-09-02

## Benchmarks Featured

### Goldcanstaytoday (Primary)
- **Spec:** `docs/specs/goldcanstaytoday_spec_v1.md`
- **Protocol:** 3-layer audit (Performance / Reciprocity / Amethyst-Apogee)
- **Dataset:** Resume Apex Dataset 1 (private/governed corpus; execution not established here)
- **Public fixture:** `datasets/fixture_v1.json`
- **Statistical target:** 95% confidence; approximately ±3 percentage-point CI half-width
- **Run target:** 50–100 runs where justified, with approximately 10-fold CV where applicable

## Evidence State

| Layer | Current state |
|---|---|
| Protocol | **DEFINED** |
| Evaluator core | **IMPLEMENTED** |
| Public known-answer fixture | **VERIFIED** |
| Deterministic repeatability | **VERIFIED** when CI passes |
| Real-model evaluation | **NOT ESTABLISHED** |
| Resume Apex Dataset 1 execution | **NOT ESTABLISHED** |
| Statistical benchmark validation | **NOT ESTABLISHED** |
| External certification | **NOT CLAIMED** |
| Production readiness | **NOT CLAIMED** |

## Metric Targets

| Layer | Key Metric | Target |
|-------|-----------|--------|
| Performance | task_success | ≥0.85 |
| Reciprocity | constraint_respect | ≥0.90 |
| Amethyst/Apogee | hallucination_flag | ≤0.05 |
| Amethyst/Apogee | epistemic_humility | ≥0.80 |

Targets are design thresholds, not observed model results.

## Verification boundary

The public fixture adapter is a known-answer mechanism used to verify evaluator behavior. It is not an AI model and must not be used as evidence of model performance.

The harness records dataset hashes, evaluator version, run count, analysis seed, bootstrap configuration, aggregate statistics, confidence intervals, and a claims-boundary field. CI repeats the fixture run and compares outputs for deterministic reproducibility.

## Remaining evidence gates

- Formal human/adjudicator agreement study for rubric reliability.
- Real-model adapter execution with model identity/configuration provenance.
- Provenance-controlled execution of the private Dataset 1 corpus.
- Appropriate statistical design for actual independent observations and cross-validation.
- Result review before any empirical performance claim.
