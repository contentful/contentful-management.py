from .client_proxy import ClientProxy
from .space_membership import SpaceMembership


"""
contentful_management.space_memberships_proxy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the SpaceMembershipsProxy class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/space-memberships

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class SpaceMembershipsProxy(ClientProxy):
    @property
    def _resource_class(self):
        return SpaceMembership

    def create(self, attributes=None, **kwargs):
        """
        Creates a space membership with given attributes.
        """

        return super(SpaceMembershipsProxy, self).create(None, attributes)
