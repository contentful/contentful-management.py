import vcr
from unittest import TestCase
from contentful_management import Client
from contentful_management.utils import ConfigurationException
from .test_helper import CLIENT, PLAYGROUND_SPACE, PLAYGROUND_KEY


class ClientTest(TestCase):
    def test_client(self):
        self.assertEqual(str(CLIENT), "<contentful_management.Client access_token='{0}' default_locale='en-US'>".format(PLAYGROUND_KEY))

    def test_client_snapshots(self):
        proxy = CLIENT.snapshots(PLAYGROUND_SPACE, 'foo')

        self.assertEqual(str(proxy), "<SnapshotsProxy space_id='{0}' entry_id='foo'>".format(PLAYGROUND_SPACE))

    def test_client_configuration_errors(self):
        with self.assertRaises(ConfigurationException):
            Client(None)

        with self.assertRaises(ConfigurationException):
            Client(PLAYGROUND_KEY, api_url=None)

        with self.assertRaises(ConfigurationException):
            Client(PLAYGROUND_KEY, default_locale=None)

        with self.assertRaises(ConfigurationException):
            Client(PLAYGROUND_KEY, api_version=None)

        with self.assertRaises(ConfigurationException):
            Client(PLAYGROUND_KEY, api_version=-1)

    def test_client_has_proxy(self):
        self.assertFalse(CLIENT._has_proxy())

        client = Client(PLAYGROUND_KEY, proxy_host='http://foo.com')

        self.assertTrue(client._has_proxy())

    @vcr.use_cassette('fixtures/client/entries.yaml')
    def test_client_raw_mode(self):
        client = Client(PLAYGROUND_KEY, raw_mode=True)

        response = client.entries(PLAYGROUND_SPACE).all()

        self.assertEqual(response.status_code, 200)

    @vcr.use_cassette('fixtures/client/not_found.yaml')
    def test_client_not_raise_errors(self):
        client = Client(PLAYGROUND_KEY, raise_errors=False)

        error = client.entries(PLAYGROUND_SPACE).find('not_here')

        self.assertEqual(error.status_code, 404)
        self.assertEqual(error.response.status_code, 404)
