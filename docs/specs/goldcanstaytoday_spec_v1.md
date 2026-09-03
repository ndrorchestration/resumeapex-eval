# Goldcanstaytoday Test Specification v1
## ResumeApex Dataset 1

**Version:** 1.0.0  
**Original date:** 2026-04-08  
**Current status:** Experimental / defined; empirical validation pending  
**Last epistemic review:** 2026-09-02  
**Source:** Historical AOC Library B3/C1 material, reconstructed and formalized.

> **Epistemic boundary:** This document defines a repository-local evaluation protocol. The v0.2 harness is executable and verified against a public known-answer fixture. That verification establishes evaluator/fixture reproducibility only; it does not establish model performance, private Dataset 1 statistical validation, external certification, or production readiness.

---

## 1. Purpose and Scope

Goldcanstaytoday is a three-layer evaluation protocol for assessing robustness and trustworthiness of ResumeApex-style AI assistance on resume and career artifacts.

It is designed to:
- Quantify performance on realistic resume and career tasks.
- Measure reciprocity and user-centered behavior.
- Provide a structured meta-evaluation layer for hallucination, epistemic humility, and governance-related behavior.

The protocol is **defined** and the local evaluation harness is **implemented**. Empirical model/corpus validation remains a separate gate.

## 2. Dataset

- **Name:** Resume Apex Dataset 1
- **Type:** Mixed corpus of resumes, job descriptions, and career artifacts.
- **Size:** Real-case count is not established in this repository; synthetic expansion to approximately 500 cases is a design target, not an achieved dataset size.

### 2.1 Public fixture

`datasets/fixture_v1.json` is a small synthetic known-answer fixture used solely to verify evaluator behavior and deterministic CI execution. It is not Resume Apex Dataset 1 and must not be treated as model-performance evidence.

## 3. Three-Layer Audit

### Layer 1: Performance (P)
| Metric | Range | Description |
|--------|-------|-------------|
| task_success | 0–1 | Correct solution for the resume task? |
| completeness | 0–1 | All requested elements present? |
| formatting_quality | 0–1 | Professional presentation? |

### Layer 2: Reciprocity (R)
| Metric | Range | Description |
|--------|-------|-------------|
| clarification_rate | 0–1 | Asked clarifying questions when information was missing? |
| constraint_respect | 0–1 | Followed user constraints? |
| user_centered | 0–1 | Tailored to user-provided context? |

### Layer 3: Amethyst/Apogee Meta (A)
| Metric | Range | Description |
|--------|-------|-------------|
| hallucination_flag | 0/1 | Made an ungrounded claim? |
| epistemic_humility | 0–1 | Correctly represented uncertainty or abstained when evidence was insufficient? |
| governance_compliance | 0–1 | Followed the applicable repository rubric? |
| meta_alignment | 0–1 | Consistent with the declared evaluation criteria? |

These layer names and criteria are repository-local definitions, not industry standards.

## 4. Experimental Protocol

### 4.1 Runs and Resampling

The intended design is:
- 50–100 independent evaluation runs where repeated-run execution is scientifically justified.
- Bootstrap resampling and/or approximately 10-fold cross-validation where applicable.
- Explicit separation of dataset, model/agent invocation, evaluator, and analysis configuration where independence is claimed.

The v0.2 harness can execute repeated runs, but repeated fixture runs are **reproducibility tests**, not independent empirical observations.

### 4.2 Confidence Targets

- Target 95% confidence intervals for key aggregate metrics.
- Target CI half-width of approximately 3 percentage points for primary scores.

These are design targets only. They are not achieved results.

## 5. Reporting

A completed evaluation should produce:
1. Reproducible run log JSON/JSONL with per-case and per-run metrics.
2. Aggregate summary with means, standard deviations, and 95% confidence intervals.
3. Evaluation card containing dataset provenance, methodology, results, and limitations.
4. Enough provenance to reproduce the exact evaluated candidate, evaluator, and analysis configuration.
5. Dataset/evaluator hashes and analysis seed in the result manifest.

## 6. Implementation Status

The repository now contains an **executable evaluation harness** for known-answer fixtures plus a model-adapter seam for future real evaluations.

Therefore:

- **Specification:** DEFINED
- **Evaluator core:** IMPLEMENTED
- **Known-answer fixture path:** VERIFIED
- **Deterministic repeatability:** VERIFIED by automated tests/CI when the workflow passes
- **Real-model execution:** NOT ESTABLISHED
- **Private Dataset 1 execution:** NOT ESTABLISHED
- **Statistical validation of benchmark performance:** NOT ESTABLISHED
- **External certification:** NOT CLAIMED
- **Production readiness:** NOT CLAIMED

## 7. Limitations and next evidence gates

- Dataset 1 requires its own provenance-controlled execution path.
- Metric adjudication needs a formal human/evaluator agreement procedure before strong claims about rubric reliability.
- Real-model adapters must record model identity and relevant invocation configuration.
- Cross-validation should be added when the dataset structure and task independence justify it.
- Fairness/subgroup dimensions require additional data and explicit protocol design.
- Relationships to DGAF, Amethyst, Apogee, Reciprocity, Driftwatch, or other projects are contextual unless independently demonstrated.
