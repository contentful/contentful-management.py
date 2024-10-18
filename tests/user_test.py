import vcr
from unittest import TestCase
from contentful_management.user import User
from .test_helper import CLIENT

USER_ITEM = {
    "sys": {
        "type": "User",
        "id": "exampleuserid",
        "version": 1,
        "createdAt": "2015-05-18T11:29:46.809Z",
        "updatedAt": "2015-05-18T11:29:46.809Z"
    },
    "firstName": "Dwight",
    "lastName": "Schrute",
    "avatarUrl": "https://images.contentful.com/abcd1234",
    "email": "dwight@dundermifflin.com",
    "activated": True,
    "signInCount": 1,
    "confirmed": True
}


class WebhookHealthTest(TestCase):
    def test_user(self):
        user = User(USER_ITEM)

        self.assertEqual(str(user), "<User[Dwight Schrute] email='dwight@dundermifflin.com' activated=True confirmed=True sign_in_count=1>")

    def test_fail_create_user(self):
        with self.assertRaises(Exception):
            CLIENT.users().create()

    def test_fail_delete_user(self):
        with self.assertRaises(Exception):
            CLIENT.users().delete('foobar')

    def test_fail_all_user(self):
        with self.assertRaises(Exception):
            CLIENT.users().all()

    @vcr.use_cassette('fixtures/users/me.yaml', decode_compressed_response=True)
    def test_users_me(self):
        user = CLIENT.users().me()

        self.assertEqual(str(user), "<User[David Litvak Bruno] email='david.litvak@contentful.com' activated=True confirmed=True sign_in_count=23>")
        self.assertEqual(user.first_name, "David")
        self.assertEqual(user.last_name, "Litvak Bruno")
        self.assertEqual(user.email, "david.litvak@contentful.com")
        self.assertTrue(user.activated)
        self.assertTrue(user.confirmed)
        self.assertTrue(user.sign_in_count)
