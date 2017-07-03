# CHANGELOG

## Unreleased
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
