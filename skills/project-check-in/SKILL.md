---
name: project-check-in
description: Move one in-progress non-code project forward from a single update. Use when the user reports what happened, hits a blocker, makes a decision, learns something new, or asks what to do next — "今天做了这些"、"客户改需求了"、"卡住了推不动"、"接下来该干嘛"、"更新一下进度"、"这周安排一下". Always gives one concrete next action, even when no project path has been named yet. Once the user names a project, reads only that project's own entry and current-status files and proposes a small status edit, which it does not write until the user approves. Not for starting a project, comparing several projects, or governing long-term memory. It also does not judge direction, scope, or whether the work is still worth doing — when that is what the user is really asking, say so rather than answering it with a next action.
---

# Project Check-in

Turn today’s work into the next safe move without creating a second project truth. Keep the check-in narrow: interpret the user’s update against the project’s stable contract and current operating state, then leave a small, confirmed handoff for the next session.

## 1. Establish the project boundary

Confirm the project root and the files or folders that may be read. If the user supplied a specific project path and has authorized that project, treat that as the read boundary; otherwise follow **Respond before the boundary exists** below.

- Read only the project contract/stable entry and the current running-state artifact named by it. Follow an additional material route only when it is necessary to understand this specific update.
- State the exact paths read. Do not scan sibling projects, the full workspace, archives, chats, or global Memory.
- Treat project evidence as stronger than remembered conversation. Mark a claim that has no supporting project evidence as **user-reported / awaiting confirmation**, not as an established fact.
- Do not create a missing contract, status file, daily log, or template during a check-in.

### Respond before the boundary exists

A missing project path blocks reading and writing. It does not block helping. When the user describes a real situation without naming a project, do not make the request for a path the only content of the response.

In the same response:

1. **Act on what the user actually said.** Give one concrete action they can take now, derived only from their own words and any stated constraint such as available time, deadline, or overrun. A generic method the user can apply without project evidence is legitimate here.
2. **Mark the basis.** State plainly that the suggestion comes from their description and has not been checked against project files. Every fact they reported stays **user-reported / awaiting confirmation**.
3. **Ask for the path as a secondary item.** Request it to ground the next round, not as a precondition for this one.

While no read boundary is established:

- Propose no state update. Section 5's closing proposal does not apply until a project scope exists; an unconfirmed path or invented target is never an acceptable substitute. Section 3's fourth item still appears, carrying the one-sentence declaration that no proposal is made yet — that declaration is not itself a proposal.
- Read no project file, index, archive, or Memory to compensate for the missing path.
- Present no suggestion, estimate, or diagnosis as an established project fact, and do not infer that work is unstarted, complete, unowned, or blocked.

Section 4's escalation test still applies in this state, with two adjustments. Read "evidence" there as the user's own account, which you cite as such rather than as project evidence. When that test fires, add the mid-course review as an offer alongside the check-in above; do not replace the check-in with it, and do not withhold the immediate action while the user decides. When the test does not fire, do not raise the review at all.

Section 2's Skill recommendation is suspended in this state. Choosing between `launch-project` and `review-project-structure` requires knowing the project's maturity, which cannot be inferred here. Ask for the path instead.

## 2. Recover only the context needed now

Locate, if available:

- the project objective, scope, roles, privacy/write boundary, and material routes;
- the current phase or period, confirmed facts, next action, open decisions, blockers, and context still to complete;
- only the source that bears on the update, such as a named decision, deliverable, or current queue item.

If the contract or current-state artifact is absent, incomplete, conflicting, or outside the approved scope, say exactly what could not be recovered. Ask only for the smallest fact needed to help with the current update. Do not infer that work is unstarted, complete, unowned, or blocked.

When the missing artifact prevents safe resumption rather than merely this answer, recommend `launch-project` for an under-structured project or `review-project-structure` for a mature project. Keep that recommendation read-only; do not launch or restructure it from this Skill. This paragraph applies only once a read boundary exists; with no boundary, section 1 suspends it.

## 3. Process the update

Classify the user’s input without expanding it into a generic project interview:

| Update kind | Check-in response |
| --- | --- |
| Progress or completed work | Identify what changed, what remains, and the next smallest action. |
| Blocker or delay | Separate confirmed blocker, missing evidence, and decision needed; propose an unblock action. |
| Decision or changed constraint | State its project impact and the smallest affected state item. Do not silently overwrite an earlier decision. |
| New fact or observation | Label the source and confidence; identify whether it changes the current plan. |
| Request for today's plan | Use current state plus the stated availability/constraint; do not invent priorities or deadlines. |

An update may match more than one row. Handle every row it matches inside the single response; do not pick one and drop the rest, and do not split the check-in into multiple rounds because of this.

Preserve the informational shape of every user-reported fact:

- If a number has no stated unit, currency, denominator, or range meaning, keep it unitless and mark the missing part rather than supplying a likely one.
- Keep an open decision open. Mentioned people, options, or examples are not an exhaustive candidate set unless the user explicitly says they are; do not turn “who decides?” into a choice between the people named in the update.

With no read boundary established, every row applies with the same adaptation: work only from the user's own stated situation and constraint, label that basis as such, and name no project state item as affected. Where a row calls for the smallest affected state item, describe what would likely need updating once the path is known, without asserting it.

Return a concise check-in with:

1. **What I understand** — user-reported update, grounded project context, and any uncertainty. With no read boundary, say plainly that no project file was read, and leave the grounded part empty rather than filling it by inference.
2. **This-session next action** — exactly one concrete action that can be done now. It may be described in several steps as long as they form that single action; do not list alternatives for the user to choose among. Add a narrowly scoped question only if it blocks that action.
3. **Watch / decision** — only a material dependency, risk, or owner decision that needs attention.
4. **Proposed state update** — the smallest exact change needed for a later session to resume; include target path, proposed text or replacement, the source of every new fact, and enough information for a fresh session to identify confirmed facts, open items, next action, and boundaries. While no read boundary exists, keep this heading and put exactly one sentence under it saying no state update is proposed until a project path is confirmed. Never place placeholder, speculative, or invented content here.

Do not turn a suggestion, forecast, or Agent diagnosis into a confirmed project fact. Keep repeated operational updates in the project’s existing operating record; do not create a parallel diary just because the update is daily.

## 4. Escalate without overreaching

Recommend a **read-only mid-course review** when evidence indicates one or more of these:

- the stated objective, scope, success measure, owner, or decision boundary has changed or conflicts with the project contract;
- the same blocker, missed cadence, or workaround recurs and the current next action no longer resolves it;
- priorities, resources, assumptions, or strategy must be traded off across several current items;
- the user explicitly asks whether to keep, change, pause, or re-plan the work.

Explain the trigger and the evidence, then offer a read-only review of goals, scope, rhythm, blockers, and strategy. The review is an offer, not a substitute: still give this session's next action, so the user is not left waiting on a decision about the review. Drop the check-in's own next action only when the user asks for the review instead. Do not write a re-plan, revise the contract, or promote a review conclusion to fact unless the user later confirms a specific change.

For sensitive personal, health, child, client, personnel, financial, or private information:

- use the smallest necessary summary and avoid reproducing identifiers or unnecessary details;
- keep it inside the approved project scope and never propose it for workspace Memory, Portfolio, or external action;
- distinguish practical support from medical, legal, school, mental-health, or other professional decisions; flag when qualified help or the owner’s decision is needed;
- ask before recording sensitive information when the user has not expressly asked to preserve it.

## 5. Propose, then wait before state changes

End every check-in that has an established read boundary with a minimal state-update proposal. It may add a confirmed outcome, replace the next action, record a blocker, resolve one item of context to complete, or add a dated operating entry only when the existing project design calls for one. When no boundary exists yet, section 1 governs: give help, propose nothing.

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
