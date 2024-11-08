import vcr
from time import sleep
from unittest import TestCase
from contentful_management.environment import Environment
from contentful_management.errors import NotFoundError
from .test_helper import CLIENT, PLAYGROUND_SPACE

BASE_ENVIRONMENT_ITEM = {
    'sys': {
        'id': 'foo',
        'type': 'Environment',
        'space': {
            'sys': {
                'id': 'foobar',
                'type': 'Link',
                'linkType': 'Space'
            }
        }
    },
    'name': 'foo'
}


class EnvironmentTest(TestCase):
    def test_entry(self):
        entry = Environment(BASE_ENVIRONMENT_ITEM)

        self.assertEqual(str(entry), "<Environment[foo] id='foo'>")

    def test_entry_to_json(self):
        entry = Environment(BASE_ENVIRONMENT_ITEM)

        self.assertEqual(entry.to_json(), BASE_ENVIRONMENT_ITEM)

    def test_entry_to_link(self):
        entry = Environment(BASE_ENVIRONMENT_ITEM)

        self.assertEqual(entry.to_link().to_json(), {
            'sys': {
                'id': 'foo',
                'type': 'Link',
                'linkType': 'Environment'
            }
        })

    @vcr.use_cassette('fixtures/environment/all.yaml', decode_compressed_response=True)
    def test_environments(self):
        environments = CLIENT.environments(PLAYGROUND_SPACE).all()

        self.assertEqual(str(environments[0]), "<Environment[master] id='master'>")

    @vcr.use_cassette('fixtures/environment/no_id_create.yaml', decode_compressed_response=True)
    def test_create_environment_without_id_raises_404(self):
        with self.assertRaises(NotFoundError):
            CLIENT.environments(PLAYGROUND_SPACE).create(None, {
                'name': 'SDK Tests - No ID'
            })

    @vcr.use_cassette('fixtures/environment/create.yaml', decode_compressed_response=True)
    def test_create_environment_with_id(self):
        environment = CLIENT.environments(PLAYGROUND_SPACE).create('sdk_tests', {
            'name': 'SDK Tests'
        })

        self.assertEqual(environment.name, 'SDK Tests')
        self.assertEqual(environment.id, 'sdk_tests')

    @vcr.use_cassette('fixtures/environment/create_different_source.yaml', decode_compressed_response=True)
    def test_create_environment_with_different_source(self):
        master = CLIENT.environments(PLAYGROUND_SPACE).find('master')

        self.assertNotEqual(len(master.entries().all()), 0)

        non_master_source = CLIENT.environments(PLAYGROUND_SPACE).create('non-master-py', {
            'name': 'Non Master - Python',
            'source_environment_id': 'source'
        })
        sleep(5) # Need to sleep to ensure environment is ready
        non_master_source.reload()

        self.assertEqual(len(non_master_source.entries().all()), 0)

    @vcr.use_cassette('fixtures/environment/find.yaml', decode_compressed_response=True)
    def test_update_environment(self):
        environment = CLIENT.environments(PLAYGROUND_SPACE).find('sdk_tests')

        self.assertEqual(environment.name, 'SDK Tests')

        with vcr.use_cassette('fixtures/environment/update.yaml'):
            environment.name = 'something else'
            environment.save()

        self.assertEqual(environment.name, 'something else')

    @vcr.use_cassette('fixtures/environment/find.yaml', decode_compressed_response=True)
    def test_delete_environment(self):
        environment = CLIENT.environments(PLAYGROUND_SPACE).find('sdk_tests')

        with vcr.use_cassette('fixtures/environment/delete.yaml'):
            environment.delete()

        with vcr.use_cassette('fixtures/environment/not_found.yaml'):
            with self.assertRaises(NotFoundError):
                CLIENT.environments(PLAYGROUND_SPACE).find('sdk_tests')

    @vcr.use_cassette('fixtures/environment/delete.yaml', decode_compressed_response=True)
    def test_delete_environment_directly_from_client_proxy(self):
        CLIENT.environments(PLAYGROUND_SPACE).delete('sdk_tests')

    @vcr.use_cassette('fixtures/environment/find_2.yaml', decode_compressed_response=True)
    def test_fetch_entries_from_an_environment(self):
        environment = CLIENT.environments(PLAYGROUND_SPACE).find('testing')

        with vcr.use_cassette('fixtures/environment/all_entries.yaml'):
            entries = environment.entries().all()
            self.assertEqual(str(entries[0]), "<Entry[cat] id='IJLRrADsqq2AmwcugoYeK'>")

    @vcr.use_cassette('fixtures/environment/find_2.yaml', decode_compressed_response=True)
    def test_environment_proxies(self):
        environment = CLIENT.environments(PLAYGROUND_SPACE).find('testing')

        self.assertEqual(str(environment.entries()), "<EnvironmentEntriesProxy space_id='facgnwwgj5fe' environment_id='testing'>")
        self.assertEqual(str(environment.assets()), "<EnvironmentAssetsProxy space_id='facgnwwgj5fe' environment_id='testing'>")
        self.assertEqual(str(environment.content_types()), "<EnvironmentContentTypesProxy space_id='facgnwwgj5fe' environment_id='testing'>")
        self.assertEqual(str(environment.locales()), "<EnvironmentLocalesProxy space_id='facgnwwgj5fe' environment_id='testing'>")
        self.assertEqual(str(environment.ui_extensions()), "<EnvironmentUIExtensionsProxy space_id='facgnwwgj5fe' environment_id='testing'>")
