from unittest import TestCase
from contentful_management.uploads_proxy import UploadsProxy
from .test_helper import CLIENT, PLAYGROUND_SPACE


class UploadsProxyTest(TestCase):
    def test_not_supported_methods(self):
        proxy = UploadsProxy(CLIENT, PLAYGROUND_SPACE)

        with self.assertRaises(Exception):
            proxy.all()
