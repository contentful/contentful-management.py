import dateutil.parser

from datetime import datetime

from .utils import snake_case
from .utils import camel_case
from .utils import base_path_for


"""
contentful.resource
~~~~~~~~~~~~~~~~~~~

This module implements the Resource, FieldResource and Link classes.

API Reference: https://www.contentful.com/developers/docs/references/content-delivery-api/#/introduction/common-resource-attributes

:copyright: (c) 2016 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class Resource(object):
    """
    Base Resource Class

    Implements common resource attributes.

    API Reference: https://www.contentful.com/developers/docs/references/content-delivery-api/#/introduction/common-resource-attributes
    """

    def __init__(self, item, default_locale='en-US', client=None):
        self.raw = item
        self.default_locale = default_locale
        self._client = client
        self.sys = self._hydrate_sys(item)

    @classmethod
    def base_url(klass, space_id='', resource_id=None, **kwargs):
        """Returns the URI for the Resource"""

        url = "spaces/{0}/{1}".format(
            space_id,
            base_path_for(klass.__name__)
        )

        if resource_id:
            url = "{0}/{1}".format(url, resource_id)

        return url

    @classmethod
    def create_attributes(klass, attributes, previous_object=None):
        """Attributes for resource creation"""

        result = {}

        if previous_object is not None:
            result = {k: v for k, v in previous_object.to_json().items() if k != 'sys'}

        result.update(attributes)

        return result

    @classmethod
    def create_headers(klass, attributes):
        """Headers for resource creation"""

        return {}

    @classmethod
    def update_attributes_map(klass):
        """Defines keys and default values for non-generic attributes"""

        return {}

    def delete(self):
        """Deletes the Resource"""

        return self._client._delete(
            self.__class__.base_url(
                self.sys['space'].id,
                self.sys['id']
            )
        )

    def update(self, attributes=None):
        """Updates the Resource with attributes"""

        if attributes is None:
            attributes = {}

        headers = self.__class__.create_headers(attributes)
        headers.update(self._update_headers())

        result = self._client._put(
            self._update_url(),
            self.__class__.create_attributes(attributes, self),
            headers=headers
        )

        self._update_from_resource(result)

        return self

    def save(self):
        """Saves the current state of the Resource"""

        return self.update()

    def reload(self, result=None):
        """Reloads the Resource"""

        if result is None:
            result = self._client._get(
                self.__class__.base_url(
                    self.sys['space'].id,
                    self.sys['id']
                )
            )

        self._update_from_resource(result)

        return self

    def to_link(self):
        """Returns a Link for the Resource"""

        link_type = self.link_type if self.type == 'Link' else self.type

        return Link({'sys': {'linkType': link_type, 'id': self.sys.get('id')}}, client=self._client)

    def to_json(self):
        """Returns the JSON Representation of the Resource"""

        result = {
            'sys': {}
        }
        for k, v in self.sys.items():
            if k in ['space', 'content_type', 'created_by',
                     'updated_by', 'published_by']:
                v = v.to_json()
            if k in ['created_at', 'updated_at', 'deleted_at',
                     'first_published_at', 'published_at', 'expires_at']:
                v = v.isoformat()
            result['sys'][camel_case(k)] = v

        return result

    def _hydrate_sys(self, item):
        sys = {}
        for k, v in item['sys'].items():
            if k in ['space', 'contentType', 'createdBy',
                     'updatedBy', 'publishedBy']:
                v = self._build_link(v)
            if k in ['createdAt', 'updatedAt', 'deletedAt',
                     'firstPublishedAt', 'publishedAt', 'expiresAt']:
                v = dateutil.parser.parse(v)
            sys[snake_case(k)] = v
        return sys

    def _build_link(self, link):
        return Link(link, client=self._client)

    def _update_headers(self):
        return {'x-contentful-version': str(self.sys['version'])}

    def _update_url(self):
        return self.__class__.base_url(
                self.sys['space'].id,
                self.sys['id']
            )

    def _update_from_resource(self, other):
        if hasattr(other, 'sys'):
            self.sys = other.sys
        for attr, default in self.__class__.update_attributes_map().items():
            value = getattr(other, attr, default)
            self_value = getattr(self, attr)
            if value == default and value != self_value:
                value = self_value
            setattr(self, attr, value)

    def __getattr__(self, name):
        if name in self.sys:
            return self.sys[name]
        raise AttributeError(
            "'{0}' object has no attribute '{1}'".format(
                self.__class__.__name__,
                name
            )
        )


class FieldsResource(Resource):
    """
    Fields Resource Class

    Implements locale handling for Resource fields.
    """

    @classmethod
    def create_attributes(klass, attributes, previous_object=None):
        """Attributes for resource creation"""

        if 'fields' not in attributes:
            if previous_object is None:
                attributes['fields'] = {}
            else:
                attributes['fields'] = previous_object.to_json()['fields']
        return {'fields': attributes['fields']}

    def __init__(self, item, **kwargs):
        super(FieldsResource, self).__init__(item, **kwargs)
        self._fields = self._hydrate_fields(item)

    def fields(self, locale=None):
        """Get fields for a specific locale

        :param locale: (optional) Locale to fetch, defaults to default_locale.
        """

        if locale is None:
            locale = self._locale()
        return self._fields.get(locale, {})

    def fields_with_locales(self):
        """Get fields with locales per field"""

        result = {}
        for locale, fields in self._fields.items():
            for k, v in fields.items():
                real_field_id = self._real_field_id_for(k)
                if real_field_id not in result:
                    result[real_field_id] = {}
                result[real_field_id][locale] = self._serialize_value(v)
        return result

    def to_json(self):
        """Returns the JSON Representation of the Resource"""

        result = super(FieldsResource, self).to_json()
        result['fields'] = self.fields_with_locales()
        return result

    @property
    def locale(self):
        """Returns the Resource's locale"""

        return self.sys.get('locale', None)

    def _real_field_id_for(self, field_id):
        for raw_field_id in self.raw['fields'].keys():
            if snake_case(raw_field_id) == field_id:
                return raw_field_id

    def _serialize_value(self, value):
        if isinstance(value, Resource):
            return value.to_link().to_json()
        elif isinstance(value, list) and value:
            if isinstance(value[0], Resource):
                return [resource.to_link().to_json() for resource in value]
        elif isinstance(value, datetime):
            return value.isoformat()
        return value

    def _hydrate_fields(self, item):
        fields = {}

        if 'fields' not in item:
            return fields

        for k, locales in item['fields'].items():
            for locale, v in locales.items():
                if locale not in fields:
                    fields[locale] = {}
                fields[locale][snake_case(k)] = self._coerce(v)

        return fields

    def _coerce(self, value):
        return value

    def _locale(self):
        return self.locale or self.__dict__['default_locale']

    def _update_from_resource(self, other):
        super(FieldsResource, self)._update_from_resource(other)
        if hasattr(other, '_fields'):
            self._fields = other._fields

    def __getattr__(self, name):
        locale = self._locale()
        if name in self._fields.get(locale, {}):
            return self._fields[locale][name]
        return super(FieldsResource, self).__getattr__(name)

    def __setattr__(self, name, value):
        if name not in ['raw', 'sys', 'default_locale',
                        '_client', '_fields', '__CONTENT_TYPE__']:
            locale = self._locale()
            if (name in self._fields.get(locale, {}) or
                    self._is_missing_field(name)):
                if locale not in self._fields:
                    self._fields[locale] = {}
                self._fields[locale][name] = value
                return self._fields[locale][name]
        return super(FieldsResource, self).__setattr__(name, value)

    def _is_missing_field(self, name):
        """
        By default, fields not appearing on responses are considered
        as object meta-data, and they will not be added to `_fields`,
        making them not part of the serialization when sent back to
        the API for saving.
        """

        return False


class PublishResource(object):
    """
    Allows for Resource Publish/Unpublish.
    """

    @property
    def is_published(self):
        """Checks if Resource is Published"""

        return bool(self.sys.get('published_at', False))

    def publish(self):
        """Publishes the Resource"""

        result = self._client._put(
            "{0}/published".format(
                self.__class__.base_url(self.sys['space'].id, self.sys['id']),
            ),
            {},
            headers=self._update_headers()
        )

        return self.reload(result)

    def unpublish(self):
        """Unpublishes the Resource"""

        self._client._delete(
            "{0}/published".format(
                self.__class__.base_url(self.sys['space'].id, self.sys['id']),
            ),
            headers=self._update_headers()
        )

        return self.reload()


class ArchiveResource(object):
    """
    Allows for Resource Archive/Unarchive.
    """

    @property
    def is_archived(self):
        """Checks if Resource is Archived"""

        return bool(self.sys.get('archived_version', False))

    def archive(self):
        """Archives the Resource"""

        self._client._put(
            "{0}/archived".format(
                self.__class__.base_url(self.sys['space'].id, self.sys['id']),
            ),
            {},
            headers=self._update_headers()
        )

        return self.reload()

    def unarchive(self):
        """Unarchives the Resource"""

        self._client._delete(
            "{0}/archived".format(
                self.__class__.base_url(self.sys['space'].id, self.sys['id']),
            ),
            headers=self._update_headers()
        )

        return self.reload()


class Link(Resource):
    """Link Class

    API Reference: https://www.contentful.com/developers/docs/references/content-delivery-api/#/reference/links
    """

    def resolve(self, space_id=None):
        """Resolves Link to a specific Resource"""

        proxy_method = getattr(
            self._client,
            base_path_for(self.link_type)
        )
        if self.link_type == 'Space':
            return proxy_method().find(self.id)
        else:
            return proxy_method(space_id).find(self.id)

    def to_json(self):
        """Returns the JSON Representation of the Resource"""

        return {
            'sys': {
                'type': 'Link',
                'linkType': self.sys.get('link_type'),
                'id': self.sys.get('id')
            }
        }

    def __repr__(self):
        return "<Link[{0}] id='{1}'>".format(
            self.link_type,
            self.id
        )
