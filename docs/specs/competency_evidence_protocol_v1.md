# Competency Evidence Protocol v1

Status: DRAFT / NON-CREDENTIALING

Purpose: define a reproducible method for converting demonstrated AI-systems capability into bounded, employer-readable evidence without representing simulation results as accredited credentials, certifications, or external validation.

## Scope

This protocol assesses practical capability in six domains:

1. LLM evaluation engineering
2. Multi-agent orchestration
3. AI governance operations
4. Production Python for AI systems
5. Prompt engineering
6. Technical communication and design defense

The default pathway is diagnostic-first and portfolio-first: assess current capability, assign only missing remediation, then produce evidence-bearing artifacts.

## Evidence classes

Every claim MUST be assigned one evidence class.

- `E0 — ASSERTED`: self-description or unverified prior claim.
- `E1 — DISCUSSED`: concept explained correctly in conversation, without independent artifact evidence.
- `E2 — GUIDED`: task completed with material scaffolding, hints, or stepwise assistance.
- `E3 — INDEPENDENT_ARTIFACT`: bounded task completed with an inspectable artifact and explicit rubric.
- `E4 — ADVERSARIAL_REPLICATION`: independent artifact survives hidden variants, counterexamples, failure injection, or hostile-but-fair review.
- `E5 — EXTERNAL_VALIDATION`: evidence from an independent external assessor, employer, recognized credentialing body, or reproducible third-party review.

Resume-facing claims SHOULD normally require E3 or higher. Claims implying certification, credentialing, independent validation, or industry recognition MUST require the corresponding external evidence and MUST NOT be inferred from this protocol.

## Scoring model

Use a 0–4 performance scale for each assessed competency:

- `0`: cannot yet perform the task.
- `1`: can describe the concept but cannot reliably operationalize it.
- `2`: can complete a guided implementation.
- `3`: can independently produce a reliable artifact under stated requirements.
- `4`: can handle ambiguity, adversarial conditions, tradeoffs, failure recovery, and critique.

Each score MUST include:

- evidence class;
- confidence (`low`, `medium`, `high`);
- artifact or source reference;
- observed failure modes;
- assistance disclosure;
- assessment version;
- date;
- recommended next test.

A numeric score without those fields is not a complete assessment result.

## Assessment loop

```text
Briefing
  -> bounded task
  -> artifact submission
  -> rubric scoring
  -> adversarial review
  -> oral/design defense
  -> hidden or changed-condition variant
  -> remediation if required
  -> evidence packaging
```

The assessor SHOULD withhold some perturbations and edge cases until after the first submission to reduce benchmark gaming.

## Independence controls

To avoid conflating model-assisted work with independent candidate performance:

1. Record what instructions, examples, hints, generated code, or edits were supplied before submission.
2. Distinguish `candidate-authored`, `candidate-directed/model-assisted`, and `model-authored/candidate-reviewed` artifacts.
3. Never elevate an assisted artifact to E3 solely because the final output is correct.
4. Use at least one fresh transfer task before assigning a score of 4.
5. For implementation competencies, prefer executable tests, deterministic fixtures, logs, and reproducible commands over prose fluency.

## Failure controls

### Fluency inflation

Risk: strong vocabulary may overstate implementation capability.

Control: require operational artifacts, observable outputs, and failure handling.

### Benchmark gaming

Risk: repeated rubric exposure may reward memorization.

Control: hidden variations, changed constraints, incomplete requirements, and transfer tasks.

### Architecture without closure

Risk: elegant designs omit operational requirements.

Control: architecture tasks SHOULD include authority boundaries, observability, retries/timeouts, cost or resource constraints, escalation behavior, and a failure matrix where relevant.

### Governance theater

Risk: governance language names risks without executable accountability.

Control: governance evidence SHOULD bind:

```text
Risk -> Control -> Owner -> Evidence -> Threshold -> Escalation
```

### Self-issued credential ambiguity

Risk: simulated-course completion is represented as certification.

Control: all reports MUST state `non-official competency assessment` unless a real external credential has separately been earned and verified.

## Benchmark alignment

External frameworks MAY anchor task design but do not confer equivalence.

Examples:

- Microsoft Applied Skills uses scenario-based interactive lab assessments for specific job tasks.
- NIST AI RMF organizes AI risk management around Govern, Map, Measure, and Manage and emphasizes testing, measurement, documentation, and lifecycle risk management.

These references are used as design anchors only. A ResumeApex assessment is not a Microsoft credential, NIST endorsement, academic course credit, or certification.

## Initial competency hypotheses

These are starting hypotheses only and MUST be replaced by measured evidence.

| Domain | Starting hypothesis | Primary verification |
|---|---|---|
| AI orchestration | strong conceptual/workflow design | architecture + failure recovery lab |
| Prompt engineering | strong | controlled prompt optimization + adversarial eval |
| LLM evaluation | strong conceptual; implementation depth to verify | executable evaluation harness |
| AI governance | strong conceptual | risk/control/evidence package |
| Software engineering | intermediate/developing | typed tested service + integration test |
| Technical communication | strong | ADR + executive brief + hostile-but-fair defense |

## Recommended course sequence

1. LLM Evaluation Engineering
2. Multi-Agent Orchestration
3. AI Governance Operations
4. Production Python for AI Systems
5. Technical Communication and Portfolio Defense

Prompt-engineering evidence is embedded across Courses 1 and 2 and MAY be scored separately when sufficient controlled evidence exists.

## Diagnostic 1 — LLM Evaluation Engineering

Design an evaluation harness for a research agent that answers questions from retrieved documents. Evaluate factual grounding, citation completeness, answer relevance, refusal behavior, and prompt-injection resistance.

Required submission:

1. evaluation dimensions;
2. 0–4 scoring rubric;
3. ten test cases spanning normal, ambiguous, adversarial, and boundary behavior;
4. one Python data structure representing the cases;
5. failure taxonomy;
6. method for distinguishing retrieval failure from model hallucination.

The first submission tests the measurement model only. The full harness SHOULD NOT be built until the rubric and taxonomy survive review.

## Resume claim policy

Permitted examples after sufficient evidence:

- `Built and tested an LLM evaluation harness covering grounding, citation completeness, relevance, refusal behavior, and prompt-injection resistance.`
- `Designed failure taxonomies and adversarial test sets for retrieval-augmented and agentic AI workflows.`
- `Mapped AI risks to controls, evidence, thresholds, and escalation paths using NIST AI RMF concepts.`

Prohibited unless independently true and verified:

- `Certified by ResumeApex`
- `DGAF-certified`
- `Microsoft-equivalent credential`
- `NIST-certified`
- any statement implying accredited course completion or independent validation when only simulated assessment exists.

## Result record minimum schema

```yaml
assessment_id: null
candidate: null
protocol: competency_evidence_protocol_v1
assessment_status: planned
credential_status: non_official_competency_assessment
domain: null
score_0_to_4: null
confidence: null
evidence_class: null
artifact_refs: []
assistance_disclosure: null
failure_notes: []
transfer_test: null
assessed_at: null
next_test: null
```

No resume-facing capability claim should be promoted from this protocol until its supporting record is populated with actual evidence.