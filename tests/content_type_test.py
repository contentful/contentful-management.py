import vcr
from unittest import TestCase
from contentful_management.content_type import ContentType
from contentful_management.errors import NotFoundError
from .test_helper import CLIENT, PLAYGROUND_SPACE

BASE_CT_ITEM = {
    'sys': {
        'id': 'foo',
        'type': 'ContentType',
        'space': {
            'sys': {
                'id': 'foobar',
                'type': 'Link',
                'linkType': 'Space'
            }
        }
    },
    'name': 'Foo',
    'displayField': 'name',
    'description': 'Something goes here...',
    'fields': [
        {
            'id': 'name',
            'name': 'Name',
            'type': 'Symbol'
        }
    ]
}


class ContentTypeTest(TestCase):
    def test_content_type(self):
        content_type = ContentType(BASE_CT_ITEM)

        self.assertEqual(str(content_type), "<ContentType[Foo] id='foo'>")

    def test_content_type_to_json(self):
        content_type = ContentType(BASE_CT_ITEM)

        self.assertEqual(content_type.to_json(), {
            'sys': {
                'id': 'foo',
                'type': 'ContentType',
                'space': {
                    'sys': {
                        'id': 'foobar',
                        'type': 'Link',
                        'linkType': 'Space'
                    }
                }
            },
            'name': 'Foo',
            'displayField': 'name',
            'description': 'Something goes here...',
            'fields': [
                {
                    'id': 'name',
                    'name': 'Name',
                    'type': 'Symbol',
                    'localized': False,
                    'omitted': False,
                    'required': False,
                    'disabled': False,
                    'validations': [],
                }
            ]
        })

    def test_content_type_to_link(self):
        content_type = ContentType(BASE_CT_ITEM)

        self.assertEqual(content_type.to_link().to_json(), {
            'sys': {
                'id': 'foo',
                'type': 'Link',
                'linkType': 'ContentType'
            }
        })

    @vcr.use_cassette('fixtures/content_type/create.yaml', decode_compressed_response=True)
    def test_create_content_type(self):
        content_type = CLIENT.content_types(PLAYGROUND_SPACE, 'master').create(None, {
            'name': 'Create Test',
            'displayField': 'name',
            'description': 'Something goes here...',
            'fields': [
                {
                    'id': 'name',
                    'name': 'Name',
                    'type': 'Symbol'
                }
            ]
        })

        self.assertEqual(content_type.name, 'Create Test')
        self.assertTrue(content_type.id)

    @vcr.use_cassette('fixtures/content_type/id_create.yaml', decode_compressed_response=True)
    def test_create_content_type_with_id(self):
        content_type = CLIENT.content_types(PLAYGROUND_SPACE, 'master').create('id_content_type_create_test', {
            'name': 'ID Create Test',
            'displayField': 'name',
            'description': 'Something goes here...',
            'fields': [
                {
                    'id': 'name',
                    'name': 'Name',
                    'type': 'Symbol'
                }
            ]
        })

        self.assertEqual(content_type.id, 'id_content_type_create_test')
        self.assertEqual(content_type.name, 'ID Create Test')

    @vcr.use_cassette('fixtures/content_type/create_with_resource_link_field.yaml', decode_compressed_response=True)
    def test_create_content_type_with_resource_link_field(self):
        content_type = CLIENT.content_types(PLAYGROUND_SPACE, 'master').create(None, {
            'name': 'Create Test',
            'description': 'Something goes here...',
            'fields': [{
                'id': 'myResourceLink',
                'name': 'My Resource Link',
                'type': 'ResourceLink',
                'localized': True,
                'disabled': False,
                'omitted': False,
                'allowedResources': [
                    {
                        'type': 'Contentful:Entry',
                        'source': 'crn:contentful:::content:spaces/yb41ceqgyiw5',
                        'contentTypes': ["foo", "bar"]
                    }]
                }
            ]
        })

        self.assertEqual(len(content_type.fields), 1)

        field = content_type.fields[0]

        self.assertEqual(field.name, 'My Resource Link')
        self.assertEqual(field.type, 'ResourceLink')
        self.assertEqual(len(field.allowedResources), 1)
        self.assertEqual(field.allowedResources[0]['type'], 'Contentful:Entry')
        self.assertEqual(field.allowedResources[0]['source'], 'crn:contentful:::content:spaces/yb41ceqgyiw5')
        self.assertEqual(field.allowedResources[0]['contentTypes'], ['foo', 'bar'])

    @vcr.use_cassette('fixtures/content_type/create_no_fields.yaml', decode_compressed_response=True)
    def test_create_content_type_no_fields(self):
        content_type = CLIENT.content_types(PLAYGROUND_SPACE, 'master').create(None, {
            'name': 'Create Test No Fields',
            'description': 'Something goes here...'
        })

        self.assertTrue(content_type.id)
        self.assertEqual(content_type.fields, [])

    @vcr.use_cassette('fixtures/content_type/find.yaml', decode_compressed_response=True)
    def test_update_content_type(self):
        content_type = CLIENT.content_types(PLAYGROUND_SPACE, 'master').find('foo')

        self.assertEqual(content_type.name, 'something else')

        with vcr.use_cassette('fixtures/content_type/update.yaml', decode_compressed_response=True):
            content_type.name = 'foo'
            content_type.save()

        self.assertEqual(content_type.name, 'foo')

    @vcr.use_cassette('fixtures/content_type/update_default_value.yaml', decode_compressed_response=True)
    def test_preserves_field_default_value_on_update(self):
        content_type = CLIENT.content_types(PLAYGROUND_SPACE, 'master').find('test123')

        assert content_type.fields[0].default_value is not None
        content_type.save()
        assert content_type.fields[0].default_value is not None

    @vcr.use_cassette('fixtures/content_type/find_2.yaml', decode_compressed_response=True)
    def test_delete_content_type(self):
        content_type = CLIENT.content_types(PLAYGROUND_SPACE, 'master').find('45JdPK7wbCQwecKOAyqcw0')

        with vcr.use_cassette('fixtures/content_type/delete.yaml', decode_compressed_response=True):
            content_type.delete()

        with vcr.use_cassette('fixtures/content_type/not_found.yaml', decode_compressed_response=True):
            with self.assertRaises(NotFoundError):
                CLIENT.content_types(PLAYGROUND_SPACE, 'master').find('45JdPK7wbCQwecKOAyqcw0')

    @vcr.use_cassette('fixtures/content_type/find_3.yaml', decode_compressed_response=True)
    def test_publish_content_type(self):
        content_type = CLIENT.content_types(PLAYGROUND_SPACE, 'master').find('1JzBeA5EcEcyKUaqGeqImy')

        published_counter = getattr(content_type, 'published_counter', 0)

        with vcr.use_cassette('fixtures/content_type/publish.yaml', decode_compressed_response=True):
            content_type.publish()

        self.assertEqual(content_type.published_counter, published_counter + 1)
        self.assertTrue(content_type.is_published)

    @vcr.use_cassette('fixtures/content_type/find_4.yaml', decode_compressed_response=True)
    def test_unpublish_content_type(self):
        content_type = CLIENT.content_types(PLAYGROUND_SPACE, 'master').find('1JzBeA5EcEcyKUaqGeqImy')

        with vcr.use_cassette('fixtures/content_type/unpublish.yaml', decode_compressed_response=True):
            content_type.unpublish()

        self.assertFalse(content_type.is_published)

    @vcr.use_cassette('fixtures/content_type/find.yaml', decode_compressed_response=True)
    def test_content_type_entries(self):
        content_type = CLIENT.content_types(PLAYGROUND_SPACE, 'master').find('foo')

        proxy = content_type.entries()

        self.assertEqual(str(proxy), "<ContentTypeEntriesProxy space_id='{0}' environment_id='master' content_type_id='foo'>".format(PLAYGROUND_SPACE))

    @vcr.use_cassette('fixtures/content_type/find.yaml', decode_compressed_response=True)
    def test_content_type_snapshots(self):
        content_type = CLIENT.content_types(PLAYGROUND_SPACE, 'master').find('foo')

        proxy = content_type.snapshots()

        self.assertEqual(str(proxy), "<ContentTypeSnapshotsProxy space_id='{0}' environment_id='master' content_type_id='foo'>".format(PLAYGROUND_SPACE))

    @vcr.use_cassette('fixtures/content_type/find.yaml', decode_compressed_response=True)
    def test_content_type_editor_interfaces(self):
        content_type = CLIENT.content_types(PLAYGROUND_SPACE, 'master').find('foo')

        proxy = content_type.editor_interfaces()

        self.assertEqual(str(proxy), "<ContentTypeEditorInterfacesProxy space_id='{0}' environment_id='master' content_type_id='foo'>".format(PLAYGROUND_SPACE))

    # Integration Tests
    @vcr.use_cassette('fixtures/content_type/issue_17.yaml', decode_compressed_response=True)
    def test_content_type_not_properly_updating(self):
        content_type = CLIENT.content_types(PLAYGROUND_SPACE, 'master').find('cat')

        self.assertEqual(content_type.name, 'Cat')

        content_type.name = 'Foo Cat'
        content_type.save()

        content_type = CLIENT.content_types(PLAYGROUND_SPACE, 'master').find('cat')

        self.assertEqual(content_type.name, 'Foo Cat')
