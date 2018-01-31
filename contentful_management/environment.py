from .resource import Resource
from .environment_content_types_proxy import EnvironmentContentTypesProxy
from .environment_entries_proxy import EnvironmentEntriesProxy
from .environment_assets_proxy import EnvironmentAssetsProxy

"""
contentful_management.environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the Environment class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/locales

:copyright: (c) 2017 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class Environment(Resource):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/locales
    """

    def __init__(self, item, **kwargs):
        super(Environment, self).__init__(item, **kwargs)
        self.name = item.get('name', '')
        self.space_id = item['sys']['space']['sys']['id']

    @classmethod
    def base_url(klass, space_id, resource_id=None, **kwargs):
        """
        Returns the URI for the environment.
        """
        return "spaces/{0}/environments/{1}".format(space_id, resource_id)

    @classmethod
    def create_attributes(klass, attributes, previous_object=None):
        """
        Attributes for environment creation.
        """

        result = super(Environment, klass).create_attributes(attributes, previous_object)
        return result

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

            >>> space_content_types_proxy = space.environment("master").content_types()
            <EnvironmentContentTypesProxy space_id="cfexampleapi" environment="master">
        """
        return EnvironmentContentTypesProxy(self._client, self.space_id, self.name)

    def entries(self):
        """
        Provides access to entry management methods.

        API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/entries

        :return: :class:`EnvironmentEntriesProxy <contentful_management.environment_entries_proxy.EnvironmentEntriesProxy>` object.
        :rtype: contentful.environment_entries_proxy.EnvironmentEntriesProxy

        Usage:

            >>> environment_entries_proxy = space.environment("master").entries()
            <EnvironmentEntriesProxy space_id="cfexampleapi" environment="master">
        """
        return EnvironmentEntriesProxy(self._client, self.space_id, self.name)
        
    def assets(self):
        """
        Provides access to asset management methods.

        API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/assets

        :return: :class:`EnvironmentAssetsProxy <contentful_management.environment_assets_proxy.EnvironmentAssetsProxy>` object.
        :rtype: contentful.environment_assets_proxy.EnvironmentAssetsProxy

        Usage:

            >>> environment_assets_proxy = space.environment("master").assets()
            <EnvironmentAssetsProxy space_id="cfexampleapi" environment="master">
        """
        return EnvironmentAssetsProxy(self._client, self.space_id, self.name)