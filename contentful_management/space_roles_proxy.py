from .space_resource_proxy import SpaceResourceProxy
from .roles_proxy import RolesProxy


"""
contentful.space_roles_proxy
~~~~~~~~~~~~~~~~~~~~~~~

This module implements the SpaceRolesProxy class.

API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/roles

:copyright: (c) 2017 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class SpaceRolesProxy(SpaceResourceProxy):
    """
    API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/roles
    """

    def _resource_proxy_class(self):
        return RolesProxy
