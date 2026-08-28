# Proxy and Resource Builder Pattern

## Status

Accepted

## Context

The Contentful Management API has a large and hierarchical resource model: Organizations → Spaces → Environments → ContentTypes/Entries/Assets, each with full CRUD plus lifecycle operations (publish, archive, etc.). A naive approach of directly exposing HTTP calls would require callers to manually construct URLs, pass credentials on every call, and deserialize JSON into dicts.

The library needed to:
1. Provide a Pythonic CRUD interface per resource type
2. Handle scoping (space_id, environment_id) transparently
3. Deserialize API JSON responses into typed, method-bearing Python objects
4. Stay extensible as new resource types are added to the CMA

## Decision

Two core patterns were established at the initial commit (January 2017):

**Proxy pattern:** A `ClientProxy` base class holds the HTTP client reference plus scope identifiers (`space_id`, `environment_id`). Concrete proxies (e.g., `EntriesProxy`, `AssetsProxy`) inherit from it and add resource-specific methods. The client exposes factory methods that return proxy instances: `client.entries('space_id', 'env_id')`. This keeps the scoping context on the proxy, not the caller.

**Resource builder pattern:** `ResourceBuilder` inspects the `sys.type` field in every API response and instantiates the corresponding Python class. This centralizes deserialization logic and makes it trivial to add support for new resource types (add an entry to the `buildables` dict and a new module).

## Consequences

- All CRUD operations are consistent across resource types through the `ClientProxy` base class
- Adding a new CMA resource requires: one new `Resource` subclass + one new `*Proxy` class + one entry in `ResourceBuilder.buildables`
- The proxy approach means callers cannot hold a stateless proxy across space changes — they must request a new proxy for a different scope
- Context not found for why this specific design was chosen over alternatives (e.g., a flat module API or a resource-registry approach) — likely a default/inherited choice from sibling SDKs
