from unittest import TestCase
from contentful_management.content_type_resource_proxy import ContentTypeResourceProxy
from .test_helper import CLIENT, PLAYGROUND_SPACE


class ContentTypeResourceProxyTest(TestCase):
    def test_resource_proxy_must_be_implemented(self):
        with self.assertRaises(Exception):
            ContentTypeResourceProxy(CLIENT, PLAYGROUND_SPACE, 'master', 'foo')
