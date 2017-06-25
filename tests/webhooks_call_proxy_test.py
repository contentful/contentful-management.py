from unittest import TestCase
from contentful_management.webhooks_call_proxy import WebhooksCallProxy
from .test_helper import CLIENT


class WebhooksCallProxyTest(TestCase):
    def test_webhooks_call_proxy(self):
        proxy = WebhooksCallProxy(CLIENT, 'orzkxlxlq59d', '16ypL3XjNK6oreLPPoVBxI')

        self.assertEqual(str(proxy), "<WebhooksCallProxy space_id='orzkxlxlq59d' webhook_id='16ypL3XjNK6oreLPPoVBxI'>")
