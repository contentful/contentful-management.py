import vcr
from unittest import TestCase
from contentful_management.entries_proxy import EntriesProxy
from .test_helper import CLIENT, PLAYGROUND_SPACE


class EntriesProxyTest(TestCase):
    @vcr.use_cassette('fixtures/entry/create_with_ct_empty.yaml', decode_compressed_response=True)
    def test_entries_proxy_create_with_content_type_and_empty_attributes(self):
        proxy = EntriesProxy(CLIENT, PLAYGROUND_SPACE, 'master', 'foo')

        entry = proxy.create('id_create_content_type_empty')

        self.assertTrue(entry.id)
