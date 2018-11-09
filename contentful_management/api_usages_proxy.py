from .client_proxy import ClientProxy
from .api_usage import ApiUsage


"""
contentful_management.api_usages_proxy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the ApiUsagesProxy class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/api-usages

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class ApiUsagesProxy(ClientProxy):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/api-usages
    """

    def __init__(self, client, organization_id):
        super(ApiUsagesProxy, self).__init__(client, None)
        self.organization_id = organization_id

    @property
    def _resource_class(self):
        return ApiUsage

    def all(self, usage_type, usage_period_id, api, query=None, *args, **kwargs):
        """
        Gets all api usages by type for a given period an api.
        """

        if query is None:
            query = {}

        mandatory_query = {
            'filters[usagePeriod]': usage_period_id,
            'filters[metric]': api
        }

        mandatory_query.update(query)

        return self.client._get(
            self._url(usage_type),
            mandatory_query,
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

    def _url(self, usage_type):
        return self._resource_class.base_url(self.organization_id, usage_type)

    def __repr__(self):
        return "<{0} organization_id='{1}'>".format(
            self.__class__.__name__,
            self.organization_id
        )
