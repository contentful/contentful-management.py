import vcr
from unittest import TestCase
from contentful_management.content_type_entries_proxy import ContentTypeEntriesProxy
from contentful_management.errors import NotFoundError
from .test_helper import CLIENT, PLAYGROUND_SPACE


class ContentTypesEntriesProxyTest(TestCase):
    def test_content_types_entries_proxy(self):
        proxy = ContentTypeEntriesProxy(CLIENT, PLAYGROUND_SPACE, 'master', 'foo')

        self.assertEqual(str(proxy), "<ContentTypeEntriesProxy space_id='{0}' environment_id='master' content_type_id='foo'>".format(PLAYGROUND_SPACE))

    @vcr.use_cassette('fixtures/entry/all_content_type.yaml', decode_compressed_response=True)
    def test_content_types_entries_proxy_all(self):
        proxy = ContentTypeEntriesProxy(CLIENT, PLAYGROUND_SPACE, 'master', 'foo')

        entries = []

        self.assertFalse(entries)

        entries = proxy.all()

        self.assertTrue(entries)

    @vcr.use_cassette('fixtures/entry/find_content_type.yaml', decode_compressed_response=True)
    def test_content_types_entries_proxy_find(self):
        proxy = ContentTypeEntriesProxy(CLIENT, PLAYGROUND_SPACE, 'master', 'foo')

        entry = proxy.find('4RToqNcBfW6MAK0UGU0qWc')

        self.assertEqual(entry.name, 'foobar')

    @vcr.use_cassette('fixtures/entry/create_content_type.yaml', decode_compressed_response=True)
    def test_content_types_entries_proxy_create(self):
        proxy = ContentTypeEntriesProxy(CLIENT, PLAYGROUND_SPACE, 'master', 'foo')

        entry = proxy.create('id_create_content_type_proxy_test', {
            'fields': {
                'name': {
                    'en-US': 'test'
                }
            }
        })

        self.assertEqual(entry.name, 'test')
        self.assertEqual(entry.id, 'id_create_content_type_proxy_test')

    @vcr.use_cassette('fixtures/entry/delete_content_type.yaml', decode_compressed_response=True)
    def test_content_types_entries_proxy_delete(self):
        proxy = ContentTypeEntriesProxy(CLIENT, PLAYGROUND_SPACE, 'master', 'foo')

        proxy.delete('1zquSqZeokECU2Wike2cQi')

        with vcr.use_cassette('fixtures/entry/not_found_content_type.yaml'):
            with self.assertRaises(NotFoundError):
                proxy.find('1zquSqZeokECU2Wike2cQi')
