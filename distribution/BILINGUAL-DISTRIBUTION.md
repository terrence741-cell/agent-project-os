# Bilingual distribution contract

[简体中文](BILINGUAL-DISTRIBUTION.zh-CN.md)

## Decision

Agent Project OS ships as two complete, language-specific packages with the same six Skills and the same behavioural contract:

| Package | Audience | Role |
| --- | --- | --- |
| `agent-project-os` | Chinese-speaking users | Canonical primary package |
| `agent-project-os-en` | International users | English localized package |

The Chinese package is canonical because Chinese is the product’s primary user language. “Canonical” identifies the source language for behavioural and wording changes; it does not imply that the English package is less complete or less supported. The packages use distinct names so that a marketplace can list both without an identifier collision. They are alternatives and should not be installed together because they expose the same Skill names.

## One behavioural source, two language surfaces

The source of truth for Skill behaviour is each canonical Chinese `SKILL.md` under `plugins/agent-project-os/skills/`. The English package is a complete human-reviewed localization of the same file. It may localize examples, natural-language triggers, headings, and user-facing prompts, but it may not change behaviour.

The following must remain equivalent across the two packages:

- the six Skill names and their routing relationships;
- the on-demand trigger boundary and the instruction to stay out of ordinary project work;
- first-run examples, including the rule that users need not learn Skill names first;
- read/write boundaries and confirmation gates;
- required output shapes and safety guardrails;
- manifest version, license, and compatible host targets;
- every release-blocking L0–L4 behavioural test.

A translation must not silently add a workflow, broaden a permission, turn a suggestion into a write, or remove a known limitation. Any behavioural change starts in the canonical package, receives its own test evidence, and is then localized for English.

## Repository layout

```text
.
├── plugins/
│   ├── agent-project-os/           # canonical Chinese package
│   └── agent-project-os-en/        # complete English package
└── distribution/
    ├── BILINGUAL-DISTRIBUTION.md   # this contract
    └── release-manifest.json       # version and parity checklist
```

Each package contains `skills/`, `.codex-plugin/`, `.claude-plugin/`, `README.md`, `CHANGELOG.md`, `LICENSE`, and `docs/VALIDATION.md`. The repository Marketplace offers both packages, but users must install exactly one.

## Version and release protocol

`distribution/release-manifest.json` coordinates a release; it is not a second product specification. Before a bilingual release:

1. Update the canonical package and record the relevant L0–L4 evidence.
2. Set both package versions to the same release version in the manifest.
3. Localize or refresh the English package from that exact canonical revision.
4. Check file inventories, Skill names, licenses, and manifest versions.
5. Verify both repository Marketplace manifests and fresh-install guidance for Codex and Claude Code.
6. Run the release-blocking behavioural cases against both language surfaces.
7. Publish both packages from the same Git tag, or publish neither.

Wording-only patches still require a parity review. A change to `SKILL.md`, a manifest, or the distribution layout triggers the relevant rows in the regression suite; it does not reset unrelated L2–L4 evidence.
