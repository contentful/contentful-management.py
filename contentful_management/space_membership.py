from .resource import Resource


"""
contentful.space_membership
~~~~~~~~~~~~~~~~~~~~~~~

This module implements the SpaceMembership class.

API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/space-memberships

:copyright: (c) 2017 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class SpaceMembership(Resource):
    """
    API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/space-memberships
    """

    def __init__(self, item, **kwargs):
        super(SpaceMembership, self).__init__(item, **kwargs)
        self.admin = item.get('admin', False)
        self.roles = item.get('roles', [])
        self.user = item.get('user', None)

    def to_json(self):
        """Returns the JSON Representation of the Resource"""

        result = super(SpaceMembership, self).to_json()
        result.update({
            'admin': self.admin,
            'roles': self.roles
        })
        return result

    def __repr__(self):
        return "<SpaceMembership id='{0}' admin={1}>".format(
            self.sys.get('id', ''),
            self.admin
        )
