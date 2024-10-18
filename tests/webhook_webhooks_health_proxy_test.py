import vcr
from unittest import TestCase
from contentful_management.webhook_webhooks_health_proxy import WebhookWebhooksHealthProxy
from .test_helper import CLIENT


class WebhookWebhooksHealthProxyTest(TestCase):
    def test_webhook_webhooks_health_proxy(self):
        proxy = WebhookWebhooksHealthProxy(CLIENT, 'orzkxlxlq59d', '16ypL3XjNK6oreLPPoVBxI')

        self.assertEqual(str(proxy), "<WebhookWebhooksHealthProxy space_id='orzkxlxlq59d' webhook_id='16ypL3XjNK6oreLPPoVBxI'>")

    def test_webhook_webhooks_health_proxy_not_supported_methods(self):
        proxy = WebhookWebhooksHealthProxy(CLIENT, 'orzkxlxlq59d', '16ypL3XjNK6oreLPPoVBxI')

        with self.assertRaises(Exception):
            proxy.create()

        with self.assertRaises(Exception):
            proxy.delete('foo')

    @vcr.use_cassette('fixtures/webhook_health/all.yaml', decode_compressed_response=True)
    def test_webhook_webhooks_health_proxy_all(self):
        proxy = WebhookWebhooksHealthProxy(CLIENT, 'orzkxlxlq59d', '16ypL3XjNK6oreLPPoVBxI')

        webhook_health = proxy.all()

        self.assertEqual(str(webhook_health), "<WebhookHealth[16ypL3XjNK6oreLPPoVBxI] total=151 healthy=151>")

    @vcr.use_cassette('fixtures/webhook_health/find.yaml', decode_compressed_response=True)
    def test_webhook_webhooks_health_proxy_find(self):
        proxy = WebhookWebhooksHealthProxy(CLIENT, 'orzkxlxlq59d', '16ypL3XjNK6oreLPPoVBxI')

        webhook_health = proxy.find()

        self.assertEqual(str(webhook_health), "<WebhookHealth[16ypL3XjNK6oreLPPoVBxI] total=151 healthy=151>")
