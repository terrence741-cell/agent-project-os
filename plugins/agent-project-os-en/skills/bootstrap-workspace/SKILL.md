---
name: bootstrap-workspace
description: "Set up or clean up what the Agent should durably remember about the user and their projects: working preferences, standing rules, and project routes. Use for “remember this about me”, “help me set up long-term memory”, “set up my workspace for the first time”, “check whether what you remember is still right”, or “register this project in memory”. Also accepts a route candidate from launch-project and checks its names, paths, source, scope, and conflicts. Reads only user-approved scope and never writes without explicit approval of both the target Memory file and exact entries. Not for reviewing one project's progress or comparing projects."
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
3. **Candidate additions** — proposed minimal entries, each with source, applicable scope, confirmation or latest-review date, and reason.
4. **Conflicts** — both statements, their sources, impact, and the precise decision needed.
5. **Do not import** — current state, history, sensitive material, duplicates, and unsupported inferences.
6. **Proposed next write** — exact target path and exact entries, or “no write proposed.”

For project route registration, also show the candidate source, any duplicate or conflict found, and the resulting “project name / alias → stable entry” relationship. Do not replace the exact entry with a vague promise to “add the project route”.

Never silently resolve a conflict. Do not recommend that either conflicting rule becomes the interim default, including a “safer” or “more conservative” one; mark the rule as unresolved until the user chooses or defines its scope. Never turn a current priority into a permanent rule. Never promise a write until the user has approved its target and contents.

## 5. Write only after explicit, specific confirmation

Proceed only when the user confirms both:

- the exact target file or files; and
- the exact entries to add, update, or remove.

Immediately before writing, reread the target within the authorized scope. Make the smallest change that implements the confirmation. Do not overwrite adjacent entries, import a whole document, or include unresolved conflicts or sensitive content.

For a project route, confirmation must occur after this Skill displays the exact entry. Earlier approval of project files, a launch plan, or the route candidate does not substitute for it. Use the actual confirmation date when writing, keep project state inside the project, and avoid creating a duplicate entry for the same path.

Afterward, report the changed paths, entries written, and items intentionally left unresolved. If the user has not confirmed, remain read-only.

## Guardrails

- Do not create a global Memory by copying every project or chat.
- Do not scan beyond the authorized scope.
- Do not copy secrets, personal data, or unclear confidential content.
- Do not merge, overwrite, choose between, or assign an interim default to conflicting Memory sources.
- Keep project execution status in project files unless the user explicitly adopts a durable cross-project rule.
- Treat the project contract's memory scope as a hard boundary: do not promote facts that the project excludes from workspace Memory or Portfolio.
- Do not treat a project route candidate as confirmed Memory; review the candidate, target file, and exact entry again in this Skill.
