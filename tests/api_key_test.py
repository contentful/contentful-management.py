import vcr
from unittest import TestCase
from contentful_management.api_key import ApiKey
from contentful_management.errors import NotFoundError
from .test_helper import CLIENT, PLAYGROUND_SPACE

API_KEY_ITEM = {
    'name': 'foo',
    'description': 'bar',
    'accessToken': '123abc',
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

        self.assertEqual(str(api_key), "<ApiKey[foo] id='foo'>")

    def test_api_key_to_json(self):
        api_key = ApiKey(API_KEY_ITEM)

        self.assertEqual(api_key.to_json(), {
            'name': 'foo',
            'description': 'bar',
            'accessToken': '123abc',
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

    @vcr.use_cassette('fixtures/api_key/create.yaml')
    def test_create_api_key(self):
        api_key = CLIENT.api_keys(PLAYGROUND_SPACE).create({
            'name': 'Test Key',
            'description': 'Something goes here...'
        })

        self.assertEqual(api_key.name, 'Test Key')
        self.assertEqual(api_key.description, 'Something goes here...')
        self.assertTrue(api_key.access_token)

    @vcr.use_cassette('fixtures/api_key/find.yaml')
    def test_update_api_key(self):
        api_key = CLIENT.api_keys(PLAYGROUND_SPACE).find('42sVZNadpFAje7EFwHOfVY')

        with vcr.use_cassette('fixtures/api_key/update.yaml'):
            api_key.name = 'Not Test Key'
            api_key.save()

        self.assertEqual(api_key.name, 'Not Test Key')

    @vcr.use_cassette('fixtures/api_key/find_2.yaml')
    def test_delete_api_key(self):
        api_key = CLIENT.api_keys(PLAYGROUND_SPACE).find('42sVZNadpFAje7EFwHOfVY')

        with vcr.use_cassette('fixtures/api_key/delete.yaml'):
            api_key.delete()

        with vcr.use_cassette('fixtures/api_key/not_found.yaml'):
            with self.assertRaises(NotFoundError):
                CLIENT.api_keys(PLAYGROUND_SPACE).find('42sVZNadpFAje7EFwHOfVY')
