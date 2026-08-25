# Architecture Decision Records

| ADR | Date | Status | Title |
|---|---|---|---|
| [005](./2026-08-25-generated-sphinx-html-committed-to-docs.md) | 2026-08-25 | Accepted | Generated Sphinx HTML is Committed to `docs/`, Sources Live in `_docs/` |

Records 001–004 (proxy and resource builder pattern, VCR cassettes for testing,
CI/CD migration, PDM as package manager) live in
[`AI_context/ADRs/`](../../AI_context/ADRs/), which is where
[`AGENTS.md`](../../AGENTS.md) points for decision history.

**Note:** `docs/` is generated output — `pdm run docs` begins with `rm -rf docs`
and will delete this directory. See ADR 005 for the details.
