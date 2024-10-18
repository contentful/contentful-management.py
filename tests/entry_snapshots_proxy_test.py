import vcr
from unittest import TestCase
from contentful_management.entry_snapshots_proxy import EntrySnapshotsProxy
from .test_helper import CLIENT, PLAYGROUND_SPACE


class EntrySnapshotsProxyTest(TestCase):
    def test_entry_snapshots_proxy(self):
        proxy = EntrySnapshotsProxy(CLIENT, PLAYGROUND_SPACE, 'master', '4dI1y4PKdWWCSC0CwQakOa')

        self.assertEqual(str(proxy), "<EntrySnapshotsProxy space_id='{0}' environment_id='master' entry_id='4dI1y4PKdWWCSC0CwQakOa'>".format(PLAYGROUND_SPACE))

    def test_entry_snapshots_proxy_not_supported_methods(self):
        proxy = EntrySnapshotsProxy(CLIENT, PLAYGROUND_SPACE, 'master', '4dI1y4PKdWWCSC0CwQakOa')

        with self.assertRaises(Exception):
            proxy.create()

        with self.assertRaises(Exception):
            proxy.delete()

    @vcr.use_cassette('fixtures/entry/snapshot_all.yaml', decode_compressed_response=True)
    def test_entry_snapshots_proxy_all(self):
        proxy = EntrySnapshotsProxy(CLIENT, PLAYGROUND_SPACE, 'master', '4dI1y4PKdWWCSC0CwQakOa')

        snapshots = []

        self.assertFalse(snapshots)

        snapshots = proxy.all()

        self.assertTrue(snapshots)
