---
name: project-os
description: Entry point for running non-code projects kept in Markdown — client delivery, content operations, research, and long-term personal matters. Use when a request is about a project but the right workflow is not obvious, including “help me start a project”, “how do I take over this project?”, “what should I do next?”, “the direction feels wrong”, “is this still worth doing?”, “which project should I do first?”, or “remember my working preferences”; Chinese examples include “帮我开个项目” and “接下来该干嘛”. When the intent is clear, pick exactly one workflow and run it in the same turn; when it is genuinely ambiguous, ask one question that tells the paths apart and route on the answer. Inspects no projects and writes no files while routing, and defers to a sibling Skill the user has clearly asked for.
---

# Project OS

Lower the entry barrier to Agent Project OS. This is a thin router, not a project manager: identify the user's present need and hand it to one workflow.

## Route the request

Use the user's requested outcome, not project keywords or inferred project health. Choose exactly one route when the intent is clear.

| Current user intent | Natural-language signals | Route |
| --- | --- | --- |
| Start, take over, or give shape to one project | “start a project”, “help me take this over”, “organize this project”, “make this sustainable” | `launch-project` |
| Advance current work or record one update | “what I did today”, “what should I do next?”, “update the project status”, “plan this week”, “here is today’s update” | `project-check-in` |
| Reconsider direction, scope, pace, or a persistent blocker | “should we change direction?”, “the project is stuck”, “is this still worth doing?”, “the goal may be wrong” | Mid-course review workflow |
| Set up, inspect, or govern durable workspace memory | “set up memory”, “organize long-term preferences”, “what should you remember?”, “check Memory” | `bootstrap-workspace` — Memory governance path |
| Compare multiple projects for priority, conflicts, or reuse | “what projects do I have?”, “which should I do first?”, “do these projects conflict?”, “review my whole portfolio” | `review-portfolio` |

Do not route a request merely because it contains words such as “project”, “review”, or “memory”. For example, “update this week’s project status” goes to `project-check-in`; “is this project’s goal still appropriate?” goes to Mid-course review.

## Select one current Skill

The router is not the current working Skill. It must select exactly one route, then get out of the way. Read the selected sibling `SKILL.md` and execute its first applicable step in the same response.

| Route | Skill file to load |
| --- | --- |
| `launch-project` | `../launch-project/SKILL.md` |
| `project-check-in` | `../project-check-in/SKILL.md` |
| Mid-course review workflow | `../review-project-structure/SKILL.md` — see the note below |
| Memory governance | `../bootstrap-workspace/SKILL.md` |
| `review-portfolio` | `../review-portfolio/SKILL.md` |

**Mid-course review has no dedicated Skill yet.** `review-project-structure` covers how a project is organized, not whether its direction, scope, or continued investment still make sense. Route there anyway — it is the closest available workflow — but say plainly, in one sentence, that this version reviews the project's structure rather than its direction, so the user is not left expecting a judgement the Skill will not make. Do not silently substitute a structural answer for the question the user asked.

Only the selected Skill may perform substantive work in this turn. Its conclusion, unresolved question, and stated next step become the routing context for the next user message. Use that recent context to resume the selected workflow rather than sending the user back through a generic router question.

## Dispatch or clarify

### When intent is clear

Load the selected Skill file and immediately execute it. Do not show a standalone `Route: ...` message, ask the user to confirm the route, wait for “yes, that’s right”, or tell the user to invoke another Skill.

You may introduce the work in one short natural sentence only if it helps comprehension, then continue with the selected Skill's actual first response. For example, a clear request to start a project should immediately receive `launch-project`'s startup package, not a routing label.

### When intent is ambiguous

Ask exactly one short question whose answer distinguishes the plausible routes. Offer no diagnosis, file plan, or additional questions.

When the request is broad enough to plausibly mean more than two routes, use one compact five-path question instead of an arbitrary binary split:

> What would you most like to do first: start or take over a project, advance work already underway, reconsider a project’s direction, organize long-term memory, or compare several projects?

Examples:

- “Do you want to advance work already underway, or reconsider this project’s direction?”
- “Do you want to work on one specific project, or compare priorities across several?”
- “Do you want to set up long-term memory, or add today’s latest update to one project?”

After the answer, route once. Do not begin a second clarification round in this Skill.

## Boundaries

- Do not read workspace indexes, project files, Memory, or folders to choose a route. Reading the selected sibling Skill file is required for dispatch. Use the recent current-conversation conclusion only as continuation context, not as evidence about project facts.
- Do not create, update, move, or delete files, including project state and Memory.
- Do not assess project status, diagnose blockers, summarize evidence, or recommend actions beyond selecting the route.
- Do not turn an unclear request into a catch-all route. Ask one distinguishing question instead.
- Allow users to bypass this router and invoke a specific workflow directly.
