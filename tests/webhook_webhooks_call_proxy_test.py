import vcr
from unittest import TestCase
from contentful_management.webhook_webhooks_call_proxy import WebhookWebhooksCallProxy
from .test_helper import CLIENT


class WebhookWebhooksCallProxyTest(TestCase):
    def test_webhook_webhooks_call_proxy(self):
        proxy = WebhookWebhooksCallProxy(CLIENT, 'orzkxlxlq59d', '16ypL3XjNK6oreLPPoVBxI')

        self.assertEqual(str(proxy), "<WebhookWebhooksCallProxy space_id='orzkxlxlq59d' webhook_id='16ypL3XjNK6oreLPPoVBxI'>")

    def test_webhook_webhooks_call_proxy_not_supported_methods(self):
        proxy = WebhookWebhooksCallProxy(CLIENT, 'orzkxlxlq59d', '16ypL3XjNK6oreLPPoVBxI')

        with self.assertRaises(Exception):
            proxy.create()

        with self.assertRaises(Exception):
            proxy.delete('foo')

    @vcr.use_cassette('fixtures/webhook_call/all.yaml', decode_compressed_response=True)
    def test_webhook_webhooks_call_proxy_all(self):
        proxy = WebhookWebhooksCallProxy(CLIENT, 'orzkxlxlq59d', '16ypL3XjNK6oreLPPoVBxI')

        webhook_calls = []

        self.assertFalse(webhook_calls)

        webhook_calls = proxy.all({'limit': 1})

        self.assertTrue(webhook_calls)

        self.assertEqual(str(webhook_calls[0]), "<WebhookCall[201] id='4KYbXQ9cg8CE2aqouWqY2i' url='https://circleci.com/api/v1/project/...' request_at='2017-06-21T22:44:42.624000+00:00' response_at='2017-06-21T22:44:43.086000+00:00'>")

    @vcr.use_cassette('fixtures/webhook_call/find.yaml', decode_compressed_response=True)
    def test_webhook_webhooks_call_proxy_find(self):
        proxy = WebhookWebhooksCallProxy(CLIENT, 'orzkxlxlq59d', '16ypL3XjNK6oreLPPoVBxI')

        webhook_call = proxy.find('4KYbXQ9cg8CE2aqouWqY2i')

        self.assertEqual(str(webhook_call), "<WebhookCall[201] id='4KYbXQ9cg8CE2aqouWqY2i' url='https://circleci.com/api/v1/project/...' request_at='2017-06-21T22:44:42.624000+00:00' response_at='2017-06-21T22:44:43.086000+00:00'>")
