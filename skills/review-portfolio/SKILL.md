---
name: review-portfolio
description: Review a portfolio of projects from a thin project index to surface cross-project blockers, stale status, conflicts, and reuse opportunities. Use when a user asks for a project portfolio review, global project health check, or cross-project prioritization. Read indexes and summaries first, remain read-only by default, and do not create a second source of project truth.
---

# Review Portfolio

Review the relationships between projects without turning the review into a new project database. The portfolio view is a routing and decision aid; each project remains the source of truth for its own status and work.

## 1. Establish the review lens

Ask for or confirm:

- the workspace root and authorized project index or entry point;
- the review purpose (for example: unblock delivery, detect stale work, or find reuse);
- the relevant time range and what “stale” means in that context;
- any projects, folders, or sensitive areas excluded from the review.

Default to read-only. If no thin index is available, do not scan every project. Ask for a bounded set of project entries or propose the minimum index fields needed: project name, type, status summary, last-updated date, entry path, and optional owner/dependency/tags.

## 2. Read thin evidence before project content

Start with the workspace project navigation, index entries, frontmatter, or status summaries explicitly in scope. Record the source for every observation.

Do not load every project body. Only request or read a single project’s specific source when index evidence is insufficient for a direct, decision-relevant question. State the reason for that down-drill and preserve the user’s scope restrictions.

## 3. Assess cross-project signals

Use only supported evidence to identify:

| Signal | What counts as evidence | Handling |
| --- | --- | --- |
| Blocker | Explicit dependency, waiting state, owner bottleneck, or missing required input | Link it to the affected project entries |
| Stale risk | Last-updated date or status explicitly outside the agreed time range | State the date and threshold; do not infer abandonment |
| Conflict | Incompatible claims about a shared resource, owner, deadline, or decision | Show both sources; do not choose a winner |
| Reuse opportunity | Repeated tool, template, asset, workflow, or demonstrated capability | Describe the candidate and the projects that support it |

Missing evidence is not a negative finding. Label it “cannot determine from the index” and add a narrowly scoped down-drill question only if it would change a decision.

## 4. Produce a portfolio report, not a replacement database

Return these sections:

1. **Portfolio snapshot** — scope, review lens, and a compact count or grouping based on the index.
2. **Attention required** — blockers, stale risks, and conflicts, each with evidence and source paths.
3. **Reuse opportunities** — supported candidates, with affected projects and expected benefit.
4. **Recommended next checks** — specific project source to inspect, why, and the question it can answer.
5. **Project handoffs** — actions belong in named project sources; list where to take each one.
6. **Limits** — excluded projects, missing fields, and findings that cannot be determined.

For every action, name the project that owns it. Do not create a new canonical status table, reframe a portfolio observation as a project fact, or modify project files unless the user separately requests a specific change.

## Guardrails

- Default to read-only and a thin-index review.
- Do not recursively inspect the workspace or load all project bodies.
- Do not fabricate dates, owners, dependencies, or causes from missing fields.
- Do not resolve cross-project conflicts; report sources and ask the relevant owner to decide.
- Do not save portfolio conclusions as a competing project-truth system.
