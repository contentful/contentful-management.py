# CHANGELOG

## Unreleased
* Changed CI/CD vendor from Travis to CircleCI

## v2.11.0

### Added
* Adds find user in space or organization scope [#66](https://github.com/contentful/contentful-management.py/pull/66)

## v2.10.0

*Note*: Only a minor change because the removed feature was *Alpha*.

### Added
* Add `OrganizationPeriodicUsage`, `Client#organization_periodic_usages` and `Organization#periodic_usages`.
* Add `SpacePeriodicUsage`, `Client#space_periodic_usages` and `Organization#space_periodic_usages`.

### Removed
* Removed now deprecated Alpha Usage APIs, which have been superseeded by the new APIs added.

## v2.9.1
* Drop support for Python 2.

## v2.9.0
### Added
* Enforce `utf-8` response encoding. [#63](https://github.com/contentful/contentful-management.py/pull/63)

## v2.8.0
### Added
* Added environment branching.

## v2.7.0
### Added
* Added `is_updated` to publishable resources. [contentful-management.rb/#178](https://github.com/contentful/contentful-management.rb/issues/178)

## v2.6.1
### Fixed
* Fixed an issue with `deepcopy` not being able to properly clone resources.
* Fixed an issue with properties missing from an entry that were not being able to be resolved to a field.

## v2.6.0
### Added
* Added Usage Periods API
* Added API Usages API

## v2.5.0

### Changed
* Removed `SpacesUploadProxy` and simplified the logic to use `UploadProxy`. [#52](https://github.com/contentful/contentful-management.py/issues/52)
* Updated `requests` version due to a vulnerability found in versions `2.19` and below.

## v2.4.0

As `RichText` moves from `alpha` to `beta`, we're treating this as a feature release.

### Changed
* Renamed `StructuredText` to `RichText`.

## v2.3.0
### Added
* Added support for `StructuredText` field type.

## v2.2.0

This release includes some minor-breaking changes. That said, those breaking changes are actually bug-fixes that actually match the behaviour of the SDK to
what's present in the README and the documentation.

### Added
* Added missing `memberships` proxy on `Space`.
* Added `transformation` and `filters` to `Webhook`.
* Added `parameters` to `UIExtension.extension`.

### Fixed
* Space Space Memberships Proxy now properly serializes attributes upon creation.
* Space Api Keys Proxy now properly serializes attributes upon creation.
* Environments Proxy now uses default behaviour.
* Space Roles Proxy now properly doesn't require a resource ID to be passed.
* Locales Proxy now properly doesn't require a resource ID to be passed.
* Space Webhooks Proxy now properly doesn't require a resource ID to be passed.

## v2.1.3
### Fixed
* Fixes 422 error handling when no `name` or `path` attribute are sent in the error details. [#36](https://github.com/contentful/contentful-management.py/issues/36)

## v2.1.2
### Fixed
* Fixed Locale creation.

## v2.1.1
### Fixed
* Fixed API Key updates when adding new environments to the existing list.

## v2.1.0
### Added
* Added environment selection option for Api Keys.
* Added a way to obtain Preview Api Keys.

## v2.0.0
### Added
* Added `Environment` API

### Changed
* `entries`, `assets`, `content_types` and `locales` are no longer available through a `Space` and have to be requested through an `Environment`.
* Methods present on the client that are environment aware, now require an `environment_id` parameter.

## v1.5.2

### Fixed
* Fixed issue when displaying UnprocessableEntityError that had no `value` attribute in it's `errors` array [#27](https://github.com/contentful/contentful-management.py/issues/27)

## v1.5.1

### Added
* Added error handling for 422 errors.

## v1.5.0

### Added
* Added better error messages for all error types.

## v1.4.0

### Added
* Added Organizations Endpoint.
* Added Webhook Calls and Health Endpoints.
* Added Content Type Snapshots Endpoints.
* Added UI Extensions Endpoints.
* Added Personal Access Tokens Endpoints.
* Added Users Endpoint.
* Added Space Memberships Endpoints.

## v1.3.2

### Fixed
* Fixed `Accept-Encoding` header when `gzip` was disabled.
* Fixed docstrings.
* Fixed Content Type Field IDs not being correctly serialized [#17](https://github.com/contentful/contentful-management.py/issues/17)

## v1.3.1

### Added
* Added `Array` wrapper [#13](https://github.com/contentful/contentful-management.py/issues/13)

### Fixed
* Fixed issue when calling `to_json()` on entries with new fields added [#10](https://github.com/contentful/contentful-management.py/issues/10)

## v1.2.0

### Added
* Added `X-Contentful-User-Agent` header for more information.

## v1.1.0

### Added

* Added check for undefined fields from the WebApp against presence in the Content Type

### Fixed

* Fixed VersionMismatch parsing error [#2](https://github.com/contentful/contentful-management.py/issues/2)

### Changed

* Reuse result from `#publish` for reloading [#1](https://github.com/contentful/contentful-management.py/issues/1)

## v1.0.2

* Add `snapshot` property to Snapshot API.

## v1.0.1

* Fix issue when creating entries through a space object.
* Increased test coverage.

## v1.0.0

Initial release of the Official CMA SDK.

* Support for all suppoerted CMA Endpoints.
* Serialization for all Endpoint resources.
* Link Resolution.
* Rate Limit automatic back-off.
* Proxy support.
* File Upload support.
