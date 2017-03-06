import vcr
from unittest import TestCase
from contentful_management.snapshots_proxy import SnapshotsProxy
from .test_helper import CLIENT, PLAYGROUND_SPACE


class SnapshotsProxyTest(TestCase):
    def test_snapshots_proxy(self):
        proxy = SnapshotsProxy(CLIENT, PLAYGROUND_SPACE, 'foo')

        self.assertEqual(str(proxy), "<SnapshotsProxy space_id='{0}' entry_id='foo'>".format(PLAYGROUND_SPACE))

        with self.assertRaises(Exception):
            proxy.create()

        with self.assertRaises(Exception):
            proxy.delete()

    @vcr.use_cassette('fixtures/snapshot/all.yaml')
    def test_content_type_editor_interfaces_proxy_all(self):
        proxy = SnapshotsProxy(CLIENT, PLAYGROUND_SPACE, '4dI1y4PKdWWCSC0CwQakOa')

        snapshots = proxy.all()

        self.assertTrue(snapshots)
        self.assertTrue(snapshots[0].id)

    @vcr.use_cassette('fixtures/snapshot/find.yaml')
    def test_content_type_editor_interfaces_proxy_find(self):
        proxy = SnapshotsProxy(CLIENT, PLAYGROUND_SPACE, '4dI1y4PKdWWCSC0CwQakOa')

        snapshot = proxy.find('7ohZjlae5pmiCsbviCFvds')

        self.assertTrue(snapshot.id, '7ohZjlae5pmiCsbviCFvds')
