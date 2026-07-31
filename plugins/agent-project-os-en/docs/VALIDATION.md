# V1.0.0 validation summary

## Release evidence

| Layer | Result |
| --- | --- |
| L0 — packaging and discoverability | 7/7 passed |
| L1 — local install and discovery | Codex and Claude Code installed and displayed all six Skills; explicit Claude Code and Codex `$project-os` calls passed |
| L2 — individual Skill contracts | 10/10 pass^3 |
| L3 — end-to-end scenarios | 6/6 complete chains passed |
| L4 — safety regressions | R1--R11 passed |

The detailed, anonymized test records live in the product workspace and are not
bundled here because they are development evidence rather than runtime files.

## Codex invocation check

On 2026-07-31, an isolated, read-only Codex CLI session invoked
`$project-os` with a new four-week short-video operation for an independent
coffee shop. The installed plugin routed in the same turn to `launch-project`,
returned a useful provisional operating-project startup package, requested only
relevant gaps, and created or modified no project files.

The host emitted a warning that its Skill descriptions were shortened to fit a
2% context budget. Explicit `$project-os` invocation nevertheless succeeded.
The local host also read its globally required shared-memory file before loading
the Skill. That read comes from the host's user-level policy, not from the
plugin's routing instruction; it is recorded as an environment interaction, not
claimed as a passing zero-read router test.

## Remaining release boundary

This is a review candidate, not a public release. The next external step is a
human review of this folder, followed by a Git commit and push when approved.
