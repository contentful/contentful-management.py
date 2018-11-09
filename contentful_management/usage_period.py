import dateutil
from .resource import Resource


"""
contentful_management.usage_period
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the UsagePeriod class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/usage-periods

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class UsagePeriod(Resource):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/usage-periods
    """

    def __init__(self, item, **kwargs):
        super(UsagePeriod, self).__init__(item, **kwargs)

        start_date = item.get('startDate', None)
        end_date = item.get('endDate', None)
        self.start_date = dateutil.parser.parse(start_date) if start_date is not None else None
        self.end_date = dateutil.parser.parse(end_date) if end_date is not None else None

    @classmethod
    def base_url(klass, organization_id):
        return "organizations/{0}/usage_periods".format(
            organization_id
        )

    def __repr__(self):
        return "<UsagePeriod id='{0}'>".format(
            self.sys.get('id', '')
        )
