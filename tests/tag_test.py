import vcr
from unittest import TestCase
from contentful_management.errors import NotFoundError
from contentful_management.tag import Tag
from .test_helper import CLIENT, PLAYGROUND_SPACE

TAG_ITEM = {
    "name": "NY Campaign",
    "sys": {
        "visibility": "public",
        "id": "nyCampaign",
        "type": "Tag"
    }
}


class TagTest(TestCase):
    def test_tag(self):
        tag = Tag(TAG_ITEM)

        self.assertEqual(str(tag), "<Tag id='nyCampaign' name='NY Campaign'>")

    @vcr.use_cassette('fixtures/tags/all.yaml', decode_compressed_response=True)
    def test_tags_all(self):
        tags = CLIENT.tags(PLAYGROUND_SPACE, 'master').all()

        self.assertEqual(len(tags), 10)
        self.assertEqual(tags[0].id, 'fooPrivate')

    @vcr.use_cassette('fixtures/tags/create_public.yaml', decode_compressed_response=True)
    def test_create_public_tag(self):
        tag = CLIENT.tags(PLAYGROUND_SPACE, 'master').create('fooPublic',
                                                             {'name': 'Foo Public', 'sys': {'visibility': 'public'}})

        self.assertEqual(tag.id, 'fooPublic')
        self.assertEqual(tag.name, 'Foo Public')
        self.assertEqual(tag.sys['visibility'], 'public')

    @vcr.use_cassette('fixtures/tags/create_private.yaml', decode_compressed_response=True)
    def test_create_private_tag(self):
        tag = CLIENT.tags(PLAYGROUND_SPACE, 'master').create('fooPrivate', {'name': 'Foo Private'})

        self.assertEqual(tag.id, 'fooPrivate')
        self.assertEqual(tag.name, 'Foo Private')
        self.assertEqual(tag.sys['visibility'], 'private')

    @vcr.use_cassette('fixtures/tags/find.yaml', decode_compressed_response=True)
    def test_find_tag(self):
        tag = CLIENT.tags(PLAYGROUND_SPACE, 'master').find('fooPrivate')

        self.assertEqual(tag.id, 'fooPrivate')
        self.assertEqual(tag.name, 'Foo Private')
        self.assertEqual(tag.sys['visibility'], 'private')

    @vcr.use_cassette('fixtures/tags/update.yaml', decode_compressed_response=True)
    def test_update_tag(self):
        tag = CLIENT.tags(PLAYGROUND_SPACE, 'master').find('fooPublic')

        tag.update({'name': 'Public Tag Name'})

        tag = CLIENT.tags(PLAYGROUND_SPACE, 'master').find('fooPublic')
        self.assertEqual(tag.name, 'Public Tag Name')

    @vcr.use_cassette('fixtures/tags/delete.yaml', decode_compressed_response=True)
    def test_delete_tag(self):
        tag = CLIENT.tags(PLAYGROUND_SPACE, 'master').find('fooPublic')

        tag.delete()

        with self.assertRaises(NotFoundError):
            CLIENT.tags(PLAYGROUND_SPACE, 'master').find('fooPublic')

    @vcr.use_cassette('fixtures/tags/add_tag_to_an_entry.yaml', decode_compressed_response=True)
    def test_add_tag_to_entry_update(self):
        entry = CLIENT.entries(PLAYGROUND_SPACE, 'master').find('4mnyzaAjCSA65Xz6jEO5yB')
        self.assertEqual(len(entry._metadata['tags']), 0)

        entry.update({"_metadata": {"tags": [{"sys": {"type": "Link", "linkType": "Tag", "id": "icon"}}]}})

        entry = CLIENT.entries(PLAYGROUND_SPACE, 'master').find('4mnyzaAjCSA65Xz6jEO5yB')
        self.assertEqual(len(entry._metadata['tags']), 1)

    @vcr.use_cassette('fixtures/tags/create_entry_with_tag.yaml', decode_compressed_response=True)
    def test_add_tag_to_entry_create(self):
        entry = CLIENT.entries(PLAYGROUND_SPACE, 'master').create(None, {
            'content_type_id': 'author',
            'fields': {
                'name': {
                    'en-US': 'Lata Mangeshkar'
                }
            },
            '_metadata': {"tags": [{"sys": {"type": "Link", "linkType": "Tag", "id": "icon"}}]}
        })

        self.assertEqual(len(entry._metadata['tags']), 1)

    @vcr.use_cassette('fixtures/tags/add_tag_to_asset.yaml', decode_compressed_response=True)
    def test_add_tag_to_asset_update(self):
        asset = CLIENT.assets(PLAYGROUND_SPACE, 'master').find('6vK2vO3YPUSSK6euosLyGf')
        self.assertEqual(0, len(asset._metadata['tags']))

        asset.update({"_metadata": {"tags": [{"sys": {"type": "Link", "linkType": "Tag", "id": "icon"}}]}})

        asset = CLIENT.assets(PLAYGROUND_SPACE, 'master').find('686aLBcjj1f47uFWxrepj6')
        self.assertEqual(1, len(asset._metadata['tags']))

    @vcr.use_cassette('fixtures/tags/create_asset_with_tag.yaml', decode_compressed_response=True)
    def test_add_tag_to_asset_create(self):
        asset = CLIENT.assets(PLAYGROUND_SPACE, 'master').create(None, {
            'fields': {
                'file': {
                    'en-US': {
                        'fileName': 'foo.png',
                        'contentType': 'image/png',
                        'upload': 'https://i.imgur.com/Zmum6k4.png'
                    }
                }
            },
            '_metadata': {"tags": [{"sys": {"type": "Link", "linkType": "Tag", "id": "icon"}}]}
        })

        self.assertEqual(len(asset._metadata['tags']), 1)

    def test_tag_to_json(self):
        tag = Tag(TAG_ITEM)

        self.assertEqual(tag.to_json(), {
            'name': 'NY Campaign',
            'sys': {
                'visibility': 'public',
                'id': 'nyCampaign',
                'type': 'Tag'
            }
        })
