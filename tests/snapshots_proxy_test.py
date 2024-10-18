import vcr
from unittest import TestCase
from contentful_management.snapshots_proxy import SnapshotsProxy
from .test_helper import CLIENT, PLAYGROUND_SPACE


class SnapshotsProxyTest(TestCase):
    def test_snapshots_proxy(self):
        proxy = SnapshotsProxy(CLIENT, PLAYGROUND_SPACE, 'master', 'foo')

        self.assertEqual(str(proxy), "<SnapshotsProxy[entries] space_id='{0}' environment_id='master' parent_resource_id='foo'>".format(PLAYGROUND_SPACE))

        with self.assertRaises(Exception):
            proxy.create()

        with self.assertRaises(Exception):
            proxy.delete('foo')

    @vcr.use_cassette('fixtures/snapshot/all.yaml', decode_compressed_response=True)
    def test_snapshots_proxy_all_entries(self):
        proxy = SnapshotsProxy(CLIENT, PLAYGROUND_SPACE, 'master', '4dI1y4PKdWWCSC0CwQakOa')

        snapshots = proxy.all()

        self.assertTrue(snapshots)
        self.assertTrue(snapshots[0].id)
        self.assertEqual(str(snapshots[0]), "<Snapshot[Entry] id='7ohZjlae5pmiCsbviCFvds'>")

    @vcr.use_cassette('fixtures/snapshot/find.yaml', decode_compressed_response=True)
    def test_snapshots_proxy_find_entry(self):
        proxy = SnapshotsProxy(CLIENT, PLAYGROUND_SPACE, 'master', '4dI1y4PKdWWCSC0CwQakOa')

        snapshot = proxy.find('7ohZjlae5pmiCsbviCFvds')

        self.assertTrue(snapshot.id, '7ohZjlae5pmiCsbviCFvds')
        self.assertEqual(snapshot.snapshot.name, 'foobar')

    @vcr.use_cassette('fixtures/snapshot/content_type_all.yaml', decode_compressed_response=True)
    def test_snapshots_proxy_all_content_types(self):
        proxy = SnapshotsProxy(CLIENT, PLAYGROUND_SPACE, 'master', 'cat', 'content_types')

        snapshots = proxy.all()

        self.assertTrue(snapshots)
        self.assertTrue(snapshots[0].id)
        self.assertEqual(str(snapshots[0]), "<Snapshot[ContentType] id='5bfy52PVk8HwBfXURLOsWJ'>")

    @vcr.use_cassette('fixtures/snapshot/content_type_find.yaml', decode_compressed_response=True)
    def test_snapshots_proxy_find_content_type(self):
        proxy = SnapshotsProxy(CLIENT, PLAYGROUND_SPACE, 'master', 'cat', 'content_types')

        snapshot = proxy.find('5bfy52PVk8HwBfXURLOsWJ')

        self.assertTrue(snapshot.id, '5bfy52PVk8HwBfXURLOsWJ')
        self.assertEqual(snapshot.snapshot.name, 'Cat')
