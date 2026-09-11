# Security Policy

## Reporting a vulnerability

Do **not** open a public GitHub issue for suspected vulnerabilities, exposed credentials, private benchmark data, sensitive career documents, or exploit details.

Prefer GitHub's private vulnerability-reporting path for this repository when it is enabled. If unavailable, contact the maintainer through a private channel associated with the GitHub account and provide only the minimum information needed to reproduce the problem. Never paste secrets or personal resume/CV content into public issues, pull requests, screenshots, or logs.

No response-time SLA is promised by this document.

## Data and credential boundary

The public fixture in this repository is synthetic/known-answer data used to verify the evaluator machinery. Real personal resumes, CVs, applications, private employer correspondence, identity records, or private corpus contents must not be committed unless deliberately sanitized for repository use.

Provider/API credentials, storage tokens, and private dataset access material must remain outside the repository and outside generated run artifacts.

## Evidence boundary

The deterministic CI harness establishes evaluator/fixture reproducibility for the checks it executes. It does not establish model security, private-corpus safety, benchmark validity, external certification, production readiness, or absence of vulnerabilities.

Security and privacy claims must remain scoped to the exact code, data path, runtime, and deployment evidence under review.
