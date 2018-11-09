import dateutil
from .resource import Resource


"""
contentful_management.api_usage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the ApiUsage class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/api-usages

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class ApiUsage(Resource):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/api-usages
    """

    def __init__(self, item, **kwargs):
        super(ApiUsage, self).__init__(item, **kwargs)

        self.unit_of_measure = item.get('unitOfMeasure', None)
        self.interval = item.get('interval', None)
        self.usage = item.get('usage', [])

        start_date = item.get('startDate', None)
        end_date = item.get('endDate', None)
        self.start_date = dateutil.parser.parse(start_date) if start_date is not None else None
        self.end_date = dateutil.parser.parse(end_date) if end_date is not None else None

    def _linkables(self):
        return super(ApiUsage, self)._linkables() + ['usagePeriod', 'organization']

    @classmethod
    def base_url(klass, organization_id, usage_type):
        return "organizations/{0}/usages/{1}".format(
            organization_id,
            usage_type
        )

    def __repr__(self):
        return "<ApiUsage id='{0}'>".format(
            self.sys.get('id', '')
        )
