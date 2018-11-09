from .client_proxy import ClientProxy
from .usage_period import UsagePeriod


"""
contentful_management.usage_periods_proxy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the UsagePeriodsProxy class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/usage-periods

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class UsagePeriodsProxy(ClientProxy):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/usage-periods
    """

    def __init__(self, client, organization_id):
        super(UsagePeriodsProxy, self).__init__(client, None)
        self.organization_id = organization_id

    @property
    def _resource_class(self):
        return UsagePeriod

    def all(self, *args, **kwargs):
        """
        Gets all usage periods.
        """

        return self.client._get(
            self._url(),
            {},
            headers={
                'x-contentful-enable-alpha-feature': 'usage-insights'
            }
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
