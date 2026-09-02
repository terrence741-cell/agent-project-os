#!/usr/bin/env python3
"""Check that Codex and Claude package workflows stay in sync."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CODEX_PACKAGE = ROOT / "plugins" / "agent-project-os"
CLAUDE_PACKAGE = ROOT / "plugins" / "agent-project-os-claude"
SKILLS = (
    "bootstrap-workspace",
    "launch-project",
    "project-os",
    "review-portfolio",
    "review-project-structure",
    "state-handoff",
)
EXPLICIT_SKILLS = ("project-os", "state-handoff")


def fail(message: str) -> None:
    raise SystemExit(f"HOST_PACKAGE_PARITY_FAIL: {message}")


def split_frontmatter(path: Path) -> tuple[str, str]:
    contents = path.read_text(encoding="utf-8")
    if not contents.startswith("---\n"):
        fail(f"missing frontmatter: {path}")
    marker = contents.find("\n---\n", 4)
    if marker < 0:
        fail(f"unclosed frontmatter: {path}")
    return contents[4:marker], contents[marker + 5 :]


def resource_files(skill_root: Path) -> dict[str, bytes]:
    resources: dict[str, bytes] = {}
    for path in sorted(skill_root.rglob("*")):
        if not path.is_file() or path.name in {"SKILL.md", ".DS_Store"}:
            continue
        relative = path.relative_to(skill_root)
        if relative.parts[0] == "agents":
            continue
        resources[relative.as_posix()] = path.read_bytes()
    return resources


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        fail(f"invalid JSON {path}: {error}")


def check_package_boundaries() -> None:
    if (CODEX_PACKAGE / ".claude-plugin").exists():
        fail("Codex package contains .claude-plugin")
    if (CLAUDE_PACKAGE / ".codex-plugin").exists():
        fail("Claude package contains .codex-plugin")
    if list(CLAUDE_PACKAGE.glob("skills/*/agents/openai.yaml")):
        fail("Claude package contains agents/openai.yaml")


def check_workflows() -> None:
    for skill in SKILLS:
        codex_root = CODEX_PACKAGE / "skills" / skill
        claude_root = CLAUDE_PACKAGE / "skills" / skill
        codex_frontmatter, codex_body = split_frontmatter(codex_root / "SKILL.md")
        claude_frontmatter, claude_body = split_frontmatter(claude_root / "SKILL.md")

        if codex_body != claude_body:
            fail(f"workflow body drift: {skill}")
        if resource_files(codex_root) != resource_files(claude_root):
            fail(f"workflow resource drift: {skill}")

        if skill in EXPLICIT_SKILLS:
            if "disable-model-invocation:" in codex_frontmatter:
                fail(f"Codex frontmatter contains Claude-only field: {skill}")
            if claude_frontmatter.count("disable-model-invocation: true") != 1:
                fail(f"Claude explicit policy missing or duplicated: {skill}")
            if "user-invocable:" in claude_frontmatter:
                fail(f"Claude explicit skill must not set user-invocable: {skill}")
            openai_adapter = codex_root / "agents" / "openai.yaml"
            if not openai_adapter.is_file():
                fail(f"Codex explicit adapter missing: {skill}")
            if "allow_implicit_invocation: false" not in openai_adapter.read_text(
                encoding="utf-8"
            ):
                fail(f"Codex explicit policy missing: {skill}")
        elif "disable-model-invocation:" in claude_frontmatter:
            fail(f"Claude automatic skill unexpectedly disabled: {skill}")


def check_distribution_contract() -> None:
    codex_manifest = load_json(CODEX_PACKAGE / ".codex-plugin" / "plugin.json")
    claude_manifest = load_json(CLAUDE_PACKAGE / ".claude-plugin" / "plugin.json")
    codex_marketplace = load_json(ROOT / ".agents" / "plugins" / "marketplace.json")
    claude_marketplace = load_json(ROOT / ".claude-plugin" / "marketplace.json")
    release_manifest = load_json(ROOT / "distribution" / "release-manifest.json")

    expected_name = "agent-project-os"
    versions = {
        str(codex_manifest.get("version", "")),
        str(claude_manifest.get("version", "")),
        str(claude_marketplace.get("version", "")),
        str(claude_marketplace.get("plugins", [{}])[0].get("version", "")),
        *(str(item.get("version", "")) for item in release_manifest.get("packages", [])),
    }
    if "" in versions or len(versions) != 1:
        fail(f"manifest version drift: {sorted(versions)}")
    if codex_manifest.get("name") != expected_name or claude_manifest.get("name") != expected_name:
        fail("host plugin name drift")

    codex_plugins = codex_marketplace.get("plugins", [])
    claude_plugins = claude_marketplace.get("plugins", [])
    if len(codex_plugins) != 1 or codex_plugins[0].get("source", {}).get("path") != "./plugins/agent-project-os":
        fail("Codex marketplace source drift")
    if len(claude_plugins) != 1 or claude_plugins[0].get("source") != "./plugins/agent-project-os-claude":
        fail("Claude marketplace source drift")

    release_hosts = {
        (item.get("host"), item.get("source")) for item in release_manifest.get("packages", [])
    }
    if release_hosts != {
        ("codex", "plugins/agent-project-os"),
        ("claude-code", "plugins/agent-project-os-claude"),
    }:
        fail(f"release package inventory drift: {sorted(release_hosts)}")


def main() -> None:
    check_package_boundaries()
    check_workflows()
    check_distribution_contract()
    print("HOST_PACKAGE_PARITY_PASS: 6 workflows, resources, host manifests, and release inventory match")


if __name__ == "__main__":
    main()
