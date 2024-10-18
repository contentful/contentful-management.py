import vcr
from unittest import TestCase
from contentful_management.resource import Link
from contentful_management.api_key import ApiKey
from contentful_management.errors import NotFoundError
from .test_helper import CLIENT, PLAYGROUND_SPACE

API_KEY_ITEM = {
    'name': 'foo',
    'description': 'bar',
    'accessToken': '123abc',
    'environments': [
        {
            'sys': {
                'type': 'Link',
                'linkType': 'Environment',
                'id': 'master'
            }
        }
    ],
    'sys': {
        'id': 'foo',
        'type': 'ApiKey',
        'space': {
            'sys': {
                'id': 'foobar',
                'type': 'Link',
                'linkType': 'Space'
            }
        }
    }
}


class ApiKeyTest(TestCase):
    def test_api_key(self):
        api_key = ApiKey(API_KEY_ITEM)

        self.assertEqual(str(api_key), "<ApiKey[foo] id='foo' access_token='123abc'>")

    def test_api_key_to_json(self):
        api_key = ApiKey(API_KEY_ITEM)

        self.assertEqual(api_key.to_json(), {
            'name': 'foo',
            'description': 'bar',
            'accessToken': '123abc',
            'environments': [
                {
                    'sys': {
                        'type': 'Link',
                        'linkType': 'Environment',
                        'id': 'master'
                    }
                }
            ],
            'sys': {
                'id': 'foo',
                'type': 'ApiKey',
                'space': {
                    'sys': {
                        'id': 'foobar',
                        'type': 'Link',
                        'linkType': 'Space'
                    }
                }
            }
        })

    def test_api_key_to_link(self):
        api_key = ApiKey(API_KEY_ITEM)

        self.assertEqual(api_key.to_link().to_json(), {
            'sys': {
                'id': 'foo',
                'type': 'Link',
                'linkType': 'ApiKey'
            }
        })

    @vcr.use_cassette('fixtures/api_key/create.yaml', decode_compressed_response=True)
    def test_create_api_key(self):
        api_key = CLIENT.api_keys(PLAYGROUND_SPACE).create({
            'name': 'Test Key',
            'description': 'Something goes here...'
        })

        self.assertEqual(api_key.name, 'Test Key')
        self.assertEqual(api_key.description, 'Something goes here...')
        self.assertTrue(api_key.access_token)

    @vcr.use_cassette('fixtures/api_key/create_with_environment.yaml', decode_compressed_response=True)
    def test_create_api_key(self):
        api_key = CLIENT.api_keys(PLAYGROUND_SPACE).create({
            'name': 'Test Key with environments',
            'description': 'Something goes here...',
            'environments': [
                {
                    'sys': {
                        'type': 'Link',
                        'linkType': 'Environment',
                        'id': 'master'
                    }
                },
                {
                    'sys': {
                        'type': 'Link',
                        'linkType': 'Environment',
                        'id': 'testing'
                    }
                }
            ]
        })

        self.assertEqual(len(api_key.environments), 2)
        self.assertEqual(api_key.environments[0].id, 'master')
        self.assertEqual(api_key.environments[1].id, 'testing')

    @vcr.use_cassette('fixtures/api_key/find.yaml', decode_compressed_response=True)
    def test_update_api_key(self):
        api_key = CLIENT.api_keys(PLAYGROUND_SPACE).find('42sVZNadpFAje7EFwHOfVY')

        with vcr.use_cassette('fixtures/api_key/update.yaml'):
            api_key.name = 'Not Test Key'
            api_key.save()

        self.assertEqual(api_key.name, 'Not Test Key')

    @vcr.use_cassette('fixtures/api_key/find_2.yaml', decode_compressed_response=True)
    def test_delete_api_key(self):
        api_key = CLIENT.api_keys(PLAYGROUND_SPACE).find('42sVZNadpFAje7EFwHOfVY')

        with vcr.use_cassette('fixtures/api_key/delete.yaml'):
            api_key.delete()

        with vcr.use_cassette('fixtures/api_key/not_found.yaml'):
            with self.assertRaises(NotFoundError):
                CLIENT.api_keys(PLAYGROUND_SPACE).find('42sVZNadpFAje7EFwHOfVY')

    @vcr.use_cassette('fixtures/api_key/find_3.yaml', decode_compressed_response=True)
    def test_get_preview_api_key_from_key(self):
        api_key = CLIENT.api_keys(PLAYGROUND_SPACE).find('5mxNhKOZYOp1wzafOR9qPw')

        with vcr.use_cassette('fixtures/api_key/find_preview.yaml'):
            preview_api_key = api_key.preview_api_key()
            self.assertEqual(str(preview_api_key), "<PreviewApiKey[management.py - playground 1] id='5mytqWZjcqEWMIHVfe5cUi' access_token='PREVIEW_TOKEN'>")

    @vcr.use_cassette('fixtures/api_key/find_3.yaml', decode_compressed_response=True)
    def test_update_api_key_with_new_environment(self):
        api_key = CLIENT.api_keys(PLAYGROUND_SPACE).find('5mxNhKOZYOp1wzafOR9qPw')

        with vcr.use_cassette('fixtures/api_key/update_key.yaml'):
            self.assertEqual(len(api_key.environments), 1)
            self.assertEqual(api_key.environments[0].id, 'testing')

            api_key.environments.append(
                Link({
                    'sys': {
                        'id': 'master',
                        'type': 'Link',
                        'linkType': 'Environment'
                    }
                })
            )

            api_key.save()

            self.assertEqual(len(api_key.environments), 2)
