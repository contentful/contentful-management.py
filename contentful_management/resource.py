import dateutil.parser

from datetime import datetime

from .utils import snake_case, camel_case, base_path_for, sanitize_date


"""
contentful_management.resource
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the Resource, FieldResource, PublishResource, ArchiveResource and Link classes.

API reference: https://www.contentful.com/developers/docs/references/content-delivery-api/#/introduction/common-resource-attributes

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class Resource(object):
    """
    Base resource class.

    Implements common resource attributes.

    API reference: https://www.contentful.com/developers/docs/references/content-delivery-api/#/introduction/common-resource-attributes
    """

    def __init__(self, item, default_locale='en-US', client=None):
        self.raw = item
        self.default_locale = default_locale
        self._client = client
        self.sys = self._hydrate_sys(item)

    @classmethod
    def base_url(klass, space_id='', resource_id=None, environment_id=None, **kwargs):
        """
        Returns the URI for the resource.
        """

        url = "spaces/{0}".format(
            space_id)

        if environment_id is not None:
            url = url = "{0}/environments/{1}".format(url, environment_id)

        url = "{0}/{1}".format(
            url,
            base_path_for(klass.__name__)
        )

        if resource_id:
            url = "{0}/{1}".format(url, resource_id)

        return url

    @classmethod
    def create_attributes(klass, attributes, previous_object=None):
        """
        Attributes for resource creation.
        """

        result = {}

        if previous_object is not None:
            result = {k: v for k, v in previous_object.to_json().items() if k != 'sys'}

        result.update(attributes)

        return result

    @classmethod
    def create_headers(klass, attributes):
        """
        Headers for resource creation.
        """

        return {}

    @classmethod
    def update_attributes_map(klass):
        """
        Defines keys and default values for non-generic attributes.
        """

        return {}

    def delete(self):
        """
        Deletes the resource.
        """

        return self._client._delete(
            self.__class__.base_url(
                self.sys['space'].id,
                self.sys['id'],
                environment_id=self._environment_id
            )
        )

    def update(self, attributes=None):
        """
        Updates the resource with attributes.
        """

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
        """
        Saves the current state of the resource.
        """

        return self.update()

    def reload(self, result=None):
        """
        Reloads the resource.
        """

        if result is None:
            result = self._client._get(
                self.__class__.base_url(
                    self.sys['space'].id,
                    self.sys['id'],
                    environment_id=self._environment_id
                )
            )

        self._update_from_resource(result)

        return self

    def to_link(self):
        """
        Returns a link for the resource.
        """

        link_type = self.link_type if self.type == 'Link' else self.type

        return Link({'sys': {'linkType': link_type, 'id': self.sys.get('id')}}, client=self._client)

    def to_json(self):
        """
        Returns the JSON representation of the resource.
        """

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
            if k in self._linkables():
                v = self._build_link(v)
            if k in self._dateables():
                v = dateutil.parser.parse(v)
            sys[snake_case(k)] = v
        return sys

    def _linkables(self):
        return ['space', 'contentType', 'createdBy',
                'updatedBy', 'publishedBy', 'environment']

    def _dateables(self):
        return ['createdAt', 'updatedAt', 'deletedAt',
                'firstPublishedAt', 'publishedAt', 'expiresAt']

    def _build_link(self, link):
        return Link(link, client=self._client)

    def _update_headers(self):
        return {'x-contentful-version': str(self.sys['version'])}

    def _update_url(self):
        return self.__class__.base_url(
                self.sys['space'].id,
                self.sys['id'],
                environment_id=self._environment_id
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

    @property
    def _environment_id(self):
        """
        Returns the Environment ID.
        """
        try:
            return super(Resource, self)._environment_id
        except AttributeError:
            # In Resources which do not inherit EnvironmentAwareResource an AttributeError will happen
            return None

    def __getattr__(self, name, *args, **kwargs):
        if name in ['__getstate__', '__setstate__']:
            return super(Resource, self).__getattr__(name, *args, **kwargs)
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
    Fields resource class.

    Implements locale handling for resource fields.
    """

    @classmethod
    def create_attributes(klass, attributes, previous_object=None):
        """
        Attributes for resource creation.
        """

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
        """
        Get fields for a specific locale.

        :param locale: (optional) Locale to fetch, defaults to default_locale.
        """

        if locale is None:
            locale = self._locale()
        return self._fields.get(locale, {})

    def fields_with_locales(self):
        """
        Get fields with locales per field.
        """

        result = {}
        for locale, fields in self._fields.items():
            for k, v in fields.items():
                real_field_id = self._real_field_id_for(k)
                if real_field_id not in result:
                    result[real_field_id] = {}
                result[real_field_id][locale] = self._serialize_value(v)
        return result

    def to_json(self):
        """
        Returns the JSON Representation of the resource.
        """

        result = super(FieldsResource, self).to_json()
        result['fields'] = self.fields_with_locales()
        return result

    @property
    def locale(self):
        """
        Returns the resource locale.
        """

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

    def __getattr__(self, name, *args, **kwargs):
        if name in ['__getstate__', '__setstate__']:
            return super(FieldsResource, self).__getattr__(name, *args, **kwargs)
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
    Allows for resource publish/unpublish.
    """

    @property
    def is_published(self):
        """
        Checks if resource is published.
        """

        return bool(self.sys.get('published_at', False))

    @property
    def is_updated(self):
        """
        Checks if a resource has been updated since last publish.
        Returns False if resource has not been published before.
        """

        if not self.is_published:
            return False

        return sanitize_date(self.sys['published_at']) < sanitize_date(self.sys['updated_at'])

    def publish(self):
        """
        Publishes the resource.
        """

        result = self._client._put(
            "{0}/published".format(
                self.__class__.base_url(
                    self.sys['space'].id,
                    self.sys['id'],
                    environment_id=self._environment_id
                ),
            ),
            {},
            headers=self._update_headers()
        )

        return self.reload(result)

    def unpublish(self):
        """
        Unpublishes the resource.
        """

        self._client._delete(
            "{0}/published".format(
                self.__class__.base_url(
                    self.sys['space'].id,
                    self.sys['id'],
                    environment_id=self._environment_id
                ),
            ),
            headers=self._update_headers()
        )

        return self.reload()


class ArchiveResource(object):
    """
    Allows for resource archive/unarchive.
    """

    @property
    def is_archived(self):
        """
        Checks if Resource is archived.
        """

        return bool(self.sys.get('archived_version', False))

    def archive(self):
        """
        Archives the resource.
        """

        self._client._put(
            "{0}/archived".format(
                self.__class__.base_url(
                    self.sys['space'].id,
                    self.sys['id'],
                    environment_id=self._environment_id
                ),
            ),
            {},
            headers=self._update_headers()
        )

        return self.reload()

    def unarchive(self):
        """
        Unarchives the resource.
        """

        self._client._delete(
            "{0}/archived".format(
                self.__class__.base_url(
                    self.sys['space'].id,
                    self.sys['id'],
                    environment_id=self._environment_id
                ),
            ),
            headers=self._update_headers()
        )

        return self.reload()


class EnvironmentAwareResource(object):
    """
    Allows environment aware resources to resolve the environment ID.
    """

    @property
    def _environment_id(self):
        """
        Returns the Environment ID.
        """

        environment = self.sys.get('environment', None)

        if environment is not None:
            return environment.id
        return 'master'


class Link(Resource):
    """
    Link Class

    API reference: https://www.contentful.com/developers/docs/references/content-delivery-api/#/reference/links
    """

    def resolve(self, space_id=None, environment_id=None):
        """
        Resolves link to a specific resource.
        """

        proxy_method = getattr(
            self._client,
            base_path_for(self.link_type)
        )
        if self.link_type == 'Space':
            return proxy_method().find(self.id)
        elif environment_id is not None:
            return proxy_method(space_id, environment_id).find(self.id)
        else:
            return proxy_method(space_id).find(self.id)

    def to_json(self):
        """
        Returns the JSON representation of the link.
        """

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
