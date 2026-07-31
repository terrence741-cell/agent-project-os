---
name: project-check-in
description: Turn one user update about an existing Markdown project into a grounded next action and a minimal, reviewable state-update proposal. Use when a user reports progress, a blocker, a decision, a new fact, or asks what to do next in a project already in progress. Read only the user-approved project scope and its contract/current-state artifacts; do not use to launch a project, run a portfolio review, or write state before explicit confirmation.
---

# Project Check-in

Turn today’s work into the next safe move without creating a second project truth. Keep the check-in narrow: interpret the user’s update against the project’s stable contract and current operating state, then leave a small, confirmed handoff for the next session.

## 1. Establish the project boundary

Confirm the project root and the files or folders that may be read. If the user supplied a specific project path and has authorized that project, treat that as the read boundary; otherwise ask one concise question before reading.

- Read only the project contract/stable entry and the current running-state artifact named by it. Follow an additional material route only when it is necessary to understand this specific update.
- State the exact paths read. Do not scan sibling projects, the full workspace, archives, chats, or global Memory.
- Treat project evidence as stronger than remembered conversation. Mark a claim that has no supporting project evidence as **user-reported / awaiting confirmation**, not as an established fact.
- Do not create a missing contract, status file, daily log, or template during a check-in.

## 2. Recover only the context needed now

Locate, if available:

- the project objective, scope, roles, privacy/write boundary, and material routes;
- the current phase or period, confirmed facts, next action, open decisions, blockers, and context still to complete;
- only the source that bears on the update, such as a named decision, deliverable, or current queue item.

If the contract or current-state artifact is absent, incomplete, conflicting, or outside the approved scope, say exactly what could not be recovered. Ask only for the smallest fact needed to help with the current update. Do not infer that work is unstarted, complete, unowned, or blocked.

When the missing artifact prevents safe resumption rather than merely this answer, recommend `launch-project` for an under-structured project or `review-project-structure` for a mature project. Keep that recommendation read-only; do not launch or restructure it from this Skill.

## 3. Process the update

Classify the user’s input without expanding it into a generic project interview:

| Update kind | Check-in response |
| --- | --- |
| Progress or completed work | Identify what changed, what remains, and the next smallest action. |
| Blocker or delay | Separate confirmed blocker, missing evidence, and decision needed; propose an unblock action. |
| Decision or changed constraint | State its project impact and the smallest affected state item. Do not silently overwrite an earlier decision. |
| New fact or observation | Label the source and confidence; identify whether it changes the current plan. |
| Request for today’s plan | Use current state plus the stated availability/constraint; do not invent priorities or deadlines. |

Return a concise check-in with:

1. **What I understand** — user-reported update, grounded project context, and any uncertainty.
2. **This-session next action** — one concrete action that can be done now, plus a narrowly scoped question only if it blocks that action.
3. **Watch / decision** — only a material dependency, risk, or owner decision that needs attention.
4. **Proposed state update** — the smallest exact change needed for a later session to resume; include target path, proposed text or replacement, the source of every new fact, and enough information for a fresh session to identify confirmed facts, open items, next action, and boundaries.

Do not turn a suggestion, forecast, or Agent diagnosis into a confirmed project fact. Keep repeated operational updates in the project’s existing operating record; do not create a parallel diary just because the update is daily.

## 4. Escalate without overreaching

Recommend a **read-only mid-course review** instead of treating the issue as an ordinary check-in when evidence indicates one or more of these:

- the stated objective, scope, success measure, owner, or decision boundary has changed or conflicts with the project contract;
- the same blocker, missed cadence, or workaround recurs and the current next action no longer resolves it;
- priorities, resources, assumptions, or strategy must be traded off across several current items;
- the user explicitly asks whether to keep, change, pause, or re-plan the work.

Explain the trigger and the evidence, then offer a read-only review of goals, scope, rhythm, blockers, and strategy. Do not write a re-plan, revise the contract, or promote a review conclusion to fact unless the user later confirms a specific change.

For sensitive personal, health, child, client, personnel, financial, or private information:

- use the smallest necessary summary and avoid reproducing identifiers or unnecessary details;
- keep it inside the approved project scope and never propose it for workspace Memory, Portfolio, or external action;
- distinguish practical support from medical, legal, school, mental-health, or other professional decisions; flag when qualified help or the owner’s decision is needed;
- ask before recording sensitive information when the user has not expressly asked to preserve it.

## 5. Propose, then wait before state changes

End every check-in with a minimal state-update proposal. It may add a confirmed outcome, replace the next action, record a blocker, resolve one item of context to complete, or add a dated operating entry only when the existing project design calls for one.

Until the user explicitly confirms both the target and proposed content:

- do not create, modify, move, or delete project files;
- do not update workspace Memory, indexes, Portfolio records, or unrelated project files;
- do not state that the project has been updated.

After confirmation, reread the approved target, apply only the confirmed minimum, and report the exact path and change. Preserve conflicts and unconfirmed claims as such. State the next continuation point after the write.

## Guardrails

- Do not re-run project-launch interviews during routine updates.
- Do not substitute a recent chat message for a missing project contract or current state.
- Do not expand approved scope to find a more convenient answer.
- Do not diagnose, decide, send, schedule, enroll, publish, or otherwise act externally for the user.
- Do not create a second source of project truth or promote daily dynamics to long-term Memory. If a stable cross-project learning emerges, hand it to `bootstrap-workspace` only as a candidate with its project source, applicable scope, and confirmation or latest-review date.
