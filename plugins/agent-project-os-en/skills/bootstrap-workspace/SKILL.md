---
name: bootstrap-workspace
description: "Set up or clean up what the Agent should durably remember about the user and their projects: working preferences, standing rules, and project routes. Use for “remember this about me”, “help me set up long-term memory”, “set up my workspace for the first time”, “have Codex and Claude Code share one Memory”, “check whether what you remember is still right”, or “register this project in memory”. For a new user, it can propose a standard preset with one physical shared-memory store, a thin index, topic files created on demand, two host entry points, and local Git recovery. It also accepts route candidates from launch-project. It reads only user-approved scope and never writes without explicit approval of exact targets and contents. Not for reviewing one project's progress or comparing projects."
---

# Bootstrap Workspace

Build a small, trustworthy orientation layer for an Agent workspace. The goal is not to collect everything: it is to preserve stable rules and useful routing information without copying private material, temporary state, or unresolved conflicts into Memory.

## 1. Set the boundary first

Before reading files, establish:

- the user’s goal for the workspace;
- exact folders or files that may be read;
- areas that must not be read or written;
- whether this pass is read-only or may propose a later write.

If the scope is unclear, ask a short clarification question. Default to read-only. Do not scan the whole workspace merely because the user asks to “organize” it.

## 2. Inventory only the authorized orientation sources

Start with the smallest useful set: an explicit Memory file, project index, workspace entry, and headers or frontmatter of listed projects. Keep an exact source list.

Do not read project bodies, archives, chats, credentials, or personal/private folders unless the user explicitly includes them. Do not treat a filename or an inferred convention as evidence.

The target Memory path and organization are part of the user's boundary too. When the user names one exact target file, keep every proposed entry within that file; do not add indexes, topic files, or directories unless the user explicitly asks for a multi-file architecture. Never treat the host Agent's automatic-memory directory, internal index format, or local-machine convention as a Memory architecture the user already chose. Naming a write target does not authorize reading or probing it; directory listings, globs, searches, and existence checks all count as reads. If the target file or directory is not authorized for reading, perform none of those checks and do not claim to know its format or whether it exists. You may propose a conservative entry confined to that target and list a pre-write reread of the same target as the minimum permission still needed.

Treat the exact user-approved read paths as a hard allowlist and check it before every read. Merely naming a path as a write target, host entry point, exclusion, or candidate does not add it to that allowlist. In the first read-only proposal, never attempt to read a write-only target even to determine whether it exists. Label it explicitly as “not authorized for inspection; current state unknown.”

### Choose the Memory mode

- When the user names one exact Memory file, use single-target mode. Do not load or propose the shared preset.
- When the user is new, asks for a long-term Memory system, or explicitly wants Codex and Claude Code to share one Memory, read [Standard shared Memory preset](references/shared-memory-preset.md) in full before proposing a design.
- When the user already has a Memory system, assess only the authorized scope and show the difference between keeping it, minimally cleaning it up, and migrating to the shared preset. Do not migrate by default.

## 3. Classify every finding

Place each finding in exactly one of these buckets before suggesting any write:

| Bucket | Meaning | Default handling |
| --- | --- | --- |
| Stable fact or rule | Durable preference, operating rule, or routing fact | Candidate for minimal Memory only with source, applicable scope, and confirmation or latest-review date |
| Current project state | Active focus, milestone, or temporary decision | Keep with its project; do not promote to long-term Memory |
| Historical record | Superseded or time-bound context | Preserve in place; do not use as default instruction |
| Sensitive | Credentials, personal data, confidential client material, or unclear private content | Do not copy; ask for handling if needed |
| Conflict | Sources disagree on the same durable fact or rule | Show both; require a user decision |
| Do not import | Duplicate, unsupported inference, or irrelevant material | Leave in source |

Facts that apply to different scopes are not necessarily a conflict. Label their scopes and ask only if the boundaries remain ambiguous.

### Project route registration mode

When `launch-project` hands off a route candidate, or the user explicitly asks to register a project entry:

1. Confirm that the route is still a candidate and obtain the minimum read authorization needed for the stable entry and target Memory file.
2. Check the canonical name, user-confirmed aliases, project root, exact stable-entry path, routing signals, applicable scope, sensitive boundary, sources, and candidate date. Keep missing fields missing; do not infer them.
3. Read the stable entry only to verify its path, project identity, and declared Memory boundary. Do not use that permission to read project bodies or current state, and do not copy project dynamics into Memory.
4. Check the target Memory for name or alias collisions, duplicate registrations of one path, stale paths, and scope conflicts. Report unresolved conflicts without writing or choosing an interim default.
5. Adapt one minimal route entry to the target Memory's existing format. Whatever the format, preserve the canonical name and aliases, root and stable-entry paths, applicable scope, source, and this user's confirmation date. Keep the sensitive boundary as a short exclusion or a route to the project contract.

A route entry only helps the host find the project entry. It must not store the current phase, next action, blockers, ownership changes, or other volatile project facts. Without a Workspace Memory route, do not promise name-only project discovery.

## 4. Report before changing anything

For a read-only pass, return a concise proposal with these sections:

1. **Authorized sources inspected** — exact paths and any excluded areas.
2. **Keep** — stable information already in the right home.
3. **Candidate additions** — proposed minimal entries, each with source, applicable scope, confirmation or latest-review date, and reason. Put those traceability fields inside the exact proposed entry, or map them explicitly to equivalent fields already present in the target Memory; do not leave them only in commentary outside the entry.
4. **Conflicts** — both statements, their sources, impact, and the precise decision needed.
5. **Do not import** — current state, history, sensitive material, duplicates, and unsupported inferences.
6. **Proposed next write** — exact target path and exact entries, or “no write proposed.” List only targets the user named or explicitly accepted; do not expand the file set merely to match the host's Memory layout.

For project route registration, also show the candidate source, any duplicate or conflict found, and the resulting “project name / alias → stable entry” relationship. Do not replace the exact entry with a vague promise to “add the project route”.

Never silently resolve a conflict. Do not recommend that either conflicting rule becomes the interim default, including a “safer” or “more conservative” one; mark the rule as unresolved until the user chooses or defines its scope. Never turn a current priority into a permanent rule. Never promise a write until the user has approved its target and contents.

## 5. Write only after explicit, specific confirmation

Proceed only when the user confirms both:

- the exact target file or files; and
- the exact entries to add, update, or remove.

Immediately before writing, reread the target within the authorized scope. Make the smallest change that implements the confirmation. Do not overwrite adjacent entries, import a whole document, or include unresolved conflicts or sensitive content.

For a project route, confirmation must occur after this Skill displays the exact entry. Earlier approval of project files, a launch plan, or the route candidate does not substitute for it. Use the actual confirmation date when writing, keep project state inside the project, and avoid creating a duplicate entry for the same path.

For the shared preset, list exact changes separately for Memory content, the physical directory and topic files, the two host entry points, global host rules, proven host read/write permission changes, and Git actions. One confirmation may cover several items only when the user explicitly names and approves those items. Approval of Memory content does not automatically authorize symlink creation, global-rule changes, host permission changes, or Git initialization.

Afterward, report the changed paths, entries written, and items intentionally left unresolved. If the user has not confirmed, remain read-only.

## Guardrails

- Do not create a global Memory by copying every project or chat.
- Do not impose the host Agent's internal automatic-memory path or default index layout on a user-specified Memory target.
- Do not scan beyond the authorized scope.
- Do not copy secrets, personal data, or unclear confidential content.
- Do not merge, overwrite, choose between, or assign an interim default to conflicting Memory sources.
- Keep project execution status in project files unless the user explicitly adopts a durable cross-project rule.
- Treat the project contract's memory scope as a hard boundary: do not promote facts that the project excludes from workspace Memory or Portfolio.
- Do not treat a project route candidate as confirmed Memory; review the candidate, target file, and exact entry again in this Skill.
- Do not create two Memory copies and synchronize them by mirroring, copying, or dual writes. Both hosts must ultimately point to one physical store.
- Do not force-replace links, delete existing targets, overwrite global rules, add a Git remote, or push automatically.
