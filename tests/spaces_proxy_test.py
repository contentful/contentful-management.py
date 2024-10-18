import vcr
from unittest import TestCase
from contentful_management.spaces_proxy import SpacesProxy
from contentful_management.errors import NotFoundError
from .test_helper import CLIENT, PLAYGROUND_SPACE


class SpacesProxyTest(TestCase):
    def test_spaces_proxy(self):
        proxy = SpacesProxy(CLIENT)

        self.assertEqual(str(proxy), "<SpacesProxy>")

    @vcr.use_cassette('fixtures/space/all.yaml', decode_compressed_response=True)
    def test_spaces_proxy_all(self):
        proxy = SpacesProxy(CLIENT)

        spaces = []

        self.assertFalse(spaces)

        spaces = proxy.all({'limit': 1})

        self.assertEqual(spaces[0].id, 'cfexampleapi')

    @vcr.use_cassette('fixtures/space/proxy_find.yaml', decode_compressed_response=True)
    def test_spaces_proxy_find(self):
        proxy = SpacesProxy(CLIENT)

        space = proxy.find(PLAYGROUND_SPACE)

        self.assertEqual(space.id, PLAYGROUND_SPACE)

    @vcr.use_cassette('fixtures/space/proxy_delete.yaml', decode_compressed_response=True)
    def test_spaces_proxy_delete(self):
        proxy = SpacesProxy(CLIENT)

        proxy.delete('66zhp0azr4c2')

        with self.assertRaises(NotFoundError):
            proxy.find('66zhp0azr4c2')
