import vcr
from unittest import TestCase
from contentful_management.personal_access_token import PersonalAccessToken
from .test_helper import CLIENT, PLAYGROUND_SPACE

PERSONAL_ACCESS_TOKEN_WITH_TOKEN = {
    "sys": {
        "type": "PersonalAccessToken",
        "id": "exampletokenid",
        "createdAt": "2015-05-18T11:29:46.809Z",
        "updatedAt": "2015-05-18T11:29:46.809Z"
    },
    "name": "My Token",
    "revokedAt": None,
    "scopes": [
        "content_management_manage"
    ],
    "token": "CFPAT-THIS-WONT-WORK"
}

PERSONAL_ACCESS_TOKEN_WITHOUT_TOKEN = {
    "sys": {
        "type": "PersonalAccessToken",
        "id": "exampletokenid",
        "createdAt": "2015-05-18T11:29:46.809Z",
        "updatedAt": "2015-05-18T11:29:46.809Z"
    },
    "name": "My Token",
    "revokedAt": None,
    "scopes": [
        "content_management_manage"
    ]
}

PERSONAL_ACCESS_TOKEN_MULTIPLE_SCOPES = {
    "sys": {
        "type": "PersonalAccessToken",
        "id": "exampletokenid",
        "createdAt": "2015-05-18T11:29:46.809Z",
        "updatedAt": "2015-05-18T11:29:46.809Z"
    },
    "name": "My Token",
    "revokedAt": None,
    "scopes": [
        "content_management_manage",
        "content_management_read"
    ]
}

PERSONAL_ACCESS_TOKEN_REVOKED = {
    "sys": {
        "type": "PersonalAccessToken",
        "id": "exampletokenid",
        "createdAt": "2015-05-18T11:29:46.809Z",
        "updatedAt": "2015-05-18T11:29:46.809Z"
    },
    "name": "My Token",
    "revokedAt": "2015-05-18T11:29:46.809Z",
    "scopes": [
        "content_management_manage"
    ]
}


class PersonalAccessTokenTest(TestCase):
    def test_personal_access_token(self):
        with_token = PersonalAccessToken(PERSONAL_ACCESS_TOKEN_WITH_TOKEN)
        self.assertEqual(str(with_token), "<PersonalAccessToken[My Token] id='exampletokenid' scopes=['content_management_manage'] revoked=False>")
        self.assertEqual(with_token.token, 'CFPAT-THIS-WONT-WORK')

        without_token = PersonalAccessToken(PERSONAL_ACCESS_TOKEN_WITHOUT_TOKEN)
        self.assertEqual(str(without_token), "<PersonalAccessToken[My Token] id='exampletokenid' scopes=['content_management_manage'] revoked=False>")
        self.assertFalse(without_token.token)

        multiple_scopes = PersonalAccessToken(PERSONAL_ACCESS_TOKEN_MULTIPLE_SCOPES)
        self.assertEqual(str(multiple_scopes), "<PersonalAccessToken[My Token] id='exampletokenid' scopes=['content_management_manage', 'content_management_read'] revoked=False>")

        revoked = PersonalAccessToken(PERSONAL_ACCESS_TOKEN_REVOKED)
        self.assertEqual(str(revoked), "<PersonalAccessToken[My Token] id='exampletokenid' scopes=['content_management_manage'] revoked=True>")

    @vcr.use_cassette('fixtures/pat/all.yaml', decode_compressed_response=True)
    def test_personal_access_token_all(self):
        tokens = CLIENT.personal_access_tokens().all({'limit': 1})

        self.assertEqual(len(tokens), 1)
        self.assertEqual(tokens[0].name, 'Playground')

    @vcr.use_cassette('fixtures/pat/find.yaml', decode_compressed_response=True)
    def test_personal_access_token_find(self):
        token = CLIENT.personal_access_tokens().find('6ZJFnifPKNpxU8r8j9Xz14')

        self.assertEqual(token.name, 'Playground')
        self.assertFalse(token.is_revoked)
        self.assertEqual(str(token), "<PersonalAccessToken[Playground] id='6ZJFnifPKNpxU8r8j9Xz14' scopes=['content_management_manage'] revoked=False>")

    @vcr.use_cassette('fixtures/pat/find_2.yaml', decode_compressed_response=True)
    def test_personal_access_token_revoke(self):
        token = CLIENT.personal_access_tokens().find('6ZKYaf1m2PyFU7Olcnw5jK')

        self.assertFalse(token.is_revoked)

        with vcr.use_cassette('fixtures/pat/revoke.yaml'):
            token = CLIENT.personal_access_tokens().revoke('6ZKYaf1m2PyFU7Olcnw5jK')

            self.assertTrue(token.is_revoked)

    @vcr.use_cassette('fixtures/pat/revoke.yaml')
    def test_personal_access_token_delete_is_same_as_revoke(self):
        token = CLIENT.personal_access_tokens().delete('6ZKYaf1m2PyFU7Olcnw5jK')

        self.assertTrue(token.is_revoked)

    @vcr.use_cassette('fixtures/pat/create.yaml')
    def test_personal_access_token_create(self):
        token = CLIENT.personal_access_tokens().create({
            'name': 'Test Create',
            'scopes': ['content_management_manage']
        })

        self.assertEqual(str(token), "<PersonalAccessToken[Test Create] id='1Ca9dLr0O9OmX18kIWZ4Is' scopes=['content_management_manage'] revoked=False>")
