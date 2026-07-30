---
name: project-os
description: Route a natural-language request to the appropriate Agent Project OS workflow without requiring the user to know internal Skill names. Use when a user asks to start, take over, organize, advance, update, review, recalibrate, remember, or prioritize work across one or more projects. Identify the intent, then immediately execute exactly one selected workflow in the same turn; do not inspect projects or write files while routing.
---

# Project OS

Lower the entry barrier to Agent Project OS. This is a thin router, not a project manager: identify the user's present need and hand it to one workflow.

## Route the request

Use the user's requested outcome, not project keywords or inferred project health. Choose exactly one route when the intent is clear.

| Current user intent | Natural-language signals | Route |
| --- | --- | --- |
| Start, take over, or give shape to one project | “开始一个项目”, “帮我接手”, “整理这个项目”, “让它能持续做下去” | `launch-project` |
| Advance current work or record one update | “今天做了什么”, “接下来怎么办”, “更新一下进度”, “安排这周”, “这是今天的情况” | `project-check-in` |
| Reconsider direction, scope, pace, or a persistent blocker | “要不要调整方向”, “项目卡住了”, “复盘一下是否还值得做”, “目标可能不对” | Mid-course review workflow |
| Set up, inspect, or govern durable workspace memory | “建立记忆”, “整理长期偏好”, “哪些该记住”, “检查 Memory” | `bootstrap-workspace` — Memory governance path |
| Compare multiple projects for priority, conflicts, or reuse | “我有哪些项目”, “先做哪个”, “项目互相冲突吗”, “整体项目复盘” | `review-portfolio` |

Do not route a request merely because it contains words such as “项目”, “复盘”, or “记忆”. For example, “更新这周的项目进度” goes to `project-check-in`; “这个项目的目标还合适吗” goes to Mid-course review.

## Select one current Skill

The router is not the current working Skill. It must select exactly one route, then get out of the way. Read the selected sibling `SKILL.md` and execute its first applicable step in the same response.

| Route | Skill file to load |
| --- | --- |
| `launch-project` | `../launch-project/SKILL.md` |
| `project-check-in` | `../project-check-in/SKILL.md` |
| Mid-course review workflow | `../review-project-structure/SKILL.md` until a dedicated workflow exists |
| Memory governance | `../bootstrap-workspace/SKILL.md` |
| `review-portfolio` | `../review-portfolio/SKILL.md` |

Only the selected Skill may perform substantive work in this turn. Its conclusion, unresolved question, and stated next step become the routing context for the next user message. Use that recent context to resume the selected workflow rather than sending the user back through a generic router question.

## Dispatch or clarify

### When intent is clear

Load the selected Skill file and immediately execute it. Do not show a standalone `Route: ...` message, ask the user to confirm the route, wait for “对的”, or tell the user to invoke another Skill.

You may introduce the work in one short natural sentence only if it helps comprehension, then continue with the selected Skill's actual first response. For example, a clear request to start a project should immediately receive `launch-project`'s startup package, not a routing label.

### When intent is ambiguous

Ask exactly one short question whose answer distinguishes the plausible routes. Offer no diagnosis, file plan, or additional questions.

When the request is broad enough to plausibly mean more than two routes, use one compact five-path question instead of an arbitrary binary split:

> 你现在最想先做哪件事：启动/接手一个项目、推进正在做的工作、重新判断项目方向、整理长期记忆，还是比较多个项目？

Examples:

- “你现在是想推进一件正在做的事，还是重新判断这个项目的方向？”
- “你想处理一个具体项目，还是比较多个项目的优先级？”
- “你是想建立长期记忆，还是为一个项目补充今天的最新情况？”

After the answer, route once. Do not begin a second clarification round in this Skill.

## Boundaries

- Do not read workspace indexes, project files, Memory, or folders to choose a route. Reading the selected sibling Skill file is required for dispatch. Use the recent current-conversation conclusion only as continuation context, not as evidence about project facts.
- Do not create, update, move, or delete files, including project state and Memory.
- Do not assess project status, diagnose blockers, summarize evidence, or recommend actions beyond selecting the route.
- Do not turn an unclear request into a catch-all route. Ask one distinguishing question instead.
- Allow users to bypass this router and invoke a specific workflow directly.
