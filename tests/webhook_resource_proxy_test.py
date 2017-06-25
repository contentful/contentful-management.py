from unittest import TestCase
from contentful_management.webhook_webhooks_call_proxy import WebhookResourceProxy
from .test_helper import CLIENT, PLAYGROUND_SPACE


class WebhookResourceProxyTest(TestCase):
    def test_resource_proxy_must_be_implemented(self):
        with self.assertRaises(Exception):
            WebhookResourceProxy(CLIENT, PLAYGROUND_SPACE, 'foo')
