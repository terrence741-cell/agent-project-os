---
name: project-os
description: "When the user explicitly says they want to use Agent Project OS to set up or repair their project system but do not know which capability to choose, load this Skill first; do not answer or start asking on your own. For that explicit, low-frequency help only — it does not take over daily project work, pure business tasks, or requests that already name an atomic Skill."
---

# Project OS

Help choose one existing Agent Project OS Skill when the user clearly wants project-system setup or repair but does not know which capability fits. This is a low-frequency help entry, not a project manager, daily entry point, or session runtime.

## 1. Decide whether this router applies

Continue only when both are true:

1. the user clearly wants to set up, organize, inspect, or maintain their project system; and
2. the user says they do not know which Project OS capability to use, or the request is genuinely ambiguous between at least two existing capabilities.

Do not use this router for:

- ordinary continuation, today's plan, progress viewing, or status updates for a named project; follow core Memory, the stable project entry, and local project protocols;
- writing, research, analysis, development, or another concrete business task; leave it to the host Agent or a specialist Skill;
- requests that already name `bootstrap-workspace`, `launch-project`, `project-check-in`, `review-project-structure`, or `review-portfolio`;
- a clear atomic need; let its matching Skill activate directly without passing through `project-os`;
- business judgments about goals, scope, direction, or whether work remains worthwhile; this release has no matching Project OS Skill, so never disguise that request as a structure review.

If the request does not qualify, yield immediately. Read no project or Memory and offer no Project OS routing advice.

## 2. Choose only among existing capabilities

| User need | Choose |
|---|---|
| Set up, organize, or review long-term Memory, or register a project route | `bootstrap-workspace` |
| Start or take over a project, or give scattered material a minimal resumable structure | `launch-project` |
| Perform an explicitly requested generic project check-in where no local protocol takes over | `project-check-in` |
| Inspect one project's entry, sources of truth, file organization, or resumability read-only | `review-project-structure` |
| Compare multiple projects for blockers, staleness, conflicts, or reuse read-only | `review-portfolio` |

Do not invent a “mid-course direction review” or any other unavailable path. If the need is outside current capabilities, state that boundary and exit so the host Agent or another tool can respond directly.

## 3. Dispatch or clarify

If the help request already points to one capability, read that sibling `SKILL.md`, execute its first applicable step in the same response, and then exit this router. Do not return only a route label, ask the user to invoke it again, or make the chosen Skill a required gateway for the next turn.

If genuine ambiguity remains, ask one question that separates the candidate paths. For example:

> Do you need to set up long-term memory, start or organize one project, inspect one project's structure, compare several projects, or perform an explicit generic check-in?

Each option must be mutually exclusive and map to exactly one existing atomic Skill; never combine single-project and multi-project review, or any other two Skills, into one answer option. Any option the user selects must allow one direct choice without a second distinguishing question.

Stay neutral while clarifying. Do not recommend a default Skill, a default execution order, or claim that “starting with X cannot go wrong”; do not use a possible dependency to pre-judge the route for the user. Choose once after the answer. Do not begin a second interview in this Skill.

## Boundaries

- Read no workspace index, project file, Memory, folder, or conversation history while routing.
- Create, modify, move, or delete no file.
- Do not assess project state, summarize evidence, diagnose blockers, or recommend business action, a default Skill, or an execution order beyond capability selection.
- Exit after choosing one atomic Skill. Later daily work follows Memory and the local project protocol.
- The user may always bypass this router and invoke an atomic Skill directly.
