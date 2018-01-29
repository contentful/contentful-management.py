from .resource import Resource
from .environment_content_types_proxy import EnvironmentContentTypesProxy

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

        :return: :class:`SpaceContentTypesProxy <contentful_management.space_content_types_proxy.SpaceContentTypesProxy>` object.
        :rtype: contentful.space_content_types_proxy.SpaceEntriesProxy

        Usage:

            >>> space_content_types_proxy = space.content_types()
            <SpaceContentTypesProxy space_id="cfexampleapi">
        """
        return EnvironmentContentTypesProxy(self._client, self.space_id, self.name)