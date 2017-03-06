from .resource import Resource


"""
contentful.role
~~~~~~~~~~~~~~~~~~~~~~~

This module implements the Role class.

API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/roles

:copyright: (c) 2017 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class Role(Resource):
    """
    API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/roles
    """

    def __init__(self, item, **kwargs):
        super(Role, self).__init__(item, **kwargs)
        self.name = item.get('name', '')
        self.description = item.get('description', '')
        self.permissions = item.get('permissions', {})
        self.policies = item.get('policies', [])

    @classmethod
    def update_attributes_map(klass):
        """Defines keys and default values for non-generic attributes"""

        return {
            'name': '',
            'description': '',
            'permissions': {},
            'policies': []
        }

    def to_json(self):
        """Returns the JSON Representation of the Resource"""

        result = super(Role, self).to_json()
        result.update({
            'name': self.name,
            'description': self.description,
            'permissions': self.permissions,
            'policies': self.policies
        })
        return result

    def __repr__(self):
        return "<Role[{0}] id='{1}'>".format(
            self.name,
            self.sys.get('id', '')
        )
