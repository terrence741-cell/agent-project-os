---
name: review-project-structure
description: "Give a read-only second opinion on how one existing non-code Markdown project is organized. Use only when the user clearly asks to inspect its entry, source of current state, file organization, or fresh-session resumability, such as “is this project structure sensible?”, “where should these files go?”, “does the way I keep these notes work?”, or “will I find my way back next time?”. Return keep / change / ignore with exact paths as evidence and never move, rename, or rewrite anything. Do not capture “continue this project”, “what should I do today?”, or other daily work, and do not judge direction, scope, or whether to continue. Not for code repositories. After approval, launch-project may carry out a precise minimal repair."
---

# Review Project Structure

Assess usefulness, not compliance with a template. Default to keeping a structure that already supports correct work.

## 1. Set the review boundary

Confirm the project root, the work problem the user wants to solve, and the allowed read scope. If any is unclear, ask the smallest needed question before scanning.

State that the review is read-only. Do not create, edit, rename, move, delete, or update Memory, indexes, or project status—even if a defect is obvious.

## 2. Read evidence in the right order

Within the approved scope, inspect only what can answer the stated problem.

1. Start with root-level files and the user-named entry/state documents. Name their exact paths in the report.
2. Identify the project type from evidence:
   - **Goal-oriented:** a definable outcome or finish line; look for one current progress/state location.
   - **Operational:** recurring work without one terminal outcome; look for the smallest useful parallel state such as a queue, review cadence, decision log, or active-items list.
3. Follow only material routes named by the entry or needed for the requested work problem.

Classify the project’s own lifecycle, not the format of one backlog or a temporary initiative. A long-running business hub that contains several initiatives, periodic work, or an ongoing queue is operational even if each initiative has a milestone. If evidence supports both a finite delivery and continuing operations, state the mixed boundary and judge whether its state locations serve both safely; do not force it into goal-oriented merely because it has a task list.

Do not treat nested `test`, `测试`, `fixtures`, `examples`, `archive`, `归档`, vendored, generated, or third-party directories as evidence of the live project structure unless the user explicitly targets that directory. Do not infer that a missing preferred filename is a defect.

## 3. Test the structure against real continuation

Use the available evidence to answer these questions:

1. Can an Agent discover where to start and what this project is for?
2. Can it distinguish current facts from stable rules, historical material, and unverified drafts?
3. Can it identify the current state and next safe action in a form appropriate to the project type?
4. Can it load detailed materials only when needed, from an explicit route?
5. Is there one authoritative home for each current fact, or a clearly flagged conflict?
6. Does the structure state relevant write, privacy, or scope boundaries?
7. Is there a practical end-of-session update or handoff practice?

Treat unavailable or conflicting evidence as **unable to determine**. Do not turn unknown into “not started,” “unowned,” or “missing.” A document can be old reference material without making the whole project defective.

## 4. Report Keep / Change / Ignore

Give a concise classification, the paths actually examined, and this table:

| Finding | Evidence | Impact | Recommendation |
|---|---|---|---|
| Keep | Exact path and observed behavior | Why it supports correct continuation | Leave unchanged |
| Change | Exact gap or conflict | Concrete effect on work, safety, or resumption | Smallest proposed change; wait for confirmation |
| Ignore | Observation that is not a present problem | Why action is not justified | No action |

Only report a Change when its benefit is supported by evidence and it is smaller than leaving the structure alone. Prefer updating an existing authoritative file over creating a new dashboard, database, or universal template. Separate stale current state from a sound stable entry.

Do not propose a change merely because a project differs from this Skill’s terminology or file naming. For a mature, resumable structure, “Keep / no changes” is a complete and desirable result.

## 5. Close safely

State the smallest next action. If the user wants a proposed Change implemented, show the exact target path, intended edit, and source-of-truth impact, then hand it to `launch-project`'s minimal-repair flow for separate confirmation and execution; this Skill remains read-only. A fresh-session resumption check after repair belongs to that execution flow or another explicit request, not this Review.
