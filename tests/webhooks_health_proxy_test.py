from unittest import TestCase
from contentful_management.webhooks_health_proxy import WebhooksHealthProxy
from .test_helper import CLIENT


class WebhooksHealthProxyTest(TestCase):
    def test_webhooks_health_proxy(self):
        proxy = WebhooksHealthProxy(CLIENT, 'orzkxlxlq59d', '16ypL3XjNK6oreLPPoVBxI')

        self.assertEqual(str(proxy), "<WebhooksHealthProxy space_id='orzkxlxlq59d' webhook_id='16ypL3XjNK6oreLPPoVBxI'>")
