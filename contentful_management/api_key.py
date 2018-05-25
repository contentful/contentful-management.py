from .resource import Resource, Link


"""
contentful_management.api_key
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the ApiKey class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/api-keys

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class ApiKey(Resource):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/api-keys
    """

    def __init__(self, item, **kwargs):
        super(ApiKey, self).__init__(item, **kwargs)
        self.name = item.get('name', '')
        self.description = item.get('description', '')
        self.access_token = item.get('accessToken', '')
        self.policies = item.get('policies', [])
        self.environments = [Link(e, **kwargs) for e in item.get('environments', [])]

        preview_api_key = item.get('preview_api_key', None)
        self._preview_api_key = Link(preview_api_key, **kwargs) if preview_api_key is not None else None

    @classmethod
    def create_attributes(klass, attributes, previous_object=None):
        """
        Attributes for resource creation.
        """

        return {
            'name': attributes.get(
                'name',
                previous_object.name if previous_object is not None else ''
            ),
            'description': attributes.get(
                'description',
                previous_object.description if previous_object is not None else ''
            ),
            'environments': attributes.get(
                'environments',
                [e.to_json() for e in previous_object.environments] if previous_object is not None else []  # Will default to master if empty
            )
        }

    @classmethod
    def update_attributes_map(klass):
        """
        Defines keys and default values for non-generic attributes.
        """

        return {
            'name': '',
            'description': '',
            'access_token': '',
            'environments': []
        }

    def preview_api_key(self):
        return self._preview_api_key.resolve(self.space.id)

    def to_json(self):
        """
        Returns the JSON representation of the API key.
        """

        result = super(ApiKey, self).to_json()
        result.update({
            'name': self.name,
            'description': self.description,
            'accessToken': self.access_token,
            'environments': [e.to_json() for e in self.environments]
        })
        return result

    def __repr__(self):
        return "<ApiKey[{0}] id='{1}' access_token='{2}'>".format(
            self.name,
            self.sys.get('id', ''),
            self.access_token
        )
