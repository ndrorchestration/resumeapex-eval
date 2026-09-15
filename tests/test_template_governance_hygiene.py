from pathlib import Path


TEMPLATE_PATHS = (
    Path(".github/pull_request_template.md"),
    Path(".github/ISSUE_TEMPLATE/bug_report.md"),
    Path(".github/ISSUE_TEMPLATE/feature_request.md"),
)

FORBIDDEN_CURRENT_AUTHORITY_PHRASES = (
    "Governed by DGAF-Framework",
    "Governed by [DGAF-Framework]",
    "Meta-orchestrated by Agent Amethyst",
    "DGAF-certified",
)


def test_current_github_templates_do_not_emit_superseded_authority_claims():
    for path in TEMPLATE_PATHS:
        text = path.read_text(encoding="utf-8")
        for phrase in FORBIDDEN_CURRENT_AUTHORITY_PHRASES:
            assert phrase not in text, f"{path} still emits superseded authority phrase: {phrase}"
