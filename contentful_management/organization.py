from .resource import Resource
from .api_usages_proxy import ApiUsagesProxy
from .usage_periods_proxy import UsagePeriodsProxy


"""
contentful_management.organization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the Organization class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/organizations

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class Organization(Resource):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/organizations
    """

    def __init__(self, item, **kwargs):
        super(Organization, self).__init__(item, **kwargs)
        self.name = item.get('name', '')

    @classmethod
    def base_url(klass, *args, **kwargs):
        """
        Returns the URI for the organization.
        """

        return "organizations"

    def usage_periods(self):
        """
        Provides access to usage periods management methods.

        API reference: TBD

        :return: :class:`UsagePeriodsProxy <contentful_management.usage_periods_proxy.UsagePeriodsProxy>` object.
        :rtype: contentful.usage_periods_proxy.UsagePeriodsProxy

        Usage:

            >>> usage_periods_proxy = organization.usage_periods()
            <UsagePeriodsProxy organization_id="cfexampleapi">
        """

        return UsagePeriodsProxy(self._client, self.id)

    def api_usage(self):
        """
        Provides access to an organizations api usage metrics.

        API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/api-usages

        :return: :class:`ApiUsagesProxy <contentful_management.api_usages_proxy.ApiUsagesProxy>` object.
        :rtype: contentful.api_usages_proxy.ApiUsagesProxy

        Usage:

            >>> api_usages_proxy = organization.api_usage()
            <ApiUsagesProxy organization_id='organization_id'>
        """

        return ApiUsagesProxy(self._client, self.id)

    def __repr__(self):
        return "<Organization[{0}] id='{1}'>".format(
            self.name,
            self.id
        )
