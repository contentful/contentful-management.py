from .space_resource_proxy import SpaceResourceProxy
from .users_proxy import UsersProxy

"""
contentful_management.space_users_proxy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the SpaceUsersProxy class.

API reference: https://www.contentful.com/developers/docs/references/user-management-api/#/reference/users

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class SpaceUsersProxy(SpaceResourceProxy):
    """
    API reference: https://www.contentful.com/developers/docs/references/user-management-api/#/reference/users
    """

    def _resource_proxy_class(self):
        return UsersProxy
