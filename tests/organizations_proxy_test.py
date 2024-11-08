import vcr
from unittest import TestCase
from contentful_management.organizations_proxy import OrganizationsProxy
from .test_helper import CLIENT


class OrganizationsProxyTest(TestCase):
    def test_spaces_proxy(self):
        proxy = OrganizationsProxy(CLIENT)

        self.assertEqual(str(proxy), "<OrganizationsProxy>")

    @vcr.use_cassette('fixtures/organization/all.yaml', decode_compressed_response=True)
    def test_organizations_proxy_all(self):
        proxy = OrganizationsProxy(CLIENT)

        organizations = []

        self.assertFalse(organizations)

        organizations = proxy.all({'limit': 1})

        self.assertEqual(len(organizations), 1)

    def test_organizations_proxy_find(self):
        proxy = OrganizationsProxy(CLIENT)

        with self.assertRaises(Exception):
            proxy.find('foo')

    def test_organizations_proxy_delete(self):
        proxy = OrganizationsProxy(CLIENT)

        with self.assertRaises(Exception):
            proxy.delete('foo')

    def test_organizations_proxy_create(self):
        proxy = OrganizationsProxy(CLIENT)

        with self.assertRaises(Exception):
            proxy.create('foo')
