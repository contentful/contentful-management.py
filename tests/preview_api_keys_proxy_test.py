from unittest import TestCase
from contentful_management.preview_api_keys_proxy import PreviewApiKeysProxy
from .test_helper import CLIENT, PLAYGROUND_SPACE


class PreviewApiKeysProxyTest(TestCase):
    def test_preview_api_keys_proxy(self):
        proxy = PreviewApiKeysProxy(CLIENT, PLAYGROUND_SPACE)

        self.assertEqual(str(proxy), "<PreviewApiKeysProxy space_id='{0}'>".format(PLAYGROUND_SPACE))
