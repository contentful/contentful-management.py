from .resource import Resource


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

    @classmethod
    def base_url(klass, space_id, resource_id=None, **kwargs):
        """
        Returns the URI for the environment.
        """
        return "spaces/{0}/environment/{resource_id}".format(space_id)

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