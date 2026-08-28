# CI/CD Migration: Travis CI → CircleCI → GitHub Actions

## Status

Accepted

## Context

The repo has gone through two CI migrations:

1. **Travis CI → CircleCI** (commit `868fa9f`, ~2021): Travis CI support was dropped by many open-source projects as it moved to a paid model. CircleCI was the team standard at the time and offered Docker-based builds with configurable Python versions.

2. **CircleCI → GitHub Actions** (commit `f73b2f6`, DX-822, March 2026). The DX team migrated all Python SDK repos to GitHub Actions.

## Decision

All CI runs via `.github/workflows/ci.yml`. The workflow runs `pdm run coverage` and `pdm run lint` across Python 3.9–3.12. Local development uses the devcontainer configuration (`.devcontainer/`) for environment parity.

## Consequences

- Fork PRs can run CI without CircleCI credentials
- CircleCI config (`.circleci/config.yml`) was deleted; no rollback path without re-adding it
- Source: DX-822, commit `f73b2f6`
