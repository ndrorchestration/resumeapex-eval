# Goldcanstaytoday Test Specification v1
## ResumeApex Dataset 1

**Version:** 1.0.0  
**Date:** 2026-04-08  
**Status:** Production  
**Source:** AOC Library B3/C1 cluster, reconstructed and formalized.

---

## 1. Purpose and Scope

Goldcanstaytoday is a three-layer evaluation protocol for assessing the robustness and trustworthiness of ResumeApex-style AI assistance on resume and career artifacts.

It is designed to:
- Quantify performance on realistic resume and career tasks.
- Measure reciprocity and user-centered behavior over time.
- Validate the validator (Amethyst/Apogee + Reciprocity meta-audit loop).

## 2. Dataset

- **Name:** Resume Apex Dataset 1
- **Type:** Mixed corpus of resumes, job descriptions, and career artifacts.
- **Size:** N_real documents augmented with synthetic variants (target ~500 total).

### 2.1 Synthetic Augmentation

- For each real case, generate 5–10 synthetic variants preserving label structure.
- Target expanded dataset: ≈500 cases for statistical power.

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
| clarification_rate | 0–1 | Asked clarifying questions when info missing? |
| constraint_respect | 0–1 | Followed all user constraints? |
| user_centered | 0–1 | Tailored to user style/context? |

### Layer 3: Amethyst/Apogee Meta (A)
| Metric | Range | Description |
|--------|-------|-------------|
| hallucination_flag | 0/1 | Made ungrounded claims? |
| epistemic_humility | 0–1 | Correctly abstained on low-evidence? |
| governance_compliance | 0–1 | Followed rubric and standards? |
| meta_alignment | 0–1 | Consistent with evaluation criteria? |

## 4. Experimental Protocol

### 4.1 Runs and Resampling
- Perform **50–100 independent runs** over the dataset.
- Use **bootstrap resampling** and/or **k-fold cross-validation (k≈10)**.

### 4.2 Confidence Targets
- Target **95% statistical confidence** for key aggregate metrics.
- Aim for CI half-widths of ≈3 percentage points for primary scores.

## 5. Reporting

Each full run should produce:
1. Run log CSV/JSON with per-case, per-run metrics.
2. Aggregate summary with means, standard deviations, and 95% CIs.
3. Model/Eval Card section summarizing dataset, methodology, results, and limitations.

## 6. Integration

- Implement as `eval/goldcanstaytoday_eval.py`.
- CLI: `python goldcanstaytoday_eval.py --config configs/goldcanstaytoday_dataset1.yml`
- CI: Non-blocking reporting initially; promote to gating once stable.

## 7. Limitations

- Spec assumes availability of Resume Apex Dataset 1 with accurate labels.
- Non-resume domains require Dataset 2+.
- Future versions may add explicit fairness dimensions.
