# PDM as Package Manager

## Status

Accepted

## Context

The repo originally used a `Makefile` + manual `pip`/`setup.py`/`twine` workflow for packaging and publishing (visible in the initial commit). As the Python ecosystem matured, options included:
- `pip` + `setup.py` / `setup.cfg` — legacy, no modern lockfile support
- `poetry` — popular but slower and heavier
- `pdm` — PEP 517/518/660 compliant, supports lockfiles, fast, used across other Contentful Python SDKs

The Contentful DX team standardized on PDM across Python SDK repos.

## Decision

Migrated to PDM in commit `712f3d5` (Use PDM for packaging and distribution) followed by cleanup in `7273ad9` (Migrate to pdm for package management). `pyproject.toml` replaced `setup.py`/`requirements*.txt`. `pdm.lock` replaced ad-hoc version pinning. Build backend: `pdm-backend`.

PDM scripts in `pyproject.toml → [tool.pdm.scripts]` replaced Makefile targets for test, lint, coverage, docs, and release.

## Consequences

- Reproducible environments via `pdm.lock` — eliminates "works on my machine" dependency drift
- `pdm run <script>` is the canonical interface for all developer commands
- `pdm publish` handles PyPI release (replaces manual `twine` invocations)
- Contributors must install PDM (`pip install pdm`) before they can work locally
- **Known issue:** PDM cache can cause resolution failures; workaround is `pdm cache clean`
- Source: Python SDK Runbook (Confluence), commit history
