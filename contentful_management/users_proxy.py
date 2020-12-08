from .client_proxy import ClientProxy
from .user import User


"""
contentful_management.users_proxy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the UsersProxy class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/users

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class UsersProxy(ClientProxy):
    def __init__(self, client, space_id=None):
        super(UsersProxy, self).__init__(client, space_id)

    @property
    def _resource_class(self):
        return User

    def create(self, *args, **kwargs):
        """
        Not supported.
        """

        raise Exception("Not Supported")

    def delete(self, *args, **kwargs):
        """
        Not supported.
        """

        raise Exception("Not Supported")

    def all(self, *args, **kwargs):
        """
        Not supported.
        """

        raise Exception("Not Supported")

    def me(self):
        """
        Returns the current user information.
        """

        return self.client._get(self._url())

    def _url(self, resource_id=None, **kwargs):
        return self._resource_class.base_url(space_id=self.space_id, resource_id=resource_id, **kwargs)

    def __repr__(self):
        return "<{0}>".format(
            self.__class__.__name__
        )
