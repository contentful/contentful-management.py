from .resource import Resource
from .space_roles_proxy import SpaceRolesProxy
from .uploads_proxy import UploadsProxy
from .space_api_keys_proxy import SpaceApiKeysProxy
from .space_webhooks_proxy import SpaceWebhooksProxy
from .space_environments_proxy import SpaceEnvironmentsProxy
from .space_preview_api_keys_proxy import SpacePreviewApiKeysProxy
from .space_space_memberships_proxy import SpaceSpaceMembershipsProxy


"""
contentful_management.space
~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the Space class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/spaces

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class Space(Resource):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/spaces
    """

    def __init__(self, item, **kwargs):
        super(Space, self).__init__(item, **kwargs)
        self.name = item.get('name', '')

    @classmethod
    def base_url(klass, space_id=None, **kwargs):
        """
        Returns the URI for the space.
        """

        if space_id is None:
            space_id = ''
        return "spaces/{0}".format(space_id)

    @classmethod
    def create_headers(klass, attributes):
        """
        Headers for space creation.
        """

        if 'organization_id' in attributes:
            return {'x-contentful-organization': attributes['organization_id']}
        return {}

    @classmethod
    def create_attributes(klass, attributes, previous_object=None):
        """Attributes for space creation."""

        if previous_object is not None:
            return {'name': attributes.get('name', previous_object.name)}
        return {
            'name': attributes.get('name', ''),
            'defaultLocale': attributes['default_locale']
        }

    @classmethod
    def update_attributes_map(klass):
        """
        Defines keys and default values for non-generic attributes.
        """

        return {
            'name': '',
            'default_locale': ''
        }

    def update(self, attributes=None):
        """Updates the space with attributes."""

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
        """
        Reloads the space.
        """

        result = self._client._get(
            self.__class__.base_url(
                self.sys['id']
            )
        )

        self._update_from_resource(result)

        return self

    def delete(self):
        """
        Deletes the space
        """

        return self._client._delete(
            self.__class__.base_url(
                self.sys['id']
            )
        )

    def to_json(self):
        """
        Returns the JSON representation of the space.
        """

        result = super(Space, self).to_json()
        result.update({'name': self.name})
        return result

    def webhooks(self):
        """
        Provides access to webhook management methods.

        API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/webhooks

        :return: :class:`SpaceWebhooksProxy <contentful_management.space_webhooks_proxy.SpaceWebhooksProxy>` object.
        :rtype: contentful.space_webhooks_proxy.SpaceWebhooksProxy

        Usage:

            >>> space_webhooks_proxy = space.webhooks()
            <SpaceWebhooksProxy space_id="cfexampleapi">
        """
        return SpaceWebhooksProxy(self._client, self.id)

    def roles(self):
        """
        Provides access to role management methods.

        API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/roles

        :return: :class:`SpaceRolesProxy <contentful_management.space_roles_proxy.SpaceRolesProxy>` object.
        :rtype: contentful.space_roles_proxy.SpaceRolesProxy

        Usage:

            >>> space_roles_proxy = space.roles()
            <SpaceRolesProxy space_id="cfexampleapi">
        """
        return SpaceRolesProxy(self._client, self.id)

    def api_keys(self):
        """
        Provides access to api key management methods.

        API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/api-keys

        :return: :class:`SpaceApiKeysProxy <contentful_management.space_api_keys_proxy.SpaceApiKeysProxy>` object.
        :rtype: contentful.space_api_keys_proxy.SpaceApiKeysProxy

        Usage:

            >>> space_api_keys_proxy = space.api_keys()
            <SpaceApiKeysProxy space_id="cfexampleapi">
        """
        return SpaceApiKeysProxy(self._client, self.id)

    def preview_api_keys(self):
        """
        Provides access to preview api key management methods.

        API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/api-keys/preview-api-key/get-a-single-preview-api-key

        :return: :class:`SpacePreviewApiKeysProxy <contentful_management.space_preview_api_keys_proxy.SpacePreviewApiKeysProxy>` object.
        :rtype: contentful.space_preview_api_keys_proxy.SpacePreviewApiKeysProxy

        Usage:

            >>> space_preview_api_keys_proxy = space.preview_api_keys()
            <SpacePreviewApiKeysProxy space_id="cfexampleapi">
        """
        return SpacePreviewApiKeysProxy(self._client, self.id)

    def memberships(self):
        """
        Provides access to space memberships management methods.

        API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/space-memberships

        :return: :class:`SpaceSpaceMembershipsProxy <contentful_management.space_space_memberships_proxy.SpaceSpaceMembershipsProxy>` object.
        :rtype: contentful.space_space_memberships_proxy.SpaceSpaceMembershipsProxy

        Usage:

            >>> space_space_memberships_proxy = space.memberships()
            <SpaceSpaceMembershipsProxy space_id="cfexampleapi">
        """
        return SpaceSpaceMembershipsProxy(self._client, self.id)

    def uploads(self):
        """
        Provides access to upload management methods.

        API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/uploads

        :return: :class:`SpaceApiKeysProxy <contentful_management.space_api_keys_proxy.SpaceApiKeysProxy>` object.
        :rtype: contentful.space_api_keys_proxy.SpaceApiKeysProxy

        Usage:

            >>> space_uploads_proxy = space.uploads()
            <UploadsProxy space_id="cfexampleapi">
        """
        return UploadsProxy(self._client, self.id)

    def environments(self):
        """
        Provides access to environment management methods.

        API reference: TBD

        :return: :class:`SpaceEnvironmentsProxy <contentful_management.space_environments_proxy` object.
        :rtype: contentful.environments_space_proxy.SpaceEnvironmentsProxy

        Usage:

            >>> space_environments_proxy = space.environments()
            <SpaceEnvironmentsProxy space_id="cfexampleapi">
        """

        return SpaceEnvironmentsProxy(self._client, self.id)

    def __repr__(self):
        return "<Space[{0}] id='{1}'>".format(
            self.name,
            self.id
        )
