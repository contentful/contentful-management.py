import vcr
from unittest import TestCase
from contentful_management.webhook import Webhook
from contentful_management.errors import NotFoundError
from .test_helper import CLIENT, PLAYGROUND_SPACE

WEBHOOK_ITEM = {
    'name': 'Testhook',
    'url': 'https://example.com',
    'sys': {
        'id': 'foo',
        'type': 'Webhook',
        'space': {
            'sys': {
                'id': 'foobar',
                'type': 'Link',
                'linkType': 'Space'
            }
        }
    }
}

class WebhookTest(TestCase):
    def test_webhook(self):
        webhook = Webhook(WEBHOOK_ITEM)

        self.assertEqual(str(webhook), "<Webhook[Testhook] id='foo'>")

    def test_webhook_to_json(self):
        webhook = Webhook(WEBHOOK_ITEM)

        self.assertEqual(webhook.to_json(), {
            'name': 'Testhook',
            'url': 'https://example.com',
            'topics': [],
            'httpBasicUsername': '',
            'headers': [],
            'sys': {
                'id': 'foo',
                'type': 'Webhook',
                'space': {
                    'sys': {
                        'id': 'foobar',
                        'type': 'Link',
                        'linkType': 'Space'
                    }
                }
            }
        })

    def test_webhook_to_link(self):
        webhook = Webhook(WEBHOOK_ITEM)

        self.assertEqual(webhook.to_link().to_json(), {
            'sys': {
                'id': 'foo',
                'type': 'Link',
                'linkType': 'Webhook'
            }
        })

    def test_fail_create_webhook(self):
        with self.assertRaises(Exception):
            CLIENT.webhooks(PLAYGROUND_SPACE).create({
                'name': 'Klingon',
                'url': 'https://example.com'
            })

    @vcr.use_cassette('fixtures/webhook/create.yaml')
    def test_create_webhook(self):
        webhook = CLIENT.webhooks(PLAYGROUND_SPACE).create({
            'name': 'Klingon',
            'url': 'https://example.com',
            'topics': ['Entry.*']
        })

        self.assertEqual(webhook.name, 'Klingon')
        self.assertEqual(webhook.url, 'https://example.com')

    @vcr.use_cassette('fixtures/webhook/find.yaml')
    def test_update_webhook(self):
        webhook = CLIENT.webhooks(PLAYGROUND_SPACE).find('2xzNZ8gOsq0sz4ueoytkeW')

        with vcr.use_cassette('fixtures/webhook/update.yaml'):
            webhook.name = 'Not Klingon'
            webhook.save()

        self.assertEqual(webhook.name, 'Not Klingon')

    @vcr.use_cassette('fixtures/webhook/find_2.yaml')
    def _test_delete_webhook(self):
        webhook = CLIENT.webhooks(PLAYGROUND_SPACE).find('2xzNZ8gOsq0sz4ueoytkeW')

        with vcr.use_cassette('fixtures/webhook/delete.yaml'):
            webhook.delete()

        with vcr.use_cassette('fixtures/webhook/not_found.yaml'):
            with self.assertRaises(NotFoundError):
                CLIENT.webhooks(PLAYGROUND_SPACE).find('2xzNZ8gOsq0sz4ueoytkeW')
