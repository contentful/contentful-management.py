from unittest import TestCase
from contentful_management.client_proxy import ClientProxy
from .test_helper import CLIENT, PLAYGROUND_SPACE


class ClientProxyTest(TestCase):
    def test_resource_must_be_implemented(self):
        proxy = ClientProxy(CLIENT, PLAYGROUND_SPACE)
        with self.assertRaises(Exception):
            proxy._resource_class
