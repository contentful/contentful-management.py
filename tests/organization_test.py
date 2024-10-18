import vcr
from unittest import TestCase
from contentful_management.organization import Organization
from .test_helper import CLIENT

BASE_ORGANIZATION_ITEM = {
    'sys': {
        'id': 'foo',
        'type': 'Organization',
    },
    'name': 'Some organization'
}


class OrganizationTest(TestCase):
    def test_organization(self):
        organization = Organization(BASE_ORGANIZATION_ITEM)

        self.assertEqual(str(organization), "<Organization[Some organization] id='foo'>")

    @vcr.use_cassette('fixtures/organization/all.yaml', decode_compressed_response=True)
    def test_organizations_all(self):
        organizations = CLIENT.organizations().all({'limit': 1})

        self.assertEqual(str(organizations[0]), "<Organization[Test Account 1] id='foobar'>")

    @vcr.use_cassette('fixtures/organization/user.yaml', decode_compressed_response=True)
    def test_organization_user(self):
        organization = CLIENT.organizations().all()[0]

        user = organization.users().find('user_id')

        self.assertEqual(str(user), "<User[Bhushan Lodha] email='bhushanlodha@gmail.com' activated=True confirmed=True sign_in_count=23>")
