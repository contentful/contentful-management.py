from .space_resource_proxy import SpaceResourceProxy
from .roles_proxy import RolesProxy


"""
contentful_management.space_roles_proxy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the SpaceRolesProxy class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/roles

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class SpaceRolesProxy(SpaceResourceProxy):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/roles
    """

    def _resource_proxy_class(self):
        return RolesProxy

    def create(self, attributes=None, **kwargs):
        """
        Creates a role with given attributes.
        """

        return super(SpaceRolesProxy, self).create(None, attributes)
