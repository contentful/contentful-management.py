from .client_proxy import ClientProxy
from .role import Role


"""
contentful_management.roles_proxy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the RolesProxy class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/roles

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class RolesProxy(ClientProxy):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/roles
    """

    @property
    def _resource_class(self):
        return Role

    def create(self, attributes=None, **kwargs):
        """
        Creates a role with given attributes.
        """

        return super(RolesProxy, self).create(None, attributes)
