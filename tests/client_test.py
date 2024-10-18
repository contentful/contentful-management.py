import vcr
import re
from unittest import TestCase
from contentful_management import Client
from contentful_management.utils import ConfigurationException
from .test_helper import CLIENT, PLAYGROUND_SPACE, PLAYGROUND_KEY


class ClientTest(TestCase):
    def test_client(self):
        self.assertEqual(str(CLIENT), "<contentful_management.Client access_token='{0}' default_locale='en-US'>".format(PLAYGROUND_KEY))

    def test_client_snapshots(self):
        proxy = CLIENT.snapshots(PLAYGROUND_SPACE, 'master', 'foo')

        self.assertEqual(str(proxy), "<SnapshotsProxy[entries] space_id='{0}' environment_id='master' parent_resource_id='foo'>".format(PLAYGROUND_SPACE))

    def test_client_snapshots_content_type(self):
        proxy = CLIENT.snapshots(PLAYGROUND_SPACE, 'master', 'foo', 'content_types')

        self.assertEqual(str(proxy), "<SnapshotsProxy[content_types] space_id='{0}' environment_id='master' parent_resource_id='foo'>".format(PLAYGROUND_SPACE))

    def test_client_entry_snapshots(self):
        proxy = CLIENT.entry_snapshots(PLAYGROUND_SPACE, 'master', 'foo')

        self.assertEqual(str(proxy), "<SnapshotsProxy[entries] space_id='{0}' environment_id='master' parent_resource_id='foo'>".format(PLAYGROUND_SPACE))

    def test_client_content_type_snapshots(self):
        proxy = CLIENT.content_type_snapshots(PLAYGROUND_SPACE, 'master', 'foo')

        self.assertEqual(str(proxy), "<SnapshotsProxy[content_types] space_id='{0}' environment_id='master' parent_resource_id='foo'>".format(PLAYGROUND_SPACE))

    def test_client_ui_extensions(self):
        proxy = CLIENT.ui_extensions(PLAYGROUND_SPACE, 'master')

        self.assertEqual(str(proxy), "<UIExtensionsProxy space_id='{0}' environment_id='master'>".format(PLAYGROUND_SPACE))

    def test_client_users(self):
        proxy = CLIENT.users()

        self.assertEqual(str(proxy), "<UsersProxy>")

    def test_client_tags(self):
        proxy = CLIENT.tags(PLAYGROUND_SPACE, 'master')

        self.assertEqual(str(proxy), "<TagsProxy space_id='{0}' environment_id='master'>".format(PLAYGROUND_SPACE))

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

    @vcr.use_cassette('fixtures/client/entries.yaml', decode_compressed_response=True)
    def test_client_raw_mode(self):
        client = Client(PLAYGROUND_KEY, raw_mode=True)

        response = client.entries(PLAYGROUND_SPACE, 'master').all()

        self.assertEqual(response.status_code, 200)

    @vcr.use_cassette('fixtures/client/not_found.yaml', decode_compressed_response=True)
    def test_client_not_raise_errors(self):
        client = Client(PLAYGROUND_KEY, raise_errors=False)

        error = client.entries(PLAYGROUND_SPACE, 'master').find('not_here')

        self.assertEqual(error.status_code, 404)
        self.assertEqual(error.response.status_code, 404)

    def test_gzip_headers_enabled(self):
        client = Client(PLAYGROUND_SPACE, raise_errors=False)

        self.assertEqual(client._request_headers()['Accept-Encoding'], 'gzip')

    def test_gzip_headers_disabled(self):
        client = Client(PLAYGROUND_SPACE, gzip_encoded=False, raise_errors=False)

        self.assertEqual(client._request_headers()['Accept-Encoding'], 'identity')

    # X-Contentful-User-Agent Headers

    def test_client_default_contentful_user_agent_headers(self):
        client = Client(PLAYGROUND_SPACE, raise_errors=False)

        from contentful_management import __version__
        import platform
        expected = [
            'sdk contentful-management.py/{0};'.format(__version__),
            'platform python/{0};'.format(platform.python_version())
        ]
        header = client._contentful_user_agent()
        for e in expected:
            self.assertTrue(e in header)

        self.assertTrue(re.search('os (Windows|macOS|Linux)(/.*)?;', header))

        self.assertTrue('integration' not in header)
        self.assertTrue('app' not in header)

    def test_client_with_integration_name_only_headers(self):
        client = Client(
            PLAYGROUND_SPACE,
            raise_errors=False,
            integration_name='foobar')

        header = client._contentful_user_agent()
        self.assertTrue('integration foobar;' in header)
        self.assertFalse('integration foobar/;' in header)

    def test_client_with_integration_headers(self):
        client = Client(
            PLAYGROUND_SPACE,
            raise_errors=False,
            integration_name='foobar',
            integration_version='0.1.0')

        header = client._contentful_user_agent()
        self.assertTrue('integration foobar/0.1.0;' in header)

    def test_client_with_application_name_only_headers(self):
        client = Client(
            PLAYGROUND_SPACE,
            raise_errors=False,
            application_name='foobar')

        header = client._contentful_user_agent()
        self.assertTrue('app foobar;' in header)
        self.assertFalse('app foobar/;' in header)

    def test_client_with_application_headers(self):
        client = Client(
            PLAYGROUND_SPACE,
            raise_errors=False,
            application_name='foobar',
            application_version='0.1.0')

        header = client._contentful_user_agent()
        self.assertTrue('app foobar/0.1.0' in header)

    def test_client_with_integration_version_only_does_not_include_integration_in_header(self):
        client = Client(
            PLAYGROUND_SPACE,
            raise_errors=False,
            integration_version='0.1.0')

        header = client._contentful_user_agent()
        self.assertFalse('integration /0.1.0;' in header)

    def test_client_with_application_version_only_does_not_include_integration_in_header(self):
        client = Client(
            PLAYGROUND_SPACE,
            raise_errors=False,
            application_version='0.1.0')

        header = client._contentful_user_agent()
        self.assertFalse('app /0.1.0;' in header)

    def test_client_with_all_headers(self):
        client = Client(
            PLAYGROUND_SPACE,
            raise_errors=False,
            application_name='foobar_app',
            application_version='1.1.0',
            integration_name='foobar integ',
            integration_version='0.1.0')

        from contentful_management import __version__
        import platform
        expected = [
            'sdk contentful-management.py/{0};'.format(__version__),
            'platform python/{0};'.format(platform.python_version()),
            'app foobar_app/1.1.0;',
            'integration foobar integ/0.1.0;'
        ]
        header = client._contentful_user_agent()
        for e in expected:
            self.assertTrue(e in header)

        self.assertTrue(re.search('os (Windows|macOS|Linux)(/.*)?;', header))

    def test_client_headers(self):
        client = Client(
            PLAYGROUND_SPACE,
            raise_errors=False,
            application_name='foobar_app',
            application_version='1.1.0',
            integration_name='foobar integ',
            integration_version='0.1.0')

        from contentful_management import __version__
        import platform
        expected = [
            'sdk contentful-management.py/{0};'.format(__version__),
            'platform python/{0};'.format(platform.python_version()),
            'app foobar_app/1.1.0;',
            'integration foobar integ/0.1.0;'
        ]
        header = client._request_headers()['X-Contentful-User-Agent']
        for e in expected:
            self.assertTrue(e in header)

        self.assertTrue(re.search('os (Windows|macOS|Linux)(/.*)?;', header))

    @vcr.use_cassette('fixtures/client/additional_headers.yaml', decode_compressed_response=True)
    def test_client_with_additional_headers(self):
        client = Client(PLAYGROUND_KEY, raise_errors=False, additional_headers={'fizz': 'buzz'})

        error = client.entries(PLAYGROUND_SPACE, 'master').find('abc123')

        self.assertIn('fizz', error.response.request.headers)
