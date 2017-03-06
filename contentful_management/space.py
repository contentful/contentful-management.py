from .resource import Resource
from .space_content_types_proxy import SpaceContentTypesProxy
from .space_entries_proxy import SpaceEntriesProxy
from .space_assets_proxy import SpaceAssetsProxy
from .space_webhooks_proxy import SpaceWebhooksProxy
from .space_roles_proxy import SpaceRolesProxy
from .space_locales_proxy import SpaceLocalesProxy
from .space_api_keys_proxy import SpaceApiKeysProxy
from .space_uploads_proxy import SpaceUploadsProxy


"""
contentful.space
~~~~~~~~~~~~~~~~

This module implements the Space class.

API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/spaces

:copyright: (c) 2017 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class Space(Resource):
    """
    API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/spaces
    """

    def __init__(self, item, **kwargs):
        super(Space, self).__init__(item, **kwargs)
        self.name = item.get('name', '')

    @classmethod
    def base_url(klass, space_id=None, **kwargs):
        """Returns the URI for the Resource"""

        if space_id is None:
            space_id = ''
        return "spaces/{0}".format(space_id)

    @classmethod
    def create_headers(klass, attributes):
        """Headers for resource creation"""

        if 'organization_id' in attributes:
            return {'x-contentful-organization': attributes['organization_id']}
        return {}

    @classmethod
    def create_attributes(klass, attributes, previous_object=None):
        """Attributes for resource creation"""

        if previous_object is not None:
            return {'name': attributes.get('name', previous_object.name)}
        return {
            'name': attributes.get('name', ''),
            'defaultLocale': attributes['default_locale']
        }

    @classmethod
    def update_attributes_map(klass):
        """Defines keys and default values for non-generic attributes"""

        return {
            'name': '',
            'default_locale': ''
        }

    def update(self, attributes=None):
        """Updates the Resource with attributes"""

        if attributes is None:
            attributes = {}

        headers = self.__class__.create_headers(attributes)
        headers.update(self._update_headers())

        result = self._client._put(
            self.__class__.base_url(
                self.sys['id']
            ),
            self.__class__.create_attributes(attributes, self),
            headers=headers
        )

        self._update_from_resource(result)

        return self

    def reload(self):
        """Reloads the Resource"""

        result = self._client._get(
            self.__class__.base_url(
                self.sys['id']
            )
        )

        self._update_from_resource(result)

        return self

    def delete(self):
        """Deletes the Space"""

        return self._client._delete(
            self.__class__.base_url(
                self.sys['id']
            )
        )

    def to_json(self):
        """Returns the JSON Representation of the Resource"""

        result = super(Space, self).to_json()
        result.update({'name': self.name})
        return result

    def content_types(self):
        """Provides access to Content Type management methods

        API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/content-types

        :return: :class:`SpaceContentTypesProxy <contentful_management.space_content_types_proxy.SpaceContentTypesProxy>` object.
        :rtype: contentful.space_content_types_proxy.SpaceEntriesProxy

        Usage:

            >>> space_content_types_proxy = space.content_types()
            <SpaceContentTypesProxy space_id="cfexampleapi">
        """
        return SpaceContentTypesProxy(self._client, self.id)

    def entries(self):
        """Provides access to Entries management methods

        API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/entries

        :return: :class:`SpaceEntriesProxy <contentful_management.space_entries_proxy.SpaceEntriesProxy>` object.
        :rtype: contentful.space_entries_proxy.SpaceEntriesProxy

        Usage:

            >>> space_entries_proxy = space.entries()
            <SpaceEntriesProxy space_id="cfexampleapi">
        """
        return SpaceEntriesProxy(self._client, self.id)

    def assets(self):
        """Provides access to Assets management methods

        API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/assets

        :return: :class:`SpaceAssetsProxy <contentful_management.space_assets_proxy.SpaceAssetsProxy>` object.
        :rtype: contentful.space_assets_proxy.SpaceAssetsProxy

        Usage:

            >>> space_assets_proxy = space.assets()
            <SpaceAssetsProxy space_id="cfexampleapi">
        """
        return SpaceAssetsProxy(self._client, self.id)

    def locales(self):
        """Provides access to Locale management methods

        API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/locales

        :return: :class:`SpaceLocalesProxy <contentful_management.space_locales_proxy.SpaceLocalesProxy>` object.
        :rtype: contentful.space_locales_proxy.SpaceLocalesProxy

        Usage:

            >>> space_locales_proxy = space.locales()
            <SpaceLocalesProxy space_id="cfexampleapi">
        """
        return SpaceLocalesProxy(self._client, self.id)

    def webhooks(self):
        """Provides access to Webhook management methods

        API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/webhooks

        :return: :class:`SpaceWebhooksProxy <contentful_management.space_webhooks_proxy.SpaceWebhooksProxy>` object.
        :rtype: contentful.space_webhooks_proxy.SpaceWebhooksProxy

        Usage:

            >>> space_webhooks_proxy = space.webhooks()
            <SpaceWebhooksProxy space_id="cfexampleapi">
        """
        return SpaceWebhooksProxy(self._client, self.id)

    def roles(self):
        """Provides access to Role management methods

        API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/roles

        :return: :class:`SpaceRolesProxy <contentful_management.space_roles_proxy.SpaceRolesProxy>` object.
        :rtype: contentful.space_roles_proxy.SpaceRolesProxy

        Usage:

            >>> space_roles_proxy = space.roles()
            <SpaceRolesProxy space_id="cfexampleapi">
        """
        return SpaceRolesProxy(self._client, self.id)

    def api_keys(self):
        """Provides access to Api Key management methods

        API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/api-keys

        :return: :class:`SpaceApiKeysProxy <contentful_management.space_api_keys_proxy.SpaceApiKeysProxy>` object.
        :rtype: contentful.space_api_keys_proxy.SpaceApiKeysProxy

        Usage:

            >>> space_api_keys_proxy = space.api_keys()
            <SpaceApiKeysProxy space_id="cfexampleapi">
        """
        return SpaceApiKeysProxy(self._client, self.id)

    def uploads(self):
        """Provides access to Upload management methods

        API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/uploads-keys

        :return: :class:`SpaceApiKeysProxy <contentful_management.space_api_keys_proxy.SpaceApiKeysProxy>` object.
        :rtype: contentful.space_api_keys_proxy.SpaceApiKeysProxy

        Usage:

            >>> space_uploads_proxy = space.uploads()
            <SpaceUploadsProxy space_id="cfexampleapi">
        """
        return SpaceUploadsProxy(self._client, self.id)

    def __repr__(self):
        return "<Space[{0}] id='{1}'>".format(
            self.name,
            self.id
        )
