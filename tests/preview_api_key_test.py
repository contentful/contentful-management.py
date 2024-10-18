import vcr
from unittest import TestCase
from contentful_management.preview_api_key import PreviewApiKey
from .test_helper import CLIENT, PLAYGROUND_SPACE

PREVIEW_API_KEY_ITEM = {
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


class PreviewApiKeyTest(TestCase):
    def test_preview_api_key(self):
        api_key = PreviewApiKey(PREVIEW_API_KEY_ITEM)

        self.assertEqual(str(api_key), "<PreviewApiKey[foo] id='foo' access_token='123abc'>")

    @vcr.use_cassette('fixtures/preview_api_key/all.yaml', decode_compressed_response=True)
    def test_preview_api_key_all(self):
        preview_keys = CLIENT.preview_api_keys(PLAYGROUND_SPACE).all()
        self.assertEqual(str(preview_keys[0]), "<PreviewApiKey[Example Key] id='22j3CYO1195Bl2QvuXWFMO' access_token='PREVIEW_TOKEN'>")
