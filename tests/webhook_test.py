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

    def test_webhook_calls(self):
        webhook = Webhook(WEBHOOK_ITEM)

        calls_proxy = webhook.calls()

        self.assertEqual(str(calls_proxy), "<WebhookWebhooksCallProxy space_id='foobar' webhook_id='foo'>")

    def test_webhook_health(self):
        webhook = Webhook(WEBHOOK_ITEM)

        health_proxy = webhook.health()

        self.assertEqual(str(health_proxy), "<WebhookWebhooksHealthProxy space_id='foobar' webhook_id='foo'>")

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

    @vcr.use_cassette('fixtures/webhook/create.yaml', decode_compressed_response=True)
    def test_create_webhook(self):
        webhook = CLIENT.webhooks(PLAYGROUND_SPACE).create({
            'name': 'Klingon',
            'url': 'https://example.com',
            'topics': ['Entry.*']
        })

        self.assertEqual(webhook.name, 'Klingon')
        self.assertEqual(webhook.url, 'https://example.com')

    @vcr.use_cassette('fixtures/webhook/find.yaml', decode_compressed_response=True)
    def test_update_webhook(self):
        webhook = CLIENT.webhooks(PLAYGROUND_SPACE).find('2xzNZ8gOsq0sz4ueoytkeW')

        with vcr.use_cassette('fixtures/webhook/update.yaml'):
            webhook.name = 'Not Klingon'
            webhook.save()

        self.assertEqual(webhook.name, 'Not Klingon')

    @vcr.use_cassette('fixtures/webhook/find_2.yaml', decode_compressed_response=True)
    def test_delete_webhook(self):
        webhook = CLIENT.webhooks(PLAYGROUND_SPACE).find('2xzNZ8gOsq0sz4ueoytkeW')

        with vcr.use_cassette('fixtures/webhook/delete.yaml'):
            webhook.delete()

        with vcr.use_cassette('fixtures/webhook/not_found.yaml'):
            with self.assertRaises(NotFoundError):
                CLIENT.webhooks(PLAYGROUND_SPACE).find('2xzNZ8gOsq0sz4ueoytkeW')

    @vcr.use_cassette('fixtures/webhook/create_with_filter.yaml', decode_compressed_response=True)
    def test_create_with_filter(self):
        webhook = CLIENT.webhooks(PLAYGROUND_SPACE).create({
            'name': 'Test Filters',
            'url': 'https://example.com',
            'topics': ['Entry.*'],
            'filters': [{"equals": [{"doc": "sys.environment.sys.id"}, "some-env-id"]}]
        })

        self.assertEqual(webhook.filters[0], {"equals": [{"doc": "sys.environment.sys.id"}, "some-env-id"]})

    @vcr.use_cassette('fixtures/webhook/create_with_transformation.yaml', decode_compressed_response=True)
    def test_create_with_transformation(self):
        webhook = CLIENT.webhooks(PLAYGROUND_SPACE).create({
            'name': 'Test Transformation',
            'url': 'https://example.com',
            'topics': ['Entry.*'],
            'transformation': {
                'method': 'POST',
                'contentType': 'application/vnd.contentful.management.v1+json; charset=utf-8',
                'body': {
                    "entryId": "{ /payload/sys/id }",
                    "fields": "{ /payload/fields }"
                }
            }
        })

        self.assertEqual(webhook.transformation, {
            'method': 'POST',
            'contentType': 'application/vnd.contentful.management.v1+json; charset=utf-8',
            'body': {
                "entryId": "{ /payload/sys/id }",
                "fields": "{ /payload/fields }"
            }
        })
