# Resume Apex Dataset 1 — Dataset Card v1

**Version:** 1.0.0  
**Original date:** 2026-04-08  
**Current epistemic status:** Defined / provenance and execution incomplete  
**Last epistemic review:** 2026-08-30

## Overview

- **Name:** Resume Apex Dataset 1
- **Purpose:** Benchmark resume/career AI assistance
- **Size:** Real-case count not established in this repository; approximately 500 total cases is a design target after synthetic augmentation
- **Tasks:** Resume generation, job matching, career path analysis

## Composition

- Real resumes/job descriptions and career artifacts, subject to provenance and authorization constraints
- Synthetic variants preserving intended label structure (5–10 per eligible real case is the design target)
- Intended annotations: `task_success`, `hallucination_flag`, `clarification_behavior`, `constraint_respect`, `meta_alignment`

## Current Evidence State

The dataset card defines the intended corpus and annotation schema. It does **not** establish that the full dataset is currently present, that the target sample size has been reached, or that labels have been independently verified.

## Provenance and Access

- The dataset is not publicly released.
- Historical documentation states that access is governed by an AOC Library agreement.
- Any future benchmark claim must bind the evaluated run to an exact dataset identity/version and document the permitted provenance.

## Limitations

- Resume domain only; broader domains require additional datasets.
- Synthetic generation requires a documented and reproducible augmentation protocol.
- Real-case count and completed corpus are not established by this repository alone.
- Dataset availability does not imply benchmark validity; validity depends on the complete evaluation apparatus and reproducible results.
