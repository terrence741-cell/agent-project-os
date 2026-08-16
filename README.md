# Agent Project OS

An on-demand toolkit for setting up and repairing durable Memory and Markdown project structures for Codex and Claude Code. Once the structure works, the plugin stays out of normal project work.

[简体中文](README.zh-CN.md)

## Use it when

- you want an Agent to remember stable preferences or where projects live;
- you are starting a project, taking over a messy one, or organizing scattered files;
- a project has become hard for a fresh Agent session to understand;
- you want to compare several Markdown projects; or
- the project has no local update protocol and you explicitly want a generic status review that proposes changes first; or
- you do not know which Project OS tool fits.

Do not invoke it merely to continue a known project, write an article, analyze a document, or do the project's ordinary work. In those cases, your Agent should follow its Memory to the project's stable entry and current-status file, then work directly.

## First run

After installing one language package, describe the setup or repair you need in ordinary language:

```text
Help me set up long-term Memory for my work and projects.
Set up one long-term Memory that Codex and Claude Code can share.
Start a new research project and give it a structure a fresh Agent can resume.
Organize these scattered notes into a maintainable project.
Review this project's structure; do not edit anything yet.
Compare these four projects and tell me which one is blocked.
```

Read-only workflows may inspect files within a supplied or authorized scope. Before any write, the Agent shows the exact target and proposed content. Project files and Workspace Memory have separate confirmation gates. A new project's Memory route is only a proposal until you approve that exact Memory change.

For a new user, the default proposal is one tool-neutral physical store at `~/.agent-project-os/shared-memory/`. A thin `MEMORY.md` routes to confirmed user, team, project, feedback, and reference topic files created only when needed. Thin Codex and Claude Code entry points reach the same physical store; the system never pretends that copying or dual writes are synchronization. Paths, files, host rules, links, proven host read/write permissions, and local Git recovery are listed as separate exact changes before you approve them.

## Packages

| Working language | Install exactly this package |
| --- | --- |
| 中文 | `agent-project-os` |
| English | `agent-project-os-en` |

Do not install both; they deliberately expose the same Skill names.

This branch is a V1.0.2 release candidate. Both repository Marketplace manifests are present, but the final public GitHub installation commands will be published only after they have been tested from the real repository URL in fresh Codex and Claude Code environments. Until then, use the host's local Marketplace/source flow with this repository and select exactly one package.

Package details:

- [English package](plugins/agent-project-os-en/README.md)
- [Chinese package](plugins/agent-project-os/README.md)
- [Bilingual distribution contract](distribution/BILINGUAL-DISTRIBUTION.md)

## What remains after setup

The useful result is not a permanently active router. It is a small set of ordinary files the host Agent can use without this plugin:

```text
Workspace Memory or exact project path -> thin host adapter -> stable project entry -> current-status source -> ordinary Agent work
```

For strict path-only continuation, `launch-project` may propose a minimal root adapter: `AGENTS.md` for Codex and `CLAUDE.md` for Claude Code. Each only points to the same tool-neutral stable entry and tells the host to read it before scanning; it never stores project status.

Call Project OS again only when that structure needs to be created, reviewed, or repaired.

Apache-2.0. See the package licenses.
