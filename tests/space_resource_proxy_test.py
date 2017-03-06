from unittest import TestCase
from contentful_management.space_resource_proxy import SpaceResourceProxy
from .test_helper import CLIENT, PLAYGROUND_SPACE


class SpaceResourceProxyTest(TestCase):
    def test_resource_proxy_is_required(self):
        with self.assertRaises(Exception):
            SpaceResourceProxy(CLIENT, PLAYGROUND_SPACE)
