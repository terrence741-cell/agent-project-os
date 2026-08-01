# Agent Project OS

[中文说明](../agent-project-os/README.md) · [Bilingual distribution contract](../../distribution/BILINGUAL-DISTRIBUTION.md)

Help desktop Harness Agents such as Claude Code and Codex become real project collaborators.

Agent Project OS is an open-source project-management system for desktop Harness Agent users who work with local files. It helps turn a real project—whether a client delivery, content operation, research topic, learning plan, or long-running personal matter—into a workspace an Agent can repeatedly pick up, understand, advance, and safely resume across sessions.

You should not need to re-explain the background, search for materials, or remember where the last session stopped every time you start a new chat. Agent Project OS guides the Agent to locate the facts in your project files, clarify the current state, propose a next step, and—after your confirmation—leave a concise handoff so the next session can continue naturally.

## Who it is for

**If you are new to desktop Agents**, it helps turn an early idea or a newly started piece of work into a project with a clear goal, file structure, current state, and next action. You do not need to design a project-file system before you begin.

**If you use desktop Agents heavily**, it does not ask you to migrate tools, rewrite existing material, or copy project facts into another platform. It helps the Agent respect your existing structure and sources of truth while maintaining continuity across sessions, weeks, and months.

It is especially useful for starting and sustaining non-code work: client delivery, content production, consulting, research, operations, learning, and personal plans. It can support code projects too, but its design focus is real work that lacks mature engineering scaffolding and still needs long-term collaboration.

## Not a traditional project-management app

It does not provide task boards or Gantt charts, and it does not replace Notion, Lark, or your project files. It runs in your workspace as a set of installable Skills that enable an Agent to:

- start or take over a project;
- turn day-to-day updates into an understood current state and next action;
- assess whether a project structure genuinely supports long-term Agent collaboration;
- help prioritize across several projects; and
- preserve confirmed, reusable cross-project lessons as long-term Memory.

Project facts always remain in the project’s own files. Any operation that writes to a file must first be confirmed by you.

## Model

Three layers are deliberately kept apart:

| Layer | What it answers | Where it lives |
| --- | --- | --- |
| Memory | Who the work is for and what its long-term boundaries are | Workspace Memory |
| Project | Where the work currently stands and where its materials are | The project’s own files |
| Skill | How this kind of work can be completed repeatedly | These Skills |

When those layers are mixed together, Agent-led projects decay: a stable entry point becomes stale when mixed with volatile status; yesterday’s blocker lasts longer than the project when project facts are promoted to long-term Memory.

## Skills

There are six Skills; you only need to know the first one.

| Skill | Question it answers |
| --- | --- |
| `project-os` | Which path should this request take? |
| `launch-project` | How can a new project get a startup package and resumable structure? |
| `project-check-in` | How does today’s update become a next action and safe status handoff? |
| `review-project-structure` | Does this project structure really support Agent work? |
| `review-portfolio` | Across several projects, what is stale, blocked, in conflict, or reusable? |
| `bootstrap-workspace` | How does an Agent understand who the user is and what their work landscape is? |

`project-os` is a thin router: while routing, it reads nothing, writes nothing, and diagnoses nothing. It selects one workflow, then hands over to it in the same turn.

## Behaviour guarantees

The following rules apply to every Skill and are verified by the test suite:

- **Never write before confirmation.** Every Skill that may write first proposes the exact target path and content.
- **A missing path blocks reading, not helping.** Even without a project path, the Agent gives one concrete action based on your description and clearly labels the source as your account rather than project files.
- **Reviews are read-only by default.** Structure review returns Keep / Change / Ignore. For a mature project, “keep it as it is” is a valid and common conclusion.
- **Never turn inference into fact.** A claim without project evidence remains labelled as user-reported until confirmed.
- **Keep portfolios thin.** Cross-project review reads indexes rather than project bodies; every action returns to the project that owns it.
- **Keep sensitive material in place.** Personal, health, client, personnel, and financial facts remain inside the project scope and are never proposed for Memory.

## Install

**Codex:** the plugin manifest is at `.codex-plugin/plugin.json`. Register this directory as a local plugin source and install `agent-project-os-en`.

**Claude Code:** the plugin manifest is at `.claude-plugin/plugin.json`. Add this directory as a plugin source, then install it.

The Skills are plain Markdown under `skills/`. Nothing executes, nothing is installed system-wide, and no network access is used. You can also read any `SKILL.md` directly and follow it manually.

## Minimal first run

```
You: I want to start a new project

Agent: (enters launch-project in the same turn and returns a read-only startup
        package: what it understands, a proposed structure, the first action
        you can take now, and a clear list of what it does not yet know —
        nothing has been written.)

You: The first two points are right; change the third one to … and write it

Agent: (writes only the confirmed minimum, reports the exact paths, then runs
        a continuation test: can a new session with no chat history pick this
        project up correctly?)
```

For a project already in progress:

```
You: This project is over budget and I have only 45 minutes today. What should I do?

Agent: (gives one concrete 45-minute action based on your account, marks that
        it has not yet checked the project files, asks for the path as a
        secondary question, and proposes no status change before confirmation.)
```

## Status

V1.0.0 review candidate. The Skills are stable enough for real work; each behavioural contract has been validated three times by independent agents (`pass^3`), rather than only once. It has not been publicly published to any marketplace.

This is the English localized package. The Chinese package is the canonical, primary package and is released independently under a distinct name. The distribution contract defines their behavioural parity and shared version gate.

Known open items are recorded as rule ambiguities in the test records: places where two rules permit more than one valid interpretation. They are recorded rather than silently patched, because changing wording can introduce new seams; the stopping condition is stable behaviour, not perfect prose.

## License

Apache-2.0. See [LICENSE](LICENSE).
