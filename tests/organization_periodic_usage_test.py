import vcr
from unittest import TestCase
from contentful_management.organization_periodic_usage import OrganizationPeriodicUsage
from .test_helper import CLIENT

TEST_ORG_ID = "org_id"

BASE_ORGANIZATION_PERIODIC_USAGE_ITEM = {
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
            "type": "OrganizationPeriodicUsage",
            "id": "usage-cda-ORG_ID-2020-02-26-2020-03-05",
            "space": {
                "sys": {
                    "type": "Link",
                    "linkType": "Organization",
                    "id": "ORG_ID"
                }
            }
        },
        "dateRange": {
            "startAt": "2020-02-26",
            "endAt": "2020-03-05"
        }
}


class OrganizationPeriodicUsageTest(TestCase):
    def test_organization_periodic_usage(self):
        organization_periodic_usage = OrganizationPeriodicUsage(BASE_ORGANIZATION_PERIODIC_USAGE_ITEM)

        self.assertEqual(str(organization_periodic_usage), "<OrganizationPeriodicUsage id='usage-cda-ORG_ID-2020-02-26-2020-03-05'>")

    @vcr.use_cassette('fixtures/organization_periodic_usage/all.yaml', decode_compressed_response=True)
    def test_organization_organization_periodic_usage_all(self):
        organization = [o for o in CLIENT.organizations().all() if o.id == TEST_ORG_ID][0]
        organization_periodic_usage = organization.periodic_usages().all()[0]

        self.assertEqual(str(organization_periodic_usage), "<OrganizationPeriodicUsage id='usage-cma-org_id-2020-01-21-2020-03-05'>")

    @vcr.use_cassette('fixtures/organization_periodic_usage/all.yaml', decode_compressed_response=True)
    def test_organization_periodic_usage_all(self):
        organization_periodic_usage = CLIENT.organization_periodic_usages(TEST_ORG_ID).all()[0]

        self.assertEqual(str(organization_periodic_usage), "<OrganizationPeriodicUsage id='usage-cma-org_id-2020-01-21-2020-03-05'>")
