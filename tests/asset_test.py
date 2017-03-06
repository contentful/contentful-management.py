import vcr
from unittest import TestCase
from contentful_management.asset import Asset
from contentful_management.errors import NotFoundError
from .test_helper import CLIENT, PLAYGROUND_SPACE

BASE_ASSET_ITEM = {
    'sys': {
        'id': 'foo',
        'type': 'Asset',
        'space': {
            'sys': {
                'id': 'foobar',
                'type': 'Link',
                'linkType': 'Space'
            }
        }
    },
    'fields': {
        'file': {
            'en-US': {
                'fileName': 'foo.png',
                'contentType': 'image/png',
                'url': '//images.contentful.com/.../foo.png'
            }
        }
    }
}

class AssetTest(TestCase):
    def test_asset(self):
        asset = Asset(BASE_ASSET_ITEM)

        self.assertEqual(str(asset), "<Asset id='foo' url='//images.contentful.com/.../foo.png'>")

    def test_asset_to_json(self):
        asset = Asset(BASE_ASSET_ITEM)

        self.assertEqual(asset.to_json(), {
            'sys': {
                'id': 'foo',
                'type': 'Asset',
                'space': {
                    'sys': {
                        'id': 'foobar',
                        'type': 'Link',
                        'linkType': 'Space'
                    }
                }
            },
            'fields': {
                'file': {
                    'en-US': {
                        'fileName': 'foo.png',
                        'contentType': 'image/png',
                        'url': '//images.contentful.com/.../foo.png'
                    }
                }
            }
        })

    def test_asset_to_link(self):
        asset = Asset(BASE_ASSET_ITEM)

        self.assertEqual(asset.to_link().to_json(), {
            'sys': {
                'id': 'foo',
                'type': 'Link',
                'linkType': 'Asset'
            }
        })

    def test_asset_url_with_parameters(self):
        asset = Asset(BASE_ASSET_ITEM)

        self.assertEqual(asset.url(w=123), '//images.contentful.com/.../foo.png?w=123')

        url = asset.url(w=123, h=123)
        self.assertTrue('w=123' in url)
        self.assertTrue('h=123' in url)
        self.assertTrue('&' in url)
        self.assertTrue('?' in url)

    @vcr.use_cassette('fixtures/asset/create.yaml')
    def test_create_asset_with_url(self):
        asset = CLIENT.assets(PLAYGROUND_SPACE).create(None, {
            'fields': {
                'file': {
                    'en-US': {
                        'fileName': 'foo.png',
                        'contentType': 'image/png',
                        'upload': 'https://i.imgur.com/Zmum6k4.png'
                    }
                }
            }
        })

        self.assertEqual(asset.file['fileName'], 'foo.png')
        self.assertTrue(asset.id)

    @vcr.use_cassette('fixtures/asset/create_empty.yaml')
    def test_create_asset_with_no_attributes(self):
        asset = CLIENT.assets(PLAYGROUND_SPACE).create()

        self.assertTrue(asset.id)


    @vcr.use_cassette('fixtures/asset/upload_create.yaml')
    def test_create_asset_with_upload(self):
        upload = CLIENT.uploads(PLAYGROUND_SPACE).create('README.rst')

        asset = CLIENT.assets(PLAYGROUND_SPACE).create(None, {
            'fields': {
                'file': {
                    'en-US': {
                        'fileName': 'Asset Tests',
                        'contentType': 'application/x-python',
                        'uploadFrom': upload.to_link().to_json()
                    }
                }
            }
        })

        self.assertTrue(asset.id)
        self.assertTrue(asset.file)

    @vcr.use_cassette('fixtures/asset/id_create.yaml')
    def test_create_asset_with_id(self):
        asset = CLIENT.assets(PLAYGROUND_SPACE).create('id_asset_create_test', {
            'fields': {
                'file': {
                    'en-US': {
                        'fileName': 'foo.png',
                        'contentType': 'image/png',
                        'upload': 'https://i.imgur.com/Zmum6k4.png'
                    }
                }
            }
        })

        self.assertEqual(asset.id, 'id_asset_create_test')

    @vcr.use_cassette('fixtures/asset/find.yaml')
    def test_process_asset(self):
        asset = CLIENT.assets(PLAYGROUND_SPACE).find('file6')

        self.assertFalse(asset.url())

        with vcr.use_cassette('fixtures/asset/process.yaml'):
            asset.process()

        self.assertTrue(asset.url())

    @vcr.use_cassette('fixtures/asset/find_2.yaml')
    def test_update_asset(self):
        asset = CLIENT.assets(PLAYGROUND_SPACE).find('file3')

        with vcr.use_cassette('fixtures/asset/update.yaml'):
            asset.file['fileName'] = 'demo app image'
            asset.save()

        self.assertEqual(asset.file['fileName'], 'demo app image')

    @vcr.use_cassette('fixtures/asset/find_3.yaml')
    def test_delete_asset(self):
        asset = CLIENT.assets(PLAYGROUND_SPACE).find('file6')

        with vcr.use_cassette('fixtures/asset/delete.yaml'):
            asset.delete()

        with vcr.use_cassette('fixtures/asset/not_found.yaml'):
            with self.assertRaises(NotFoundError):
                CLIENT.assets(PLAYGROUND_SPACE).find('file6')

    @vcr.use_cassette('fixtures/asset/find_4.yaml')
    def test_publish_asset(self):
        asset = CLIENT.assets(PLAYGROUND_SPACE).find('file3')

        published_counter = getattr(asset, 'published_counter', 0)

        with vcr.use_cassette('fixtures/asset/publish.yaml'):
            asset.publish()

        self.assertEqual(asset.published_counter, published_counter + 1)
        self.assertTrue(asset.is_published)

    @vcr.use_cassette('fixtures/asset/find_5.yaml')
    def test_unpublish_asset(self):
        asset = CLIENT.assets(PLAYGROUND_SPACE).find('file3')

        with vcr.use_cassette('fixtures/asset/unpublish.yaml'):
            asset.unpublish()

        self.assertFalse(asset.is_published)

    @vcr.use_cassette('fixtures/asset/find_6.yaml')
    def test_archive_asset(self):
        asset = CLIENT.assets(PLAYGROUND_SPACE).find('file3')

        archived_version = getattr(asset, 'archived_version', asset.version)

        self.assertFalse(asset.is_archived)

        with vcr.use_cassette('fixtures/asset/archive.yaml'):
            asset.archive()

        self.assertEqual(asset.archived_version, archived_version)
        self.assertTrue(asset.is_archived)

    @vcr.use_cassette('fixtures/asset/find_7.yaml')
    def test_unarchive_asset(self):
        asset = CLIENT.assets(PLAYGROUND_SPACE).find('file3')

        self.assertTrue(asset.is_archived)

        with vcr.use_cassette('fixtures/asset/unarchive.yaml'):
            asset.unarchive()

        self.assertFalse(getattr(asset, 'archived_version', False))
        self.assertFalse(asset.is_archived)
