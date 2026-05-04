# CI/CD Migration: Travis CI → CircleCI → GitHub Actions

## Status

Accepted

## Context

The repo has gone through two CI migrations:

1. **Travis CI → CircleCI** (commit `868fa9f`, ~2021): Travis CI support was dropped by many open-source projects as it moved to a paid model. CircleCI was the team standard at the time and offered Docker-based builds with configurable Python versions.

2. **CircleCI → GitHub Actions + devcontainers** (commit `f73b2f6`, DX-822, March 2026): CircleCI was causing 401 errors for forked-repo PRs (external contributions could not run CI). The DX team decided to migrate all Python SDK repos to GitHub Actions to resolve the fork CI issue and to align local development with CI via devcontainers. Motivation from Ethan Ozelius (Slack `#prd-alpine-chat`, March 31, 2026): "I am going to remove the CircleCI required checks... migrating from CircleCI to GitHub Actions in basically all of our repos."

## Decision

All CI runs via `.github/workflows/ci.yml`. The workflow uses the devcontainer configuration (`.devcontainer/`) to run `pdm run coverage` and `pdm run lint` across Python 3.9–3.12. Local development uses the same devcontainer, ensuring local/CI parity.

## Consequences

- Fork PRs can run CI without CircleCI credentials
- Local dev and CI use identical environments (same Dockerfile, same `pdm install --group test`)
- External contributors need Docker to use the devcontainer locally (or can install PDM directly as a fallback)
- CircleCI config (`.circleci/config.yml`) was deleted; no rollback path without re-adding it
- Source: DX-822, commit `f73b2f6`, Slack `#prd-alpine-chat` (March 31, 2026)
