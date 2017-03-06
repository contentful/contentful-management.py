from .resource import Resource


"""
contentful.api_key
~~~~~~~~~~~~~~~~~~~~~~~

This module implements the ApiKey class.

API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/api-keys

:copyright: (c) 2017 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class ApiKey(Resource):
    """
    API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/api-keys
    """

    def __init__(self, item, **kwargs):
        super(ApiKey, self).__init__(item, **kwargs)
        self.name = item.get('name', '')
        self.description = item.get('description', '')
        self.access_token = item.get('accessToken', '')

    @classmethod
    def create_attributes(klass, attributes, previous_object=None):
        """Attributes for resource creation"""

        if previous_object is not None:
            return {
                'name': attributes.get('name', previous_object.name),
                'description': attributes.get('description', previous_object.description)
            }
        return {
            'name': attributes.get('name', ''),
            'description': attributes.get('description', '')
        }

    @classmethod
    def update_attributes_map(klass):
        """Defines keys and default values for non-generic attributes"""

        return {
            'name': '',
            'description': '',
            'access_token': ''
        }

    def to_json(self):
        """Returns the JSON Representation of the Resource"""

        result = super(ApiKey, self).to_json()
        result.update({
            'name': self.name,
            'description': self.description,
            'accessToken': self.access_token
        })
        return result

    def __repr__(self):
        return "<ApiKey[{0}] id='{1}'>".format(
            self.name,
            self.sys.get('id', '')
        )
