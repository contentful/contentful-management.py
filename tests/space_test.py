import vcr
from unittest import TestCase
from contentful_management.space import Space
from contentful_management.errors import NotFoundError
from .test_helper import CLIENT, PLAYGROUND_SPACE, PLAYGROUND_ORG

BASE_SPACE_ITEM = {
    'sys': {
        'id': 'foo',
        'type': 'Space',
    },
    'name': 'Some Space'
}

class SpaceTest(TestCase):
    def test_space(self):
        space = Space(BASE_SPACE_ITEM)

        self.assertEqual(str(space), "<Space[Some Space] id='foo'>")

    def test_space_to_json(self):
        space = Space(BASE_SPACE_ITEM)

        self.assertEqual(space.to_json(), {
            'sys': {
                'id': 'foo',
                'type': 'Space',
            },
            'name': 'Some Space'
        })

    def test_space_to_link(self):
        space = Space(BASE_SPACE_ITEM)

        self.assertEqual(space.to_link().to_json(), {
            'sys': {
                'id': 'foo',
                'type': 'Link',
                'linkType': 'Space'
            }
        })

    @vcr.use_cassette('fixtures/space/create.yaml')
    def test_create_space(self):
        with self.assertRaises(NotFoundError):
            CLIENT.spaces().create({
                'name': 'Create Test',
                'defaultLocale': 'en-US'
            })

        space = CLIENT.spaces().create({
            'name': 'Create Test',
            'defaultLocale': 'en-US',
            'organization_id': PLAYGROUND_ORG
        })

        self.assertEqual(space.name, 'Create Test')
        self.assertTrue(space.id)

    @vcr.use_cassette('fixtures/space/find.yaml')
    def test_update_space(self):
        space = CLIENT.spaces().find('6sun6p8v2zr6')

        self.assertEqual(space.name, 'Create Test')

        with vcr.use_cassette('fixtures/space/update.yaml'):
            space.name = 'Update Test'
            space.save()

        self.assertEqual(space.name, 'Update Test')

    @vcr.use_cassette('fixtures/space/find_2.yaml')
    def test_delete_space(self):
        space = CLIENT.spaces().find('6sun6p8v2zr6')

        with vcr.use_cassette('fixtures/space/delete.yaml'):
            space.delete()

        with vcr.use_cassette('fixtures/space/not_found.yaml'):
            with self.assertRaises(NotFoundError):
                CLIENT.spaces().find('6sun6p8v2zr6')

    @vcr.use_cassette('fixtures/space/reload.yaml')
    def test_reload_space(self):
        space = CLIENT.spaces().find(PLAYGROUND_SPACE)

        space.name = 'foo'

        space.reload()

        self.assertEqual(space.name, 'management.py - playground')

    @vcr.use_cassette('fixtures/space/find_3.yaml')
    def test_space_api_keys(self):
        space = CLIENT.spaces().find(PLAYGROUND_SPACE)

        proxy = space.api_keys()

        self.assertEqual(str(proxy), "<SpaceApiKeysProxy space_id='{0}'>".format(PLAYGROUND_SPACE))

    @vcr.use_cassette('fixtures/space/find_3.yaml')
    def test_space_roles(self):
        space = CLIENT.spaces().find(PLAYGROUND_SPACE)

        proxy = space.roles()

        self.assertEqual(str(proxy), "<SpaceRolesProxy space_id='{0}'>".format(PLAYGROUND_SPACE))

    @vcr.use_cassette('fixtures/space/find_3.yaml')
    def test_space_uploads(self):
        space = CLIENT.spaces().find(PLAYGROUND_SPACE)

        proxy = space.uploads()

        self.assertEqual(str(proxy), "<SpaceUploadsProxy space_id='{0}'>".format(PLAYGROUND_SPACE))

    @vcr.use_cassette('fixtures/space/find_3.yaml')
    def test_space_webhooks(self):
        space = CLIENT.spaces().find(PLAYGROUND_SPACE)

        proxy = space.webhooks()

        self.assertEqual(str(proxy), "<SpaceWebhooksProxy space_id='{0}'>".format(PLAYGROUND_SPACE))
