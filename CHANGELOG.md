# CHANGELOG

## Unreleased

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
