from .client_proxy import ClientProxy
from .space_periodic_usage import SpacePeriodicUsage


"""
contentful_management.space_periodic_usages_proxy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the SpacePeriodicUsagesProxy class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/usage

:copyright: (c) 2020 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class SpacePeriodicUsagesProxy(ClientProxy):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/usage
    """

    def __init__(self, client, organization_id):
        super(SpacePeriodicUsagesProxy, self).__init__(client, None)
        self.organization_id = organization_id

    @property
    def _resource_class(self):
        return SpacePeriodicUsage

    def all(self, query=None, *args, **kwargs):
        """
        Gets all organization periodic usage grouped by space.
        """

        if query is None:
            query = {}

        return self.client._get(
            self._url(),
            query
        )

    def create(self, file_or_path, **kwargs):
        """
        Not supported.
        """

        raise Exception("Not supported")

    def find(self, *args, **kwargs):
        """
        Not supported.
        """

        raise Exception("Not supported")

    def delete(self, upload_id):
        """
        Not supported.
        """

        raise Exception("Not supported")

    def _url(self):
        return self._resource_class.base_url(self.organization_id)

    def __repr__(self):
        return "<{0} organization_id='{1}'>".format(
            self.__class__.__name__,
            self.organization_id
        )
