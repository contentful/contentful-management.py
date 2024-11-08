import vcr
from unittest import TestCase
from contentful_management.space_periodic_usage import SpacePeriodicUsage
from .test_helper import CLIENT

TEST_ORG_ID = "org_id"

BASE_SPACE_PERIODIC_USAGE_ITEM = {
        "metric": "cda",
        "usage": 39,
        "usagePerDay": {
            "2020-02-26": 39,
            "2020-02-27": 0,
            "2020-02-28": 0,
            "2020-02-29": 0,
            "2020-03-01": 0,
            "2020-03-02": 0,
            "2020-03-03": 0,
            "2020-03-04": 0,
            "2020-03-05": 0
        },
        "unitOfMeasure": "apiRequestsCount",
        "sys": {
            "type": "SpacePeriodicUsage",
            "id": "usage-cda-SPACE_ID-2020-02-26-2020-03-05",
            "space": {
                "sys": {
                    "type": "Link",
                    "linkType": "Space",
                    "id": "SPACE_ID"
                }
            }
        },
        "dateRange": {
            "startAt": "2020-02-26",
            "endAt": "2020-03-05"
        }
}


class SpacePeriodicUsageTest(TestCase):
    def test_space_periodic_usage(self):
        space_periodic_usage = SpacePeriodicUsage(BASE_SPACE_PERIODIC_USAGE_ITEM)

        self.assertEqual(str(space_periodic_usage), "<SpacePeriodicUsage id='usage-cda-SPACE_ID-2020-02-26-2020-03-05'>")

    @vcr.use_cassette('fixtures/space_periodic_usage/all.yaml', decode_compressed_response=True)
    def test_organization_space_periodic_usage_all(self):
        organization = [o for o in CLIENT.organizations().all() if o.id == TEST_ORG_ID][0]
        space_periodic_usage = organization.space_periodic_usages().all()[0]

        self.assertEqual(str(space_periodic_usage), "<SpacePeriodicUsage id='usage-cma-fj3kyv4vsm89-2020-01-21-2020-03-05'>")

    @vcr.use_cassette('fixtures/space_periodic_usage/all.yaml', decode_compressed_response=True)
    def test_space_periodic_usage_all(self):
        space_periodic_usage = CLIENT.space_periodic_usages(TEST_ORG_ID).all()[0]

        self.assertEqual(str(space_periodic_usage), "<SpacePeriodicUsage id='usage-cma-fj3kyv4vsm89-2020-01-21-2020-03-05'>")
