from .space_resource_proxy import SpaceResourceProxy
from .space_memberships_proxy import SpaceMembershipsProxy


"""
contentful_management.space_space_memberships_proxy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the SpaceSpaceMembershipsProxy class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/space-memberships

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class SpaceSpaceMembershipsProxy(SpaceResourceProxy):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/space-memberships
    """

    def _resource_proxy_class(self):
        return SpaceMembershipsProxy

    def create(self, attributes=None, **kwargs):
        """
        Creates a space membership with given attributes.
        """

        return super(SpaceSpaceMembershipsProxy, self).create(None, attributes)
