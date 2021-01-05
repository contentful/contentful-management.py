from .resource import Resource


"""
contentful_management.user
~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the User class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/users

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class User(Resource):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/users
    """

    def __init__(self, item, **kwargs):
        super(User, self).__init__(item, **kwargs)
        self.first_name = item.get('firstName', '')
        self.last_name = item.get('lastName', '')
        self.avatar_url = item.get('avatarUrl', '')
        self.email = item.get('email', '')
        self.activated = item.get('activated', False)
        self.sign_in_count = item.get('signInCount', 0)
        self.confirmed = item.get('confirmed', False)

    @classmethod
    def base_url(klass, space_id=None, resource_id=None, organization_id=None, **kwargs):
        """
        Returns the URI for the user.
        """

        if space_id is not None:
            url = "spaces/{0}/users/{1}".format(space_id, resource_id)
        elif organization_id is not None:
            url = "organizations/{0}/users/{1}".format(organization_id, resource_id)
        else:
            url = "users/me"

        return url

    def __repr__(self):
        return "<User[{0} {1}] email='{2}' activated={3} confirmed={4} sign_in_count={5}>".format(
            self.first_name,
            self.last_name,
            self.email,
            self.activated,
            self.confirmed,
            self.sign_in_count
        )
