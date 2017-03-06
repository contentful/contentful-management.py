from unittest import TestCase
from contentful_management.api_keys_proxy import ApiKeysProxy
from .test_helper import CLIENT, PLAYGROUND_SPACE


class ApiKeysProxyTest(TestCase):
    def test_api_keys_proxy(self):
        proxy = ApiKeysProxy(CLIENT, PLAYGROUND_SPACE)

        self.assertEqual(str(proxy), "<ApiKeysProxy space_id='{0}'>".format(PLAYGROUND_SPACE))
