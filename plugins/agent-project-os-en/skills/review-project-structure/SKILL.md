---
name: review-project-structure
description: "Read-only review of the file structure of one existing non-code Markdown project layer, focused on the fresh-session entry and the source of current state. When the user says “check whether this project's files make it easy to pick up next time” or “where do I read the entry and current state from”, or asks the same thing in other words, load this Skill first instead of scanning directly. Still applies when a business project links code assets; out of scope when the review root itself is a source tree. Does not take over daily project work."
---

# Review Project Structure

Assess usefulness, not compliance with a template. Default to keeping a structure that already supports correct work.

## 1. Set the review boundary

Confirm the project root, the work problem the user wants to solve, and the allowed read scope. If any is unclear, ask the smallest needed question before scanning.

State that the review is read-only. Do not create, edit, rename, move, delete, or update Memory, indexes, or project status—even if a defect is obvious.

## 2. Read evidence in the right order

Within the approved scope, inspect only what can answer the stated problem.

1. Start with the user-named entry/state documents. If the user gives only the project root, inspect root-level candidate files non-recursively; stop enumerating once the entry is found, then read the current state named by that entry. Name the exact paths actually read in the report.
2. Identify the project type from evidence:
   - **Goal-oriented:** a definable outcome or finish line; look for one current progress/state location.
   - **Operational:** recurring work without one terminal outcome; look for the smallest useful parallel state such as a queue, review cadence, decision log, or active-items list.
3. Follow only routes named by the entry that are immediately necessary for the stated structural question. Do not open paths marked excluded, archived, third-party, example, unverified, or “read only when executing” merely to verify the boundary claim; read one only when the user explicitly includes that path in the review target.

Do not begin with recursive `find`, `tree`, `rg --files`, or an equivalent full-tree inventory. You may read competing root-level entry or current-state candidates when needed to test an authority conflict; do not turn that into a project-wide scan.

A business or operational project may link to code repositories, source snapshots, or tool directories. Continue reviewing the non-code project's entry, current-state source, and asset routing; treat only the authority boundary or routing seam as structural evidence, without reading source code or judging implementation quality. Yield to a code workflow only when the requested review root itself is a code repository or source tree.

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

Only report a Change when its benefit is supported by evidence that was both authorized and necessary to read, and it is smaller than leaving the structure alone. Do not turn details that may exist in deferred or excluded material into a gap merely because this review did not verify them. Prefer updating an existing authoritative file over creating a new dashboard, database, or universal template. Separate stale current state from a sound stable entry.

Do not propose a change merely because a project differs from this Skill’s terminology or file naming. For a mature, resumable structure, “Keep / no changes” is a complete and desirable result.

## 5. Close safely

State the smallest next action. If the user wants a proposed Change implemented, show the exact target path, intended edit, and source-of-truth impact, then hand it to `launch-project`'s minimal-repair flow for separate confirmation and execution; this Skill remains read-only. A fresh-session resumption check after repair belongs to that execution flow or another explicit request, not this Review.
