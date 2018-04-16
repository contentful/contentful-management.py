from unittest import TestCase
from contentful_management.content_type_snapshots_proxy import ContentTypeSnapshotsProxy
from .test_helper import CLIENT, PLAYGROUND_SPACE


class ContentTypeSnapshotsProxyTest(TestCase):
    def test_content_type_snapshots_proxy_not_supported_methods(self):
        proxy = ContentTypeSnapshotsProxy(CLIENT, PLAYGROUND_SPACE, 'master', 'foo')

        with self.assertRaises(Exception):
            proxy.create({'foo': 'bar'})

        with self.assertRaises(Exception):
            proxy.delete('foo')
