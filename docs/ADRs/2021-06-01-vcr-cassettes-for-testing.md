# VCR Cassettes for Testing

## Status

Accepted

## Context

The SDK makes real HTTP calls to `api.contentful.com`. Testing against the live API requires valid credentials, creates real content side-effects, and makes tests non-deterministic and slow. Options considered:

1. **Live API calls** — requires real credentials, creates side effects, slow and flaky
2. **Manual HTTP mocking** (e.g., `unittest.mock.patch`) — verbose, must be kept in sync with actual API response shapes
3. **VCR cassettes** (`vcrpy`) — record real API interactions once, replay them deterministically in CI

## Decision

`vcrpy` was adopted for HTTP mocking. YAML cassette files are stored in `fixtures/` organized by resource type. Tests record against the real API once; subsequent runs replay from cassettes with no live traffic.

Source: the `fixtures/` directory and `vcrpy==6.0.1` pin in `pyproject.toml` [test] extras.

## Consequences

- Tests are fast, deterministic, and run offline (used in CI via devcontainer with no API credentials)
- When the CMA API response shape changes for a resource, the cassettes for that resource must be re-recorded against the live API
- Adding tests for new endpoints requires a one-time recording step with a valid management token
- Cassette files can become stale if API responses change without re-recording — this is the main maintenance burden
