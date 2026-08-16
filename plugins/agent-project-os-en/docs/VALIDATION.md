# V1.0.2 validation summary

## Release evidence

| Layer | Result |
| --- | --- |
| L0 — packaging and discoverability | Previous local checks passed; changed manifests pass static validation and await real-GitHub retesting |
| L1 — local install and discovery | Previous dual-host local installation passed; fresh environments and unfamiliar-user first runs await retesting |
| L2 — individual Skill contracts | Previous contracts passed; on-demand trigger cases A--K each passed three runs |
| L3 — end-to-end scenarios | Memory route proposal, conflict blocking, and separate confirmation passed forward tests; the shared preset passed its read-only proposal, one-store/two-entry setup, cross-writes, real isolated sessions on both hosts, and on-demand reads |
| L4 — safety regressions | This revision preserves confirm-before-write, read-only review, and sensitive-context boundaries; Claude Code external reads and Codex external writes both have deny-versus-exact-grant evidence |

The detailed, anonymized test records live in the product workspace and are not
bundled here because they are development evidence rather than runtime files.

## Current positioning check

On 2026-08-15, both language packages were checked against the same boundary.
Memory setup, project launch or organization, explicit structure review,
multi-project comparison, explicit check-in, and explicit routing uncertainty
may invoke the relevant capability. Known-project continuation, ordinary
writing, direction decisions, and a next-step request for one project do not.

Project-file and Workspace Memory writes require separate confirmation.
`launch-project` produces only a route candidate; `bootstrap-workspace` checks
alias and path conflicts, displays the exact write, and registers it only after
the second confirmation. Path-based resumption does not claim name-only
discovery.

V1.0.2 adds the standard shared Memory preset. A new user may receive a proposal for one physical store, a thin `MEMORY.md`, topic files created on demand, Codex and Claude Code entry points, and local Git recovery. An exact single-file target remains higher priority, and a write-only target may not be probed without separate read authorization.

On 2026-08-16, real local Codex CLI and Claude Code CLI sessions in isolated host configurations both loaded their global thin rules automatically and read only the request-relevant topic, stable project entry, and current state. The chain worked without the plugin loaded. Access to a physical path outside a host workspace is proposed separately by host, operation, and exact path only after a real denial.

## Remaining release boundary

This is a review candidate, not a public release. Fresh Codex and Claude Code
installation from the real GitHub repository URL, final copyable commands, and
trials with at least five unfamiliar users remain release gates.
