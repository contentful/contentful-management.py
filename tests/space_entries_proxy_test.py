import vcr
from unittest import TestCase
from contentful_management.space_entries_proxy import SpaceEntriesProxy
from contentful_management.errors import NotFoundError
from .test_helper import CLIENT, PLAYGROUND_SPACE


class SpaceEntriesProxyTest(TestCase):
    @vcr.use_cassette('fixtures/entry/space_proxy_all.yaml')
    def test_all_entries(self):
        proxy = SpaceEntriesProxy(CLIENT, PLAYGROUND_SPACE)

        entries = proxy.all()

        self.assertTrue(entries)

    @vcr.use_cassette('fixtures/entry/space_proxy_find.yaml')
    def test_find_entry(self):
        proxy = SpaceEntriesProxy(CLIENT, PLAYGROUND_SPACE)

        entry = proxy.find('foo')

        self.assertEqual(entry.id, 'foo')

    @vcr.use_cassette('fixtures/entry/space_proxy_create.yaml')
    def test_create_entry(self):
        proxy = SpaceEntriesProxy(CLIENT, PLAYGROUND_SPACE)

        entry = proxy.create(None, {'content_type_id': 'foo'})

        self.assertTrue(entry.id)

    @vcr.use_cassette('fixtures/entry/space_proxy_delete.yaml')
    def test_delete_entry(self):
        proxy = SpaceEntriesProxy(CLIENT, PLAYGROUND_SPACE)

        proxy.delete('6zRjISJ7peuaGK0iaMskWa')

        with self.assertRaises(NotFoundError):
            proxy.find('6zRjISJ7peuaGK0iaMskWa')
