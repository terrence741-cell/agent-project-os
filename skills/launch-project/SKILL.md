---
name: launch-project
description: Launch, take over, or minimally organize a Markdown project so a later Agent can continue it correctly. Use when a user wants to start a project, make an under-structured project resumable, or assess an existing project before reorganizing it. First provide a read-only startup package; create or change project files only after explicit confirmation.
---

# Launch Project

Create the smallest project structure that gives a later Agent reliable continuity. Do not impose a universal folder template or treat missing details as a reason to provide no useful first response.

## 1. Establish safe read scope

Use the path and read/write boundaries the user gives. If the target path is known, inspect it read-only before proposing changes; otherwise use the project description alone and label the missing path as a blocking gap for writing.

At the project's root, look for a stable entry, current state, source material, decisions, and deliverables. State exact paths used as evidence. Do not use nested `测试`, `test`, `fixtures`, `examples`, `archive`, `归档`, vendored, or generated directories as evidence for the live project unless the user explicitly targets one.

Treat drafts, old quotations, meeting notes, and undated material as references, not current facts, unless confirmed. If the user describes existing materials outside readable scope, mark them **unknown / needs verification**; never convert them into “not started”, “no active work”, or “unassigned”.

## 2. Deliver a read-only startup package

On the first substantive response, give a useful startup package even when information is incomplete. Make no filesystem writes, Memory updates, index changes, or external actions.

Include only the sections useful to the situation:

1. **Known facts** — extract user-provided facts and inspected evidence. Keep evidence separate from inference.
2. **Provisional three-dimensional classification** — state working form (goal-oriented, operational, or mixed), service protocol (delivery progress, continuous operation, long-term companionship), and maturity (blank concept, scattered materials, runnable but messy, or mature/resumable). Give a short reason for each and label unsupported parts provisional.
3. **Key gaps** — ask only for facts that change safety, structure, or the next action. A gap is non-blocking if it can safely remain unresolved in the current-state record.
4. **First action** — recommend one concrete, reversible next move that produces value before a complete system exists.
5. **Proposed artifacts** — list the minimum creates/changes with exact paths when a target path is known; otherwise show path patterns and state that final paths require confirmation. For each artifact, give purpose and whether it is a stable rule source, current-state source, or only a route to existing evidence.
6. **Confirmation gate** — ask for explicit approval of the target path, boundaries, and listed writes. Combine this with only the smallest blocking questions.

Do not invent cadence, owner, metrics, workflow, platform, volume, health facts, or other user-owned facts. Mark assumptions as assumptions. Do not ask a fixed questionnaire or require every future-useful detail before proposing a safe minimum.

### Ask enough to operate, not just enough to create files

Do not stop after asking only for a goal and a path when the user is asking for a continuing project system. In the startup package, group the remaining high-impact gaps so the user can answer them in one reply. Ask only groups relevant to the provisional service protocol:

| Need | Ask when it affects the first operating cycle |
| --- | --- |
| Outcome and scope | What result or change matters, what is outside scope, and what would count as a useful first stage? |
| Starting reality | What already exists, what is currently happening, and what constraint, deadline, or blocker matters now? |
| Ownership and authority | Who decides, contributes, or must approve key choices? |
| Location and permissions | Where may the project live, what may be read/written, and what is out of bounds? |
| Continuity | What should a new session recover, and what regular rhythm or trigger should cause a check-in? |
| Protocol-specific needs | Delivery: stakeholder, deliverable, timing. Operations: current queue, cadence, signal/metric. Long-term companionship: service object, privacy, decision rights, escalation boundary. |

Present these as a compact, tailored question group, not a mandatory form. Omit questions already answered and defer non-blocking detail to **Context to complete**. If a question is needed to write safely, mark it as blocking; otherwise explain the task that will trigger it later.

For a long-term companionship project, explicitly identify the service object, owner decision rights, privacy boundary, recurring rhythm, and professional-escalation boundary. Do not make medical, school, legal, or other high-risk decisions for the owner.

## 3. Preserve mature projects; classify before changing

Use classification to choose a response, not a template:

| Situation | Default response |
|---|---|
| Goal-oriented work | Propose one current progress record plus a stable entry only if the existing structure lacks them. |
| Operational or mixed work | Propose the smallest useful current operating record, queue, period review, or active-item route; do not force a linear progress file. |
| Mature and resumable | Recommend keeping or directly taking over the structure when it already has a stable entry, current state, source routing, and clear next step. Cite evidence; do not rebuild it. |
| Runnable but messy | Identify the smallest missing link and propose a minimal adjustment, not a wholesale restructuring. |

Every proposal must preserve original evidence in place. Route to existing sources rather than copying their full content into an entry document. If non-blocking unknowns need recording, put them only in the authoritative current-state location as **Context to complete**, with: missing fact, why it matters, trigger for asking, and source/person to confirm.

## 4. Write only after explicit confirmation

Require an unambiguous confirmation of the target path, allowed boundary, and proposed write list. A general desire to “start the project” is not confirmation of a specific file plan.

After confirmation:

1. Re-check the target path for changes that affect the proposal.
2. Create or modify only approved artifacts.
3. Keep stable rules in the stable entry, current facts and next action in the authoritative current-state record, and source locations as routes rather than copied facts.
4. Add non-blocking unknowns to that current-state record; do not scatter them into reviews, retrospectives, or source notes.
5. Report exact changed paths, actual changes, and any departure from the approved proposal.

Never overwrite Memory or existing project state as part of launch. Never batch-restructure, delete, move, or perform external actions.

## 5. Verify a fresh-session hand-off

After approved writing, use a new session or equivalent isolated context. Give it only the project path and ask it to identify:

1. objective;
2. current state;
3. next step;
4. materials to read next; and
5. boundaries it must not cross.

Record the result in the approved project location only when that write was included in the confirmation. If the project cannot answer one item, identify the smallest missing link and propose a correction; do not silently expand the structure.

## Safety rules

- Keep user-owned facts in their original source unless explicitly approved for promotion.
- Mark uncertainty and inferences; a recommendation or review finding is not a project fact.
- Do not write before confirmation, including empty folders, templates, indexes, or status files.
- End a completed working session by updating only the approved current-state location and stating the next continuation point.
