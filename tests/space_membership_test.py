import vcr
from unittest import TestCase
from contentful_management.space_membership import SpaceMembership
from contentful_management.errors import NotFoundError
from .test_helper import CLIENT, PLAYGROUND_SPACE

MEMBERSHIP_ITEM = {
    "sys": {
        "type": "SpaceMembership",
        "id": "0xWanD4AZI2AR35wW9q51n",
        "version": 0,
        "createdBy": {
            "sys": {
                "type": "Link",
                "linkType": "User",
                "id": "4FLrUHftHW3v2BLi9fzfjU"
            }
        },
        "updatedBy": {
            "sys": {
                "type": "Link",
                "linkType": "User",
                "id": "4FLrUHftHW3v2BLi9fzfjU"
            }
        }
    },
    "admin": False,
    "roles": [
        {
            "type": "Link",
            "linkType": "Role",
            "id": "1ElgCn1mi1UHSBLTP2v4TD"
        }
    ],
    "user": {
        "sys": {
            "type": "Link",
            "linkType": "User",
            "id": "7BslKh9TdKGOK41VmLDjFZ"
        }
    }
}


class SpaceMembershipTest(TestCase):
    def test_space_membership(self):
        membership = SpaceMembership(MEMBERSHIP_ITEM)

        self.assertEqual(str(membership), "<SpaceMembership id='0xWanD4AZI2AR35wW9q51n' admin=False>")

    def test_space_membership_to_json(self):
        membership = SpaceMembership(MEMBERSHIP_ITEM)

        self.assertEqual(membership.to_json(), {
            "sys": {
                "type": "SpaceMembership",
                "id": "0xWanD4AZI2AR35wW9q51n",
                "version": 0,
                "createdBy": {
                    "sys": {
                        "type": "Link",
                        "linkType": "User",
                        "id": "4FLrUHftHW3v2BLi9fzfjU"
                    }
                },
                "updatedBy": {
                    "sys": {
                        "type": "Link",
                        "linkType": "User",
                        "id": "4FLrUHftHW3v2BLi9fzfjU"
                    }
                }
            },
            "admin": False,
            "roles": [
                {
                    "type": "Link",
                    "linkType": "Role",
                    "id": "1ElgCn1mi1UHSBLTP2v4TD"
                }
            ]
        })

    def test_space_membership_to_link(self):
        membership = SpaceMembership(MEMBERSHIP_ITEM)

        self.assertEqual(membership.to_link().to_json(), {
            'sys': {
                'id': '0xWanD4AZI2AR35wW9q51n',
                'type': 'Link',
                'linkType': 'SpaceMembership'
            }
        })

    @vcr.use_cassette('fixtures/memberships/all.yaml', decode_compressed_response=True)
    def test_space_memberships_all(self):
        memberships = CLIENT.memberships(PLAYGROUND_SPACE).all()

        self.assertTrue(memberships)
        self.assertEqual(str(memberships[0]), "<SpaceMembership id='1NI22o8oAxT9Jnu2J9wJSu' admin=True>")

    @vcr.use_cassette('fixtures/memberships/find.yaml', decode_compressed_response=True)
    def test_space_memberships_find(self):
        membership = CLIENT.memberships(PLAYGROUND_SPACE).find('1NI22o8oAxT9Jnu2J9wJSu')

        self.assertTrue(membership)
        self.assertEqual(str(membership), "<SpaceMembership id='1NI22o8oAxT9Jnu2J9wJSu' admin=True>")

    @vcr.use_cassette('fixtures/memberships/create.yaml', decode_compressed_response=True)
    def test_space_memberships_create(self):
        membership = CLIENT.memberships(PLAYGROUND_SPACE).create({
            "admin": False,
            "roles": [
                {
                    "type": "Link",
                    "linkType": "Role",
                    "id": "1Nq88dKTNXNaxkbrRpEEw6"
                }
            ],
            "email": "david.litva+test_memberships_create@contentful.com"
        })

        self.assertEqual(str(membership), "<SpaceMembership id='3x8XW8RsuC70XSmtlkrbLg' admin=False>")

    @vcr.use_cassette('fixtures/memberships/update.yaml', decode_compressed_response=True)
    def test_space_memberships_update(self):
        membership = CLIENT.memberships(PLAYGROUND_SPACE).find('3x8XW8RsuC70XSmtlkrbLg')
        self.assertEqual(str(membership), "<SpaceMembership id='3x8XW8RsuC70XSmtlkrbLg' admin=False>")

        membership.admin = True
        membership.save()

        membership = CLIENT.memberships(PLAYGROUND_SPACE).find('3x8XW8RsuC70XSmtlkrbLg')
        self.assertEqual(str(membership), "<SpaceMembership id='3x8XW8RsuC70XSmtlkrbLg' admin=True>")

    @vcr.use_cassette('fixtures/memberships/delete.yaml', decode_compressed_response=True)
    def test_space_memberships_delete(self):
        membership = CLIENT.memberships(PLAYGROUND_SPACE).find('3x8XW8RsuC70XSmtlkrbLg')
        self.assertEqual(str(membership), "<SpaceMembership id='3x8XW8RsuC70XSmtlkrbLg' admin=True>")

        membership.delete()
        with self.assertRaises(NotFoundError):
            CLIENT.memberships(PLAYGROUND_SPACE).find('3x8XW8RsuC70XSmtlkrbLg')
