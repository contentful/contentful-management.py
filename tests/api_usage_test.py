import vcr
from unittest import TestCase
from contentful_management.api_usage import ApiUsage
from contentful_management.organization import Organization
from .test_helper import CLIENT

BASE_API_USAGE_ITEM = {
    "sys": {
        "type": "ApiUsage",
        "id": "1_fooOrg",
        "usagePeriod": {
            "sys": {
                "type": "Link",
                "linkType": "UsagePeriod",
                "id": 1
                }
            },
        "organization": {
            "sys": {
                "type": "Link",
                "linkType": "Organization",
                "id": "fooOrg"
                }
            }
        },
    "unitOfMeasure": "apiRequests",
    "interval": "daily",
    "startDate": "2018-06-15T00:00:00.000Z",
    "endDate": "2018-07-14T00:00:00.000Z",
    "usage": [6442, 5952, 8713, 1998, 5209, 2894, 1144, 2152, 4305, 4534, 1832, 5979, 6189, 954,
              4847, 3953, 9094, 1800, 5044, 1232, 920, 2396, 9551, 4350, 2809, 5496, 9442, 7301, 4349, 1778]
}


class ApiUsageTest(TestCase):
    def test_api_usage(self):
        api_usage = ApiUsage(BASE_API_USAGE_ITEM)

        self.assertEqual(str(api_usage), "<ApiUsage id='1_fooOrg'>")
        self.assertEqual(api_usage.start_date.isoformat(), '2018-06-15T00:00:00+00:00')
        self.assertEqual(api_usage.end_date.isoformat(), '2018-07-14T00:00:00+00:00')

    @vcr.use_cassette('fixtures/api_usage/all.yaml')
    def test_api_usage_all(self):
        api_usage = CLIENT.api_usage('test_org').all('organization', 1, 'all_apis')[0]

        self.assertEqual(str(api_usage.usage_period), "<Link[UsagePeriod] id='1'>")
        self.assertEqual(str(api_usage.organization), "<Link[Organization] id='test_org'>")
        self.assertTrue(any(api_usage.usage))

    @vcr.use_cassette('fixtures/api_usage/all.yaml')
    def test_api_usage_organization_all(self):
        organization = Organization({'sys': {'id': 'test_org'}}, client=CLIENT)
        api_usage = organization.api_usage().all('organization', 1, 'all_apis')[0]

        self.assertEqual(str(api_usage.usage_period), "<Link[UsagePeriod] id='1'>")
        self.assertEqual(str(api_usage.organization), "<Link[Organization] id='test_org'>")
        self.assertTrue(any(api_usage.usage))
