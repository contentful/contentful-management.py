from .resource import Resource
from .space_periodic_usages_proxy import SpacePeriodicUsagesProxy
from .organization_periodic_usages_proxy import OrganizationPeriodicUsagesProxy


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

    def periodic_usages(self):
        """
        Provides access to organization periodic usages management methods.

        API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/usage

        :return: :class:`OrganizationPeriodicUsagesProxy <contentful_management.organization_periodic_usages_proxy.OrganizationPeriodicUsagesProxy>` object.
        :rtype: contentful.organization_periodic_usages_proxy.OrganizationPeriodicUsagesProxy

        Usage:

            >>> organization_periodic_usages_proxy = organization.usage_periods()
            <OrganizationPeriodicUsagesProxy organization_id="cfexampleapi">
        """

        return OrganizationPeriodicUsagesProxy(self._client, self.id)

    def space_periodic_usages(self):
        """
        Provides access to organization periodic usages grouped by space management methods.

        API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/usage

        :return: :class:`SpacePeriodicUsagesProxy<contentful_management.space_periodic_usages_proxy.SpacePeriodicUsagesProxy>` object.
        :rtype: contentful.space_periodic_usages_proxy.SpacePeriodicUsagesProxy

        Usage:

            >>> space_periodic_usages_proxy = organization.space_usage_periods()
            <SpacePeriodicUsagesProxyorganization_id="cfexampleapi">
        """

        return SpacePeriodicUsagesProxy(self._client, self.id)

    def __repr__(self):
        return "<Organization[{0}] id='{1}'>".format(
            self.name,
            self.id
        )
