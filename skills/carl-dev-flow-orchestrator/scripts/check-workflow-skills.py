#!/usr/bin/env python3

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import NoReturn

ROOT = Path(__file__).resolve().parents[2]

SKILL_VERSION = "1.4.0"

EXPECTED = {
    "carl-dev-flow-orchestrator": {
        "required": [
            f"version: {SKILL_VERSION}",
            "let the user make the final decision",
            "keep this skill short and structural",
            "keep detailed stage procedures only in subskills",
            "Artifact location convention",
            "State convention",
            ".carl/",
            "review conclusions stay with `Hephaestus`",
            "must never delegate review work to `Oracle`",
            "do not override intra-stage autonomous progression",
        ],
        "forbidden": [
            "requirements draft",
            "technical spec draft",
        ],
    },
    "carl-dev-flow-stage-router": {
        "required": [
            f"version: {SKILL_VERSION}",
            "If no workflow artifacts exist yet, default to `requirements-development`.",
            "must never delegate review work to `Oracle`",
        ],
        "forbidden": [],
    },
    "carl-dev-flow-requirements": {
        "required": [
            f"version: {SKILL_VERSION}",
            "This skill is the authoritative source for the detailed procedure of the `requirements-development` stage",
            "The reviewer of record is `Hephaestus`",
            "stateful interaction behavior when conversations, edits, or branching flows exist",
            "side effects, suppression rules, or failure semantics when external actions or notifications exist",
            "Artifact location",
            ".carl/requirements/",
            "Requirements format guidance",
            "Pre-draft interrogation",
            "Convergence rule",
        ],
        "forbidden": [
            "thread and edit behavior if messaging is involved",
            "notification suppression or failure semantics if alerts are involved",
        ],
    },
    "carl-dev-flow-tech-spec": {
        "required": [
            f"version: {SKILL_VERSION}",
            "This skill is the authoritative source for the detailed procedure of the `technical-confirmation` stage",
            "The reviewer of record is `Hephaestus`",
            "Artifact location",
            ".carl/tech-spec/",
            "ADR guidance",
            "rejected alternatives documented as ADR",
            "Bug-fix adaptation",
        ],
        "forbidden": [],
    },
    "carl-dev-flow-implementation": {
        "required": [
            f"version: {SKILL_VERSION}",
            "This skill is the authoritative source for the detailed procedure of the `development-execution` stage",
            "`Hephaestus` reviews integrated changes in parallel",
            "Artifact location",
            ".carl/implementation/",
            "Pre-edit checklist",
            "Bug-fix adaptation",
            "Execution modes",
            "Slice decomposition",
            "slices.md",
            "must never delegate review work to `Oracle`",
        ],
        "forbidden": [],
    },
    "carl-dev-flow-review-loop": {
        "required": [
            f"version: {SKILL_VERSION}",
            "This skill is the authoritative source for the detailed procedure of the `recursive-improvement` stage",
            "code-review-expert",
            "requesting-code-review",
            "Artifact location",
            ".carl/review/",
            "Bug-fix adaptation",
            "after `Hephaestus` has written the findings",
            "Do not delegate the review itself to `Oracle` or any other agent",
            "Within the review-fix-re-review cycle, `Sisyphus` proceeds autonomously",
        ],
        "forbidden": [],
    },
    "carl-dev-flow-bugfix": {
        "required": [
            f"version: {SKILL_VERSION}",
            "Bug severity grading",
            "Bug-fix principles",
            "Artifact location",
            ".carl/bugfix/",
        ],
        "forbidden": [],
    },
}

FRONTMATTER_KEYS = ("name:", "description:", "version:", "compatibility:", "license:", "metadata:")
SKILL_NAMES = tuple(EXPECTED.keys())
EXPECTED_LICENSE = "CC-BY-4.0"
EXPECTED_COMPATIBILITY = "opencode"
METADATA_KEYS = ("audience:", "domain:")


def fail(message: str) -> NoReturn:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def parse_frontmatter(text: str, path: Path) -> str:
    text = text.replace("\r\n", "\n")
    if not text.startswith("---\n"):
        fail(f"{path}: missing frontmatter start")
    parts = text.split("\n---\n", 1)
    if len(parts) != 2:
        fail(f"{path}: missing frontmatter end")
    return parts[0]


def extract_frontmatter_value(frontmatter: str, key: str, path: Path) -> str:
    match = re.search(rf"^{re.escape(key)}:\s*(.+)$", frontmatter, re.MULTILINE)
    if match is None:
        fail(f"{path}: missing {key} value")

    value = match.group(1).split("#", 1)[0].strip().strip('"').strip("'")
    if not value:
        fail(f"{path}: empty {key} value")
    return value


def ensure_version_consistency(versions: set[str]) -> None:
    if versions != {SKILL_VERSION}:
        fail(f"version mismatch across workflow skills: {sorted(versions)} (expected {SKILL_VERSION})")


def check_file(skill_name: str, config: dict[str, list[str]]) -> str:
    path = ROOT / skill_name / "SKILL.md"
    if not path.exists():
        fail(f"missing expected file: {path}")

    text = path.read_text(encoding="utf-8")
    frontmatter = parse_frontmatter(text, path)

    for key in FRONTMATTER_KEYS:
        if key not in frontmatter:
            fail(f"{path}: missing frontmatter key {key}")

    for key in METADATA_KEYS:
        if key not in frontmatter:
            fail(f"{path}: missing metadata key {key}")

    name = extract_frontmatter_value(frontmatter, "name", path)
    version = extract_frontmatter_value(frontmatter, "version", path)
    compatibility = extract_frontmatter_value(frontmatter, "compatibility", path)
    license_name = extract_frontmatter_value(frontmatter, "license", path)

    if name != skill_name:
        fail(f"{path}: frontmatter name {name!r} must match directory name {skill_name!r}")

    if compatibility != EXPECTED_COMPATIBILITY:
        fail(f"{path}: compatibility must be {EXPECTED_COMPATIBILITY!r}, got {compatibility!r}")

    if license_name != EXPECTED_LICENSE:
        fail(f"{path}: license must be {EXPECTED_LICENSE!r}, got {license_name!r}")

    for needle in config["required"]:
        if needle not in text:
            fail(f"{path}: missing required text: {needle}")

    for needle in config["forbidden"]:
        if needle in text:
            fail(f"{path}: contains forbidden text: {needle}")

    return version


EXPECTED_TEMPLATES: dict[str, list[str]] = {
    "carl-dev-flow-orchestrator": ["minimal-zh.md"],
    "carl-dev-flow-stage-router": ["minimal-zh.md", "zh_CN_INVOCATION.md"],
    "carl-dev-flow-requirements": ["requirements-draft.md"],
    "carl-dev-flow-tech-spec": ["tech-spec-draft.md", "adr-template.md"],
    "carl-dev-flow-implementation": ["task-plan.md", "slices.md"],
    "carl-dev-flow-review-loop": ["review-memo.md"],
    "carl-dev-flow-bugfix": ["minimal-zh.md"],
}


def check_chinese_templates() -> None:
    for skill_name in SKILL_NAMES:
        path = ROOT / skill_name / "templates" / "minimal-zh.md"
        if not path.exists():
            fail(f"missing expected Chinese template: {path}")


def check_templates() -> None:
    """Verify that expected template files exist in each skill's templates/ directory."""
    for skill_name, templates in EXPECTED_TEMPLATES.items():
        template_dir = ROOT / skill_name / "templates"
        for template in templates:
            path = template_dir / template
            if not path.exists():
                fail(f"missing expected template: {path}")


def main() -> int:
    versions = set()
    for skill_name, config in EXPECTED.items():
        versions.add(check_file(skill_name, config))

    ensure_version_consistency(versions)
    check_chinese_templates()
    check_templates()
    print(
        f"Workflow skill family check passed: {len(EXPECTED)} files verified, "
        f"{sum(len(t) for t in EXPECTED_TEMPLATES.values())} templates validated, "
        f"required wording present, forbidden wording absent, versions consistent."
    )
    return 0

if __name__ == "__main__":
    sys.exit(main())
