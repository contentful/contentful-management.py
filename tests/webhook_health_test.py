import vcr
from unittest import TestCase
from contentful_management.webhook_health import WebhookHealth
from .test_helper import CLIENT, PLAYGROUND_SPACE

WEBHOOK_HEALTH_ITEM = {
    "sys": {
        "type": "Webhook",
        "id": "bar",
        "space": {
            "sys": {
                "type": "Link",
                "linkType": "Space",
                "id": "yadj1kx9rmg0"
            }
        },
        "createdBy": {
            "sys": {
                "type": "Link",
                "linkType": "WebhookDefinition",
                "id": "foobar"
            }
        }
    },
    "calls": {
        "total": 233,
        "healthy": 102
    }
}


class WebhookHealthTest(TestCase):
    def test_webhook_health(self):
        webhook_health = WebhookHealth(WEBHOOK_HEALTH_ITEM)

        self.assertEqual(str(webhook_health), "<WebhookHealth[foobar] total=233 healthy=102>")

    def test_fail_create_webhook_health(self):
        with self.assertRaises(Exception):
            CLIENT.webhook_health(PLAYGROUND_SPACE, 'foo').create()

    def test_fail_delete_webhook_health(self):
        with self.assertRaises(Exception):
            CLIENT.webhook_health(PLAYGROUND_SPACE, 'foo').delete('foobar')

    @vcr.use_cassette('fixtures/webhook_health/all.yaml', decode_compressed_response=True)
    def test_webhook_health_all(self):
        webhook_health = CLIENT.webhook_health('orzkxlxlq59d', '16ypL3XjNK6oreLPPoVBxI').all()

        self.assertTrue(webhook_health)
        self.assertEqual(str(webhook_health), "<WebhookHealth[16ypL3XjNK6oreLPPoVBxI] total=151 healthy=151>")

    @vcr.use_cassette('fixtures/webhook_health/all.yaml', decode_compressed_response=True)
    def test_webhook_health_find_is_same_as_all(self):
        webhook_health = CLIENT.webhook_health('orzkxlxlq59d', '16ypL3XjNK6oreLPPoVBxI').find()

        self.assertTrue(webhook_health)
        self.assertEqual(str(webhook_health), "<WebhookHealth[16ypL3XjNK6oreLPPoVBxI] total=151 healthy=151>")
