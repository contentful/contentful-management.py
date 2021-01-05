from .client_proxy import ClientProxy
from .user import User

"""
contentful_management.organization_users_proxy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the OrganizationUsersProxy class.

API reference: https://www.contentful.com/developers/docs/references/user-management-api/#/reference/users

:copyright: (c) 2020 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class OrganizationUsersProxy(ClientProxy):
    """
    API reference: https://www.contentful.com/developers/docs/references/user-management-api/#/reference/users
    """

    def __init__(self, client, organization_id):
        super(OrganizationUsersProxy, self).__init__(client, None)
        self.organization_id = organization_id

    @property
    def _resource_class(self):
        return User

    def _url(self, resource_id=None, **kwargs):
        return self._resource_class.base_url(None, resource_id=resource_id, organization_id=self.organization_id, **kwargs)
