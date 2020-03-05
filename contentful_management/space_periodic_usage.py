from .resource import Resource


"""
contentful_management.space_periodic_usage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the SpacePeriodicUsage class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/usage

:copyright: (c) 2020 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class SpacePeriodicUsage(Resource):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/usage
    """

    def __init__(self, item, **kwargs):
        super(SpacePeriodicUsage, self).__init__(item, **kwargs)

        self.unit_of_measure = item.get('unitOfMeasure', None)
        self.metric = item.get('metric', None)
        self.usage = item.get('usage', None)
        self.usage_per_day = item.get('usagePerDay', None)
        self.date_range = item.get('dateRange', None)

    def _linkables(self):
        return super(SpacePeriodicUsage, self)._linkables() + ['organization']

    @classmethod
    def base_url(klass, organization_id):
        return "organizations/{0}/space_periodic_usages".format(organization_id)

    def __repr__(self):
        return "<SpacePeriodicUsage id='{0}'>".format(
            self.sys.get('id', '')
        )
