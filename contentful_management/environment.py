from .resource import Resource
from .environment_content_types_proxy import EnvironmentContentTypesProxy
from .environment_entries_proxy import EnvironmentEntriesProxy
from .environment_assets_proxy import EnvironmentAssetsProxy
from .environment_locales_proxy import EnvironmentLocalesProxy
from .environment_ui_extensions_proxy import EnvironmentUIExtensionsProxy

"""
contentful_management.environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the Environment class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/locales

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class Environment(Resource):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/locales
    """

    def __init__(self, item, **kwargs):
        super(Environment, self).__init__(item, **kwargs)
        self.name = item.get('name', '')

    @classmethod
    def base_url(klass, space_id, resource_id=None, **kwargs):
        """
        Returns the URI for the environment.
        """

        return "spaces/{0}/environments/{1}".format(space_id, resource_id)

    @classmethod
    def create_headers(klass, attributes):
        """
        Headers for environment creation.
        """

        if 'source_environment_id' not in attributes:
            return {}
        return {'X-Contentful-Source-Environment': attributes['source_environment_id']}

    @classmethod
    def create_attributes(klass, attributes, previous_object=None):
        """
        Attributes for environment creation.
        """

        return {'name': attributes.get('name', None)}

    def to_json(self):
        """
        Returns the JSON representation of the environment.
        """

        result = super(Environment, self).to_json()
        result.update({
            'name': self.name
        })

        return result

    def content_types(self):
        """
        Provides access to content type management methods for content types of an environment.

        API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/content-types

        :return: :class:`EnvironmentContentTypesProxy <contentful_management.space_content_types_proxy.EnvironmentContentTypesProxy>` object.
        :rtype: contentful.space_content_types_proxy.EnvironmentContentTypesProxy

        Usage:

            >>> space_content_types_proxy = environment.content_types()
            <EnvironmentContentTypesProxy space_id="cfexampleapi" environment_id="master">
        """

        return EnvironmentContentTypesProxy(self._client, self.space.id, self.id)

    def entries(self):
        """
        Provides access to entry management methods.

        API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/entries

        :return: :class:`EnvironmentEntriesProxy <contentful_management.environment_entries_proxy.EnvironmentEntriesProxy>` object.
        :rtype: contentful.environment_entries_proxy.EnvironmentEntriesProxy

        Usage:

            >>> environment_entries_proxy = environment.entries()
            <EnvironmentEntriesProxy space_id="cfexampleapi" environment_id="master">
        """

        return EnvironmentEntriesProxy(self._client, self.space.id, self.id)

    def assets(self):
        """
        Provides access to asset management methods.

        API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/assets

        :return: :class:`EnvironmentAssetsProxy <contentful_management.environment_assets_proxy.EnvironmentAssetsProxy>` object.
        :rtype: contentful.environment_assets_proxy.EnvironmentAssetsProxy

        Usage:

            >>> environment_assets_proxy = environment.assets()
            <EnvironmentAssetsProxy space_id="cfexampleapi" environment_id="master">
        """

        return EnvironmentAssetsProxy(self._client, self.space.id, self.id)

    def locales(self):
        """
        Provides access to locale management methods.

        API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/locales

        :return: :class:`EnvironmentLocalesProxy <contentful_management.environment_locales_proxy.EnvironmentLocalesProxy>` object.
        :rtype: contentful.environment_locales_proxy.EnvironmentLocalesProxy

        Usage:

            >>> environment_locales_proxy = environment.locales()
            <EnvironmentLocalesProxy space_id="cfexampleapi" environment_id="master">
        """

        return EnvironmentLocalesProxy(self._client, self.space.id, self.id)

    def ui_extensions(self):
        """
        Provides access to UI extensions management methods.

        API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/ui-extensions

        :return: :class:`EnvironmentUIExtensionsProxy <contentful_management.ui_extensions_proxy.EnvironmentUIExtensionsProxy>` object.
        :rtype: contentful.ui_extensions_proxy.EnvironmentUIExtensionsProxy

        Usage:

            >>> ui_extensions_proxy = environment.ui_extensions()
            <EnvironmentUIExtensionsProxy space_id="cfexampleapi" environment_id="master">
        """

        return EnvironmentUIExtensionsProxy(self._client, self.space.id, self.id)

    def __repr__(self):
        return "<Environment[{0}] id='{1}'>".format(
            self.name,
            self.id
        )
