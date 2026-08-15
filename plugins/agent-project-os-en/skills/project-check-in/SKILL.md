---
name: project-check-in
description: "Turn one explicitly requested generic project check-in into a next action and a reviewable state-update proposal. Use only for an explicit $project-check-in invocation, “do a project check-in”, or a clear request to turn one new fact or update into a state hand-off when no more specific local project protocol takes over. Do not capture ordinary continuation for a project that has a Memory route or stable entry: “continue project X”, “what should I do today?”, “update progress”, and “the client changed requirements” follow core Memory and local project rules. Require a project path and read boundary; write nothing before the user confirms the target file and exact content. Not for launching projects, comparing projects, governing Memory, reviewing structure, or judging direction, scope, or whether to continue."
---

# Project Check-in

Only when the user explicitly requests a **generic check-in**, turn a confirmed project update into one next action and a reviewable minimal state change. This is an on-demand maintenance tool, not a daily project entry point.

## 0. Applicability gate

Before starting, confirm that:

- the user explicitly invoked this Skill or asked for a generic project check-in / state hand-off;
- the project path and allowed read boundary are available; and
- no more specific local update protocol takes over, or the stable entry explicitly permits a generic check-in.

For ordinary continuation, today's plan, or a progress update, yield to core Memory and the local project protocol instead of running this Skill. If a project has its own update protocol, follow it without imposing this generic output or creating a parallel state source. If the path or read boundary is missing, ask only for that information. Do not read global Memory to guess a location or propose project state without evidence.

## 1. Establish the project boundary

Read only:

1. the stable project entry;
2. the one current-state artifact it names; and
3. a related material explicitly routed by the entry only when it is necessary for this update.

State the exact paths read. Do not scan sibling projects, the full workspace, archives, chats, or global Memory. Project evidence outranks recent conversation. Mark unsupported claims as **user-reported / awaiting confirmation**.

If the stable entry or state is missing, conflicting, or insufficient for a safe update, state exactly what could not be recovered and remain read-only. Suggest `review-project-structure` when the structure itself needs inspection, or `launch-project` when a minimal structure must be established or repaired, but do not perform either workflow here.

## 2. Process the explicit update

Handle only the progress, blocker, decision, changed constraint, or new fact the user explicitly supplied:

- separate existing project evidence, the user's new report, inference, and unknowns;
- state whether the update changes current state, next action, an open decision, or a blocker;
- preserve a missing unit, currency, denominator, or range instead of filling it in;
- keep an open decision open; named people or options are not automatically the complete candidate set;
- never write advice, forecasts, or Agent diagnosis as confirmed fact.

Return:

1. **What I understand**: project evidence, user report, and uncertainty.
2. **Next safe action**: exactly one action; ask one narrow question only when it blocks that action.
3. **Watch / decision**: only a material dependency, risk, or owner decision.
4. **Proposed state update**: target path, exact added or replacement text, source for each new fact, and the minimum needed for a fresh session to resume.

Do not create a daily log, template, second state file, or any parallel source of truth for one check-in.

## 3. Write only after confirmation

Display the exact target file and exact change, then wait. Continue only after the user confirms both.

Reread the target before writing and apply only the confirmed minimum. Preserve conflicts, unknowns, and unconfirmed claims. Report the exact path, actual change, and next continuation point afterward.

Before confirmation, create, modify, move, or delete no project file. Never update Workspace Memory, an index, Portfolio, or an unrelated project. A durable cross-project lesson may only become a candidate for `bootstrap-workspace`; never promote it here.

## Boundaries

- Do not judge project direction, scope, whether its goal remains appropriate, or whether to continue. State that such a question is outside this Skill.
- Do not compare projects, review structure, or launch or reorganize a project.
- Do not diagnose, decide, send, schedule, publish, or take external action for the user.
- Keep sensitive personal, health, child, client, personnel, or financial facts in the approved project scope using the smallest necessary summary.
- Exit when complete. Ordinary later work continues through Memory and the local project protocol.
