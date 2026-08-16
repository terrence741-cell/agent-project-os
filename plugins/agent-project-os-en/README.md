# Agent Project OS English package

[中文包](../agent-project-os/README.md) · [Bilingual distribution contract](../../distribution/BILINGUAL-DISTRIBUTION.md)

Agent Project OS is an on-demand project setup and repair toolkit. It helps file-system Agents such as Codex and Claude Code establish durable Memory, launch or organize Markdown projects, and check whether a fresh session can resume them. Once the structure works, the plugin should disappear from normal work; the host Agent reads Memory and project files directly.

## Use it at these moments

- setting up long-term Memory for stable preferences, boundaries, and project locations;
- starting a project, taking over someone else's project, or organizing scattered notes;
- repairing a confusing project entry, current-status file, or source-of-truth layout;
- explicitly requesting a read-only structure review;
- explicitly comparing several projects;
- the project has no local update protocol and you explicitly request a generic status review that proposes changes first; or
- explicitly saying you do not know which of these Project OS capabilities fits.

## Do not use it for

- ordinary continuation, writing, research, execution, or delivery inside a known project;
- merely asking what to do next in one project;
- work that already has a known project path and a clear task; or
- automatically copying daily chats, progress, or temporary blockers into Memory.

Normal continuation should follow:

```text
Workspace Memory or exact project path -> thin host adapter -> stable project entry -> current-status source -> host Agent works directly
```

Once that route works, Agent Project OS is not required again.

## First run

You do not need to memorize Skill names. Describe the real need after installation:

```text
Help me set up long-term Memory for how I work and where my projects live.
Start a client-delivery project that a fresh session can resume next time.
These materials are scattered across folders; organize them into a project.
Review this project's structure, but do not edit anything yet.
Compare these projects and tell me which is blocked or stale.
This project has no update protocol. Run a generic status review, propose the status changes, and do not write them yet.
```

If the need itself is unclear, say:

```text
I want to use Agent Project OS to organize this, but I do not know which capability fits.
```

Only that explicit uncertainty calls for the low-frequency `project-os` router.

## Safety boundaries

- A workflow that may write first shows the exact target path and proposed content, then waits for confirmation.
- Project-file writes and Workspace Memory writes require separate confirmations.
- `launch-project` creates only a Memory route candidate. `bootstrap-workspace` must check conflicts and obtain separate confirmation before registering it in Memory.
- Structure review remains read-only. An approved repair is executed later by `launch-project` in a separate, explicit workflow.
- Project status, temporary blockers, client details, and sensitive facts remain in the project rather than long-term Memory.
- Without a project path, the plugin does not pretend it checked the project or invent ordinary day-to-day project action.
- For strict path-only continuation, `launch-project` separately proposes Codex `AGENTS.md` or Claude Code `CLAUDE.md`. Each only routes to the same stable entry, never copies project status, and still requires confirmation before writing.

## Install

This package is named `agent-project-os-en` and is intended for English working sessions. Do not install it together with `agent-project-os`; both packages expose the same Skill names.

This is a V1.0.1 release candidate. Package manifests for Codex and Claude Code are present. Final GitHub installation commands will be documented only after fresh-install testing against the real public repository URL on both hosts. For now, add the repository root through the host's local Marketplace/plugin-source flow and select `agent-project-os-en`.

The Skills are Markdown instructions under `skills/`; they include no background service or automatic network request. The host Agent may still read or modify workspace files within the scope you approve.

## Skill reference

| Skill | Use only when |
| --- | --- |
| `bootstrap-workspace` | setting up or organizing long-term Memory; confirming a project route |
| `launch-project` | starting, taking over, or organizing a project; applying an approved exact structure repair |
| `review-project-structure` | explicitly requesting a read-only review of one project's structure |
| `review-portfolio` | explicitly comparing multiple projects |
| `project-check-in` | no local update protocol exists and a generic status review is explicitly requested, or the Skill is invoked directly |
| `project-os` | explicitly unsure which Project OS capability to use |

## Status

V1.0.1 release candidate. Package structure, bilingual behaviour, on-demand triggering, Memory route handoff, and safety boundaries have passed local validation. Fresh GitHub installation on both hosts and trials with unfamiliar users remain release gates; this package is not claimed as publicly ready yet.

Apache-2.0. See [LICENSE](LICENSE).
