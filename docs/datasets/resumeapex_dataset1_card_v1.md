# Resume Apex Dataset 1 — Dataset Card v1

**Version:** 1.0.0  
**Date:** 2026-04-08  
**Status:** Production  

## Overview
- **Name:** Resume Apex Dataset 1
- **Purpose:** Benchmark resume/career AI assistance
- **Size:** N_real cases + synthetic augmentations (target ~500 total)
- **Tasks:** Resume generation, job matching, career path analysis

## Composition
- Real resumes/job descriptions
- Synthetic variants preserving label structure (5–10 per real case)
- Annotations: task_success, hallucination_flag, clarification_behavior, constraint_respect, meta_alignment

## Limitations
- Resume domain only (Dataset 2+ needed for broader tasks)
- Requires synthetic generation protocol for scale
- Not publicly released; governed by AOC Library agreement
