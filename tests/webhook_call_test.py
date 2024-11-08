import vcr
from unittest import TestCase
from contentful_management.webhook_call import WebhookCall
from .test_helper import CLIENT, PLAYGROUND_SPACE

WEBHOOK_CALL_ITEM = {
    'errors': [],
    'eventType': 'publish',
    'request': {
        'body': '{"sys":{"space": ... }',
        'headers': {
            'Content-Type': 'application/vnd.contentful.management.v1+json',
            'X-Contentful-Topic': 'ContentManagement.Entry.publish',
            'X-Contentful-Webhook-Name': 'CircleCI'
        },
        'method': 'POST',
        'url': 'https://circleci.com/api/v1/project/...'
    },
    'requestAt': '2017-06-21T22:44:42.624Z',
    'response': {
        'body': '{:previous_successful_build nil, ...',
        'headers': {
            'connection': 'Close',
            'content-length': '2221',
            'date': 'Wed, 21 Jun 2017 22:44:26 GMT',
            'location': 'https://circleci.com/api/v1/project/...',
            'server': 'nginx',
            'strict-transport-security': 'max-age=15724800',
            'x-circleci-scopes': ':write-settings, :view-builds, :read-settings, :trigger-builds, :all, :status, :none',
            'x-frame-options': 'DENY',
            'x-route': '/tree/:branch, :branch, [^,;?]+'
        },
        'statusCode': 201,
        'url': 'https://circleci.com/api/v1/project/...'
    },
    'responseAt': '2017-06-21T22:44:43.086Z',
    'statusCode': 201,
    'sys': {
        'createdAt': '2017-06-21T22:44:42.624Z',
        'createdBy': {
            'sys': {
                'id': '16ypL3XjNK6oreLPPoVBxI',
                'linkType': 'WebhookDefinition',
                'type': 'Link'
            }
        },
        'id': '4KYbXQ9cg8CE2aqouWqY2i',
        'space': {
            'sys': {
                'id': 'orzkxlxlq59d',
                'linkType': 'Space',
                'type': 'Link'
            }
        },
        'type': 'WebhookCallDetails'
    },
    'url': 'https://circleci.com/api/v1/project/...'
}

WEBHOOK_CALL_ITEM_NO_DATE = {
    'errors': [],
    'eventType': 'publish',
    'request': {
        'body': '{"sys":{"space": ... }',
        'headers': {
            'Content-Type': 'application/vnd.contentful.management.v1+json',
            'X-Contentful-Topic': 'ContentManagement.Entry.publish',
            'X-Contentful-Webhook-Name': 'CircleCI'
        },
        'method': 'POST',
        'url': 'https://circleci.com/api/v1/project/...'
    },
    'requestAt': '',
    'response': {
        'body': '{:previous_successful_build nil, ...',
        'headers': {
            'connection': 'Close',
            'content-length': '2221',
            'date': 'Wed, 21 Jun 2017 22:44:26 GMT',
            'location': 'https://circleci.com/api/v1/project/...',
            'server': 'nginx',
            'strict-transport-security': 'max-age=15724800',
            'x-circleci-scopes': ':write-settings, :view-builds, :read-settings, :trigger-builds, :all, :status, :none',
            'x-frame-options': 'DENY',
            'x-route': '/tree/:branch, :branch, [^,;?]+'
        },
        'statusCode': 201,
        'url': 'https://circleci.com/api/v1/project/...'
    },
    'responseAt': '',
    'statusCode': 201,
    'sys': {
        'createdAt': '2017-06-21T22:44:42.624Z',
        'createdBy': {
            'sys': {
                'id': '16ypL3XjNK6oreLPPoVBxI',
                'linkType': 'WebhookDefinition',
                'type': 'Link'
            }
        },
        'id': '4KYbXQ9cg8CE2aqouWqY2i',
        'space': {
            'sys': {
                'id': 'orzkxlxlq59d',
                'linkType': 'Space',
                'type': 'Link'
            }
        },
        'type': 'WebhookCallDetails'
    },
    'url': 'https://circleci.com/api/v1/project/...'
}


class WebhookCallTest(TestCase):
    def test_webhook_call(self):
        webhook_call = WebhookCall(WEBHOOK_CALL_ITEM)

        self.assertEqual(str(webhook_call), "<WebhookCall[201] id='4KYbXQ9cg8CE2aqouWqY2i' url='https://circleci.com/api/v1/project/...' request_at='2017-06-21T22:44:42.624000+00:00' response_at='2017-06-21T22:44:43.086000+00:00'>")

    def test_webhook_call_no_dates(self):
        webhook_call = WebhookCall(WEBHOOK_CALL_ITEM_NO_DATE)

        self.assertEqual(str(webhook_call), "<WebhookCall[201] id='4KYbXQ9cg8CE2aqouWqY2i' url='https://circleci.com/api/v1/project/...' request_at='N/A' response_at='N/A'>")

    def test_fail_create_webhook_call(self):
        with self.assertRaises(Exception):
            CLIENT.webhook_calls(PLAYGROUND_SPACE, 'foo').create()

    def test_fail_delete_webhook_call(self):
        with self.assertRaises(Exception):
            CLIENT.webhook_calls(PLAYGROUND_SPACE, 'foo').delete('foobar')

    @vcr.use_cassette('fixtures/webhook_call/all.yaml', decode_compressed_response=True)
    def test_webhook_call_all(self):
        webhook_calls = CLIENT.webhook_calls('orzkxlxlq59d', '16ypL3XjNK6oreLPPoVBxI').all({'limit': 1})

        self.assertEqual(len(webhook_calls), 1)
        self.assertEqual(webhook_calls[0].id, '4KYbXQ9cg8CE2aqouWqY2i')

    @vcr.use_cassette('fixtures/webhook_call/find.yaml', decode_compressed_response=True)
    def test_webhook_call_find(self):
        webhook_call = CLIENT.webhook_calls('orzkxlxlq59d', '16ypL3XjNK6oreLPPoVBxI').find('4KYbXQ9cg8CE2aqouWqY2i')

        self.assertEqual(str(webhook_call), "<WebhookCall[201] id='4KYbXQ9cg8CE2aqouWqY2i' url='https://circleci.com/api/v1/project/...' request_at='2017-06-21T22:44:42.624000+00:00' response_at='2017-06-21T22:44:43.086000+00:00'>")
