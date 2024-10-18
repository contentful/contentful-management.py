import vcr
from unittest import TestCase
from contentful_management.upload import Upload
from contentful_management.errors import NotFoundError
from .test_helper import CLIENT, PLAYGROUND_SPACE

BASE_UPLOAD_ITEM = {
    "sys": {
        "type": "Upload",
        "id": "foo",
        "space": {
            "sys": {
                "type": "Link",
                "linkType": "Space",
                "id": "yadj1kx9rmg0"
            }
        }
    }
}


class UploadTest(TestCase):
    def test_upload(self):
        upload = Upload(BASE_UPLOAD_ITEM)

        self.assertEqual(str(upload), "<Upload id='foo'>")

    def test_upload_to_json(self):
        upload = Upload(BASE_UPLOAD_ITEM)

        self.assertEqual(upload.to_json(), {
            "sys": {
                "type": "Upload",
                "id": "foo",
                "space": {
                    "sys": {
                        "type": "Link",
                        "linkType": "Space",
                        "id": "yadj1kx9rmg0"
                    }
                }
            }
        })

    def test_upload_to_link(self):
        upload = Upload(BASE_UPLOAD_ITEM)

        self.assertEqual(upload.to_link().to_json(), {
            'sys': {
                'id': 'foo',
                'type': 'Link',
                'linkType': 'Upload'
            }
        })

    def test_create_fail(self):
        with self.assertRaises(Exception):
            CLIENT.uploads(PLAYGROUND_SPACE).create(12345)

    @vcr.use_cassette('fixtures/upload/create.yaml', decode_compressed_response=True)
    def test_create_upload_from_path(self):
        upload = CLIENT.uploads(PLAYGROUND_SPACE).create('README.rst')

        self.assertTrue(upload.id)

    @vcr.use_cassette('fixtures/upload/create_from_file.yaml', decode_compressed_response=True)
    def test_create_upload_from_file(self):
        upload = None

        with open('README.rst', 'rb') as f:
            upload = CLIENT.uploads(PLAYGROUND_SPACE).create(f)

        self.assertTrue(upload.id)

    @vcr.use_cassette('fixtures/upload/find.yaml', decode_compressed_response=True)
    def test_find_upload(self):
        upload = CLIENT.uploads(PLAYGROUND_SPACE).find('3pF6ACckKKcB3P60zeszce')

        self.assertEqual(upload.id, '3pF6ACckKKcB3P60zeszce')

    @vcr.use_cassette('fixtures/upload/delete.yaml', decode_compressed_response=True)
    def test_delete_upload(self):
        upload = CLIENT.uploads(PLAYGROUND_SPACE).create('README.rst')
        CLIENT.uploads(PLAYGROUND_SPACE).delete(upload.id)

        with self.assertRaises(NotFoundError):
            CLIENT.uploads(PLAYGROUND_SPACE).find(upload.id)
