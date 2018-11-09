import vcr
from unittest import TestCase
from contentful_management.usage_period import UsagePeriod
from contentful_management.organization import Organization
from .test_helper import CLIENT

BASE_USAGE_PERIOD_ITEM = {
    'sys': {
        'id': 1,
        'type': 'UsagePeriod',
    },
    'startDate': '2018-10-10T20:10:10Z',
    'endDate': None
}


class UsagePeriodTest(TestCase):
    def test_usage_period(self):
        usage_period = UsagePeriod(BASE_USAGE_PERIOD_ITEM)

        self.assertEqual(str(usage_period), "<UsagePeriod id='1'>")
        self.assertEqual(usage_period.start_date.isoformat(), '2018-10-10T20:10:10+00:00')
        self.assertTrue(usage_period.end_date is None)

    @vcr.use_cassette('fixtures/usage_period/all.yaml')
    def test_usage_period_all(self):
        usage_periods = CLIENT.usage_periods('test_org').all()

        self.assertEqual(str(usage_periods[0]), "<UsagePeriod id='2'>")
        self.assertEqual(str(usage_periods[1]), "<UsagePeriod id='1'>")

    @vcr.use_cassette('fixtures/usage_period/all.yaml')
    def test_usage_period_organization_all(self):
        organization = Organization({'sys': {'id': 'test_org'}}, client=CLIENT)
        usage_periods = organization.usage_periods().all()

        self.assertEqual(str(usage_periods[0]), "<UsagePeriod id='2'>")
        self.assertEqual(str(usage_periods[1]), "<UsagePeriod id='1'>")
