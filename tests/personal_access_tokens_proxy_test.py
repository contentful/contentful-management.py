from unittest import TestCase
from contentful_management.personal_access_tokens_proxy import PersonalAccessTokensProxy
from .test_helper import CLIENT, PLAYGROUND_SPACE


class PersonalAccessTokensProxyTest(TestCase):
    def test_personal_access_tokens_proxy(self):
        proxy = PersonalAccessTokensProxy(CLIENT)

        self.assertEqual(str(proxy), "<PersonalAccessTokensProxy>")
