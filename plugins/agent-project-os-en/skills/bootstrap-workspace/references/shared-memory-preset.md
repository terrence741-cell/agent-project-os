# Standard shared Memory preset

Use this preset only when a new user asks for a long-term Memory system or explicitly wants Codex and Claude Code to share one Memory. Do not use it when the user has named one exact target file.

## 1. Method and default structure

Create one tool-neutral physical store. The default candidate is `~/.agent-project-os/shared-memory/`; it remains a proposal, and the user may choose another exact path.

```text
shared-memory/
├── MEMORY.md
├── user_profile.md
├── team_<slug>.md
├── project_<slug>.md
├── feedback_<slug>.md
└── reference_<slug>.md
```

- `MEMORY.md`: thin top-level index with only minimal stable preferences and routes to topic files.
- `user_profile.md`: confirmed stable user profile.
- `team_<slug>.md`: stable team or business-line context and boundaries.
- `project_<slug>.md`: project names, aliases, root, stable entry, scope, and source; never current project state.
- `feedback_<slug>.md`: confirmed cross-project collaboration feedback.
- `reference_<slug>.md`: durable infrastructure or reference guidance.

Create only files with confirmed content. Do not generate empty files to complete the template. Do not promote daily progress, project tasks, unconfirmed judgments, or sensitive facts into Memory.

## 2. Share across hosts

Both hosts must ultimately read and write the same physical files. Never create two directories and synchronize them.

Default proposal on POSIX systems:

```text
~/.codex/shared-memory  -> <physical-shared-memory>
~/.claude/shared-memory -> <physical-shared-memory>
```

If symlinks are unavailable, have both host-rule files refer directly to the same physical path. Do not invent unverified platform commands.

After receiving exact read authorization for each endpoint, classify it separately:

- Missing: may be proposed as a new link.
- Already a link to the same target: keep it; do not recreate it.
- Link to another target, or existing regular file/directory: report a conflict and stop. Do not delete, move, or force-replace it.

## 3. Host startup rules

Propose minimal equivalent rules for Codex's global `AGENTS.md` and Claude Code's global `CLAUDE.md`. Read each authorized existing target first and propose a minimal merge; never overwrite unrelated rules.

The rule semantics must say:

1. At the start of a new session, read `<physical-shared-memory>/MEMORY.md`.
2. Read only linked topic files relevant to the current request; do not preload the directory.
3. Treat Memory as durable orientation, not evidence of current project state. Verify current state through the stable project entry.
4. Write back only confirmed durable preferences, stable cross-project rules, and project routes. Keep temporary task state in the project.

If either host proves that a read or write is blocked because the symlink's real target or physical path is outside its current access scope, verify the actual error first. Only after reading the current host configuration and current documentation may the Agent propose the smallest separate permission change for that host: name the read or write operation, exact physical path, exact configuration file or launch argument, and minimal edit. Do not edit configuration merely because it might be needed, and do not extend one host's approval to the other host.

## 4. Local Git recovery

After authorization to inspect the physical store and its parent, determine whether it already belongs to a Git repository.

- Already in a repository: use the existing repository; do not initialize a nested one.
- Not in a repository: local `git init` may be proposed separately.
- Commit: create a recovery point only when the user confirms it and the scope contains only approved Memory changes.
- Never add a remote, push, create a scheduler, or treat a backup directory as current Memory.

## 5. Proposal and consent scopes

Return one exact proposal separated into:

1. **Memory content**: exact path and full proposed text for every target file.
2. **Physical structure**: directories and on-demand files to create, plus empty categories intentionally omitted.
3. **Host entry points**: exact source and target for every link or direct reference, with detected conflicts.
4. **Host rules**: exact minimal text to merge, listed separately for Codex and Claude Code.
5. **Host access permission**: only after a proven need; separately name the host, read or write operation, exact physical path, configuration file or launch argument, and minimal edit.
6. **Git recovery**: whether to initialize or create a local recovery point, and which remote actions will not occur.

The user may approve several scopes at once only by naming them explicitly. Leave every unapproved scope read-only or unexecuted.

## 6. Validation

After approved changes:

1. Resolve both host entry points and verify that they reach the same physical directory.
2. Make one approved synthetic write through the Codex entry and read the same content through the Claude Code entry; repeat in reverse.
3. Verify both hosts start from the thin `MEMORY.md` and load only relevant topic files.
4. Verify a project name routes through Memory to the stable entry and current state; Memory must not replace project state.
5. Verify the chain still works with the plugin disabled.
6. If a Git recovery point was created, locate it in local history and verify that no automatic push occurred.
