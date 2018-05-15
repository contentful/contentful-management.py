from .client_proxy import ClientProxy
from .organization import Organization


"""
contentful_management.organizations_proxy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the OrganizationsProxy class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/organizations

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class OrganizationsProxy(ClientProxy):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/organizations
    """

    def __init__(self, client):
        super(OrganizationsProxy, self).__init__(client, None)

    def __repr__(self):
        return "<OrganizationsProxy>"

    @property
    def _resource_class(self):
        return Organization

    def all(self, query=None, **kwargs):
        """
        Gets all organizations.
        """

        return super(OrganizationsProxy, self).all(query=query)

    def find(self, organization_id, query=None, **kwargs):
        """
        Not supported.
        """

        raise Exception("Not supported")

    def create(self, attributes=None, **kwargs):
        """
        Not supported.
        """

        raise Exception("Not supported")

    def delete(self, organization_id):
        """
        Not supported.
        """

        raise Exception("Not supported")
