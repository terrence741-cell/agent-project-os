---
name: bootstrap-workspace
description: Set up or clean up what the Agent should durably remember about the user and their projects — working preferences, standing rules, and where each project lives. Use for “remember this about me”, “stop asking me this every time”, “these are my working preferences”, “help me set up long-term memory”, “set up my workspace for the first time”, “check whether what you remember is still right”, or “organize my long-term preferences”; Chinese examples include “以后记住我…” and “帮我建立长期记忆”. Reads only the folders the user names, sorts findings into keep / add / conflict / private / skip, shows both sides of a conflict instead of picking a winner, and never writes memory without explicit approval of both the target file and the exact entries. Not for reviewing one project's progress or comparing projects.
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

## 4. Report before changing anything

For a read-only pass, return a concise proposal with these sections:

1. **Authorized sources inspected** — exact paths and any excluded areas.
2. **Keep** — stable information already in the right home.
3. **Candidate additions** — proposed minimal entries, each with source, applicable scope, confirmation or latest-review date, and reason.
4. **Conflicts** — both statements, their sources, impact, and the precise decision needed.
5. **Do not import** — current state, history, sensitive material, duplicates, and unsupported inferences.
6. **Proposed next write** — exact target path and exact entries, or “no write proposed.”

Never silently resolve a conflict. Do not recommend that either conflicting rule becomes the interim default, including a “safer” or “more conservative” one; mark the rule as unresolved until the user chooses or defines its scope. Never turn a current priority into a permanent rule. Never promise a write until the user has approved its target and contents.

## 5. Write only after explicit, specific confirmation

Proceed only when the user confirms both:

- the exact target file or files; and
- the exact entries to add, update, or remove.

Immediately before writing, reread the target within the authorized scope. Make the smallest change that implements the confirmation. Do not overwrite adjacent entries, import a whole document, or include unresolved conflicts or sensitive content.

Afterward, report the changed paths, entries written, and items intentionally left unresolved. If the user has not confirmed, remain read-only.

## Guardrails

- Do not create a global Memory by copying every project or chat.
- Do not scan beyond the authorized scope.
- Do not copy secrets, personal data, or unclear confidential content.
- Do not merge, overwrite, choose between, or assign an interim default to conflicting Memory sources.
- Keep project execution status in project files unless the user explicitly adopts a durable cross-project rule.
- Treat the project contract's memory scope as a hard boundary: do not promote facts that the project excludes from workspace Memory or Portfolio.
