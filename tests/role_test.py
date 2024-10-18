import vcr
from unittest import TestCase
from contentful_management.role import Role
from contentful_management.errors import NotFoundError
from .test_helper import CLIENT, PLAYGROUND_SPACE

ROLE_ITEM = {
    'name': 'Jedi Master',
    'description': 'Master of the Force',
    'permissions': {},
    'policies': [],
    'sys': {
        'id': 'foo',
        'type': 'Role',
        'space': {
            'sys': {
                'id': 'foobar',
                'type': 'Link',
                'linkType': 'Space'
            }
        }
    }
}


class RoleTest(TestCase):
    def test_role(self):
        role = Role(ROLE_ITEM)

        self.assertEqual(str(role), "<Role[Jedi Master] id='foo'>")

    def test_role_to_json(self):
        role = Role(ROLE_ITEM)

        self.assertEqual(role.to_json(), {
            'name': 'Jedi Master',
            'description': 'Master of the Force',
            'permissions': {},
            'policies': [],
            'sys': {
                'id': 'foo',
                'type': 'Role',
                'space': {
                    'sys': {
                        'id': 'foobar',
                        'type': 'Link',
                        'linkType': 'Space'
                    }
                }
            }
        })

    def test_role_to_link(self):
        role = Role(ROLE_ITEM)

        self.assertEqual(role.to_link().to_json(), {
            'sys': {
                'id': 'foo',
                'type': 'Link',
                'linkType': 'Role'
            }
        })

    @vcr.use_cassette('fixtures/role/create.yaml', decode_compressed_response=True)
    def test_create_role(self):
        role = CLIENT.roles(PLAYGROUND_SPACE).create({
            "name": "Jedi Master",
            "description": "Test role",
            "permissions": {
            },
            "policies": [
            ]
        })

        self.assertEqual(role.name, 'Jedi Master')

    @vcr.use_cassette('fixtures/role/find.yaml', decode_compressed_response=True)
    def test_update_role(self):
        role = CLIENT.roles(PLAYGROUND_SPACE).find('1a6FSwjdLnKifppXvfELau')

        with vcr.use_cassette('fixtures/role/update.yaml'):
            role.name = 'Not Klingon'
            role.save()

        self.assertEqual(role.name, 'Not Klingon')

    @vcr.use_cassette('fixtures/role/find_2.yaml', decode_compressed_response=True)
    def test_delete_role(self):
        role = CLIENT.roles(PLAYGROUND_SPACE).find('1a6FSwjdLnKifppXvfELau')

        with vcr.use_cassette('fixtures/role/delete.yaml'):
            role.delete()

        with vcr.use_cassette('fixtures/role/not_found.yaml'):
            with self.assertRaises(NotFoundError):
                CLIENT.roles(PLAYGROUND_SPACE).find('1a6FSwjdLnKifppXvfELau')
