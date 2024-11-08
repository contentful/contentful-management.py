from unittest import TestCase
from contentful_management.entry_resource_proxy import EntryResourceProxy
from .test_helper import CLIENT, PLAYGROUND_SPACE


class EntryResourceProxyTest(TestCase):
    def test_resource_proxy_must_be_implemented(self):
        with self.assertRaises(Exception):
            EntryResourceProxy(CLIENT, PLAYGROUND_SPACE, 'foo', 'master')
