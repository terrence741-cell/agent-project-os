# Agent Project OS

Skills that let a file-system Agent carry a real project across sessions.

Most Agent project tooling assumes the project is code. This one assumes it is not:
a client deliverable, a content operation, a research question, a long-running
personal commitment. What those have in common is that the work lives in Markdown,
the state lives in the user's head, and the next session starts from nothing.

Agent Project OS is a continuity protocol, not a project manager. It never becomes
the owner of your project's truth — it helps the Agent find that truth, act on it,
and leave a small confirmed handoff behind.

## The model

Three layers, kept apart on purpose:

| Layer | Answers | Lives in |
| --- | --- | --- |
| Memory | Who this is for, what the long-term boundaries are | Workspace memory |
| Project | Where the work stands now, where the material is | The project's own files |
| Skill | How this kind of thing gets done repeatably | These Skills |

Collapsing them is what makes Agent-run projects rot. A stable entry point mixed
with volatile status means the entry point goes stale; project facts promoted to
long-term Memory means yesterday's blocker outlives the project.

## The Skills

Six Skills. You only need to know the first one.

| Skill | The question it answers |
| --- | --- |
| `project-os` | Which path does this request belong to? |
| `launch-project` | How does a new project get a startup package and a resumable structure? |
| `project-check-in` | How does today's update become the next action and a safe state handoff? |
| `review-project-structure` | Does this project's structure actually support an Agent working in it? |
| `review-portfolio` | Across projects, what is stale, blocked, conflicting, or reusable? |
| `bootstrap-workspace` | How does the Agent learn who the user is and what the work landscape looks like? |

`project-os` is a thin router. It reads nothing, writes nothing, and diagnoses
nothing — it picks one workflow and gets out of the way in the same turn.

## Behaviour guarantees

These hold across every Skill, and are what the test suite verifies:

- **Nothing is written before you confirm it.** Every Skill that can write proposes
  first, with the exact target path and the exact content.
- **A missing path blocks reading, not helping.** Describe a real situation without
  naming a project and you still get a concrete action you can take now, marked as
  based on your own account rather than on project files.
- **Review is read-only by default.** Structure review returns Keep / Change /
  Ignore. "Keep it as it is" is a legitimate and common answer for a mature project.
- **Nothing is inferred into fact.** A claim with no supporting project evidence
  stays labelled user-reported until it is confirmed.
- **The portfolio stays thin.** Cross-project review reads indexes, not project
  bodies, and hands every action back to the project that owns it.
- **Sensitive material stays where it is.** Personal, health, client, personnel, and
  financial facts stay inside the project scope and are never proposed for Memory.

## Install

**Codex** — the plugin manifest is at `.codex-plugin/plugin.json`. Register this
directory as a local plugin source and install `agent-project-os`.

**Claude Code** — the manifest is at `.claude-plugin/plugin.json`. Add this
directory as a plugin source and install it.

The Skills are plain Markdown under `skills/`. Nothing executes, nothing is
installed system-wide, and no network access is used. You can also read any
`SKILL.md` directly and follow it by hand.

## A minimal first run

```
你: 我想启动一个新项目

Agent: (enters launch-project in the same turn, returns a read-only startup
       package: what it understood, a proposed shape, the first action you
       can take, and an explicit list of what it does not yet know —
       nothing is written yet)

你: 前面两条对，第三条改成……然后落盘

Agent: (writes only the confirmed minimum, reports the exact paths, then runs
       a continuation test: can a fresh session with no chat history pick
       this up correctly?)
```

Later, with the project already running:

```
你: 这个项目超预算了，我今天只有 45 分钟，怎么办

Agent: (gives one concrete 45-minute action derived from what you said,
       marks it as not yet checked against project files, asks for the path
       as a secondary item, and proposes no state change until it has one)
```

## Status

Pre-release. The Skills are stable enough for real use, and each behavioural
contract is verified by independent agents run three times over (pass^3) rather
than once. Not yet published to any marketplace.

Known open items are tracked as rule ambiguities in the test records: places
where two rules admit more than one lawful reading. They are recorded rather
than silently patched, because fixing wording tends to introduce new seams —
the stopping condition is stable behaviour, not perfect prose.

## License

Apache-2.0. See [LICENSE](LICENSE).
