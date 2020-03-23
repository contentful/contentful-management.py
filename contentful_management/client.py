import requests
import platform
from re import sub

from .resource_builder import ResourceBuilder
from .errors import get_error, RateLimitExceededError
from .utils import ConfigurationException, retry_request

from .users_proxy import UsersProxy
from .roles_proxy import RolesProxy
from .assets_proxy import AssetsProxy
from .spaces_proxy import SpacesProxy
from .entries_proxy import EntriesProxy
from .locales_proxy import LocalesProxy
from .uploads_proxy import UploadsProxy
from .api_keys_proxy import ApiKeysProxy
from .webhooks_proxy import WebhooksProxy
from .snapshots_proxy import SnapshotsProxy
from .environments_proxy import EnvironmentsProxy
from .webhooks_call_proxy import WebhooksCallProxy
from .ui_extensions_proxy import UIExtensionsProxy
from .content_types_proxy import ContentTypesProxy
from .organizations_proxy import OrganizationsProxy
from .webhooks_health_proxy import WebhooksHealthProxy
from .preview_api_keys_proxy import PreviewApiKeysProxy
from .space_memberships_proxy import SpaceMembershipsProxy
from .editor_interfaces_proxy import EditorInterfacesProxy
from .space_periodic_usages_proxy import SpacePeriodicUsagesProxy
from .personal_access_tokens_proxy import PersonalAccessTokensProxy
from .organization_periodic_usages_proxy import OrganizationPeriodicUsagesProxy

try:
    import multijson as json
except ImportError:
    import json


"""
contentful_management.client
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the Contentful Management API Client,
allowing interaction with every method present in it.

Complete API documentation: https://www.contentful.com/developers/docs/references/content-management-api

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class Client(object):
    """Constructs the API client.

    :param access_token: API access token.
    :param api_url: (optional) URL of the Contentful API,
        defaults to Management API.
    :param uploads_api_url: (optional) URL of the Contentful upload API,
        defaults to Upload API.
    :param api_version: (optional) Target version of the Contentful API.
    :param default_locale: (optional) Default locale for your spaces,
        defaults to 'en-US'.
    :param https: (optional) Boolean determining wether to use https
        or http, defaults to True.
    :param raw_mode: (optional) Boolean determining wether to process the
        response or return it raw after each API call, defaults to True.
    :param gzip_encoded: (optional) Boolean determining wether to accept
        gzip encoded results, defaults to True.
    :param raise_errors: (optional) Boolean determining wether to raise
        an exception on requests that aren't successful, defaults to True.
    :param proxy_host: (optional) URL for Proxy, defaults to None.
    :param proxy_port: (optional) Port for Proxy, defaults to None.
    :param proxy_username: (optional) Username for Proxy, defaults to None.
    :param proxy_password: (optional) Password for Proxy, defaults to None.
    :param max_rate_limit_retries: (optional) Maximum amount of retries
        after RateLimitError, defaults to 1.
    :param max_rate_limit_wait: (optional) Timeout (in seconds) for waiting
        for retry after RateLimitError, defaults to 60.
    :param application_name: (optional) User application name, defaults to None.
    :param application_version: (optional) User application version, defaults to None.
    :param integration_name: (optional) Integration name, defaults to None.
    :param integration_version: (optional) Integration version, defaults to None.
    :return: :class:`Client <Client>` object.
    :rtype: contentful.Client

    Usage:

        >>> import contentful_management
        >>> client = contentful_management.Client('YOUR_MANAGEMENT_TOKEN')
        <contentful_management.Client access_token="YOUR_MANAGEMENT_TOKEN" default_locale="en-US">
    """

    def __init__(
            self,
            access_token,
            api_url='api.contentful.com',
            uploads_api_url='upload.contentful.com',
            api_version=1,
            default_locale='en-US',
            https=True,
            raw_mode=False,
            gzip_encoded=True,
            raise_errors=True,
            proxy_host=None,
            proxy_port=None,
            proxy_username=None,
            proxy_password=None,
            max_rate_limit_retries=1,
            max_rate_limit_wait=60,
            application_name=None,
            application_version=None,
            integration_name=None,
            integration_version=None,
            additional_headers=None):
        self.access_token = access_token
        self.api_url = api_url
        self.uploads_api_url = uploads_api_url
        self.api_version = api_version
        self.default_locale = default_locale
        self.https = https
        self.raw_mode = raw_mode
        self.gzip_encoded = gzip_encoded
        self.raise_errors = raise_errors
        self.proxy_host = proxy_host
        self.proxy_port = proxy_port
        self.proxy_username = proxy_username
        self.proxy_password = proxy_password
        self.max_rate_limit_retries = max_rate_limit_retries
        self.max_rate_limit_wait = max_rate_limit_wait
        self.application_name = application_name
        self.application_version = application_version
        self.integration_name = integration_name
        self.integration_version = integration_version
        self.additional_headers = additional_headers or {}

        self._validate_configuration()

    def spaces(self):
        """
        Provides access to space management methods.

        API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/spaces

        :return: :class:`SpacesProxy <contentful_management.spaces_proxy.SpacesProxy>` object.
        :rtype: contentful.spaces_proxy.SpacesProxy

        Usage:

            >>> spaces_proxy = client.spaces()
            <SpacesProxy>
        """

        return SpacesProxy(self)

    def memberships(self, space_id):
        """
        Provides access to space membership management methods.

        API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/space-memberships

        :return: :class:`SpaceMembershipsProxy <contentful_management.space_memberships_proxy.SpaceMembershipsProxy>` object.
        :rtype: contentful.space_memberships_proxy.SpaceMembershipsProxy

        Usage:

            >>> space_memberships_proxy = client.memberships('cfexampleapi')
            <SpaceMembershipsProxy space_id="cfexampleapi">
        """

        return SpaceMembershipsProxy(self, space_id)

    def organizations(self):
        """
        Provides access to organization management methods.

        API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/organizations

        :return: :class:`OrganizationsProxy <contentful_management.organizations_proxy.OrganizationsProxy>` object.
        :rtype: contentful.organizations_proxy.OrganizationsProxy

        Usage:

            >>> organizations_proxy = client.organizations()
            <OrganizationsProxy>
        """

        return OrganizationsProxy(self)

    def organization_periodic_usages(self, organization_id):
        """
        Provides access to an organizations usage periods.

        API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/usage

        :return: :class:`OrganizationPeriodicUsagesProxy <contentful_management.organization_periodic_usages_proxy.OrganizationPeriodicUsagesProxy>` object.
        :rtype: contentful.organization_periodic_usages.OrganizationPeriodicUsagesProxy

        Usage:

            >>> organization_periodic_usages = client.organization_periodic_usages('organization_id')
            <OrganizationPeriodicUsagesProxy organization_id='organization_id'>
        """

        return OrganizationPeriodicUsagesProxy(self, organization_id)

    def space_periodic_usages(self, organization_id):
        """
        Provides access to an organizations usage periods grouped by space.

        API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/usage

        :return: :class:`SpacePeriodicUsagesProxy <contentful_management.space_periodic_usages_proxy.SpacePeriodicUsagesProxy>` object.
        :rtype: contentful.space_periodic_usages_proxy.SpacePeriodicUsagesProxy

        Usage:

            >>> space_periodic_usages = client.space_periodic_usages('organization_id')
            <SpacePeriodicUsagesProxy organization_id='organization_id'>
        """

        return SpacePeriodicUsagesProxy(self, organization_id)

    def users(self):
        """
        Provides access to user management methods.

        API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/users

        :return: :class:`UsersProxy <contentful_management.users_proxy.UsersProxy>` object.
        :rtype: contentful.users_proxy.UsersProxy

        Usage:

            >>> users_proxy = client.users()
            <UsersProxy>
        """

        return UsersProxy(self)

    def content_types(self, space_id, environment_id):
        """
        Provides access to content type management methods.

        API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/content-types

        :return: :class:`ContentTypesProxy <contentful_management.content_types_proxy.ContentTypesProxy>` object.
        :rtype: contentful.content_types_proxy.ContentTypesProxy

        Usage:

            >>> content_types_proxy = client.content_types('cfexampleapi', 'master')
            <ContentTypesProxy space_id="cfexampleapi" environment_id="master">
        """

        return ContentTypesProxy(self, space_id, environment_id)

    def entries(self, space_id, environment_id):
        """
        Provides access to entry management methods.

        API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/entries

        :return: :class:`EntriesProxy <contentful_management.entries_proxy.EntriesProxy>` object.
        :rtype: contentful.entries_proxy.EntriesProxy

        Usage:

            >>> entries_proxy = client.entries('cfexampleapi', 'master')
            <EntriesProxy space_id="cfexampleapi" environment_id="master">
        """

        return EntriesProxy(self, space_id, environment_id)

    def assets(self, space_id, environment_id):
        """
        Provides access to asset management methods.

        API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/assets

        :return: :class:`AssetsProxy <contentful_management.assets_proxy.AssetsProxy>` object.
        :rtype: contentful.assets_proxy.AssetsProxy

        Usage:

            >>> assets_proxy = client.assets('cfexampleapi', 'master')
            <AssetsProxy space_id="cfexampleapi" environment_id="master">
        """

        return AssetsProxy(self, space_id, environment_id)

    def locales(self, space_id, environment_id):
        """
        Provides access to locale management methods.

        API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/locales

        :return: :class:`LocalesProxy <contentful_management.locales_proxy.LocalesProxy>` object.
        :rtype: contentful.locales_proxy.LocalesProxy

        Usage:

            >>> locales_proxy = client.locales('cfexampleapi', 'master')
            <LocalesProxy space_id="cfexampleapi" environment_id="master">
        """

        return LocalesProxy(self, space_id, environment_id)

    def webhooks(self, space_id):
        """
        Provides access to webhook management methods.

        API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/webhooks

        :return: :class:`WebhooksProxy <contentful_management.locales_proxy.WebhooksProxy>` object.
        :rtype: contentful.webhooks_proxy.WebhooksProxy

        Usage:

            >>> webhooks_proxy = client.webhooks('cfexampleapi')
            <WebhooksProxy space_id="cfexampleapi">
        """

        return WebhooksProxy(self, space_id)

    def webhook_calls(self, space_id, webhook_id):
        """
        Provides access to webhook call information.

        API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/webhook-calls

        :return: :class:`WebhooksProxy <contentful_management.webhooks_call_proxy.WebhooksCallProxy>` object.
        :rtype: contentful.webhooks_call_proxy.WebhooksProxy

        Usage:

            >>> webhooks_call_proxy = client.webhook_calls('cfexampleapi', 'my_webhook')
            <WebhooksCallProxy space_id="cfexampleapi" webhook_id="my_webhook">
        """

        return WebhooksCallProxy(self, space_id, webhook_id)

    def webhook_health(self, space_id, webhook_id):
        """
        Provides access to webhook health information.

        API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/webhook-calls/webhook-health

        :return: :class:`WebhooksHealthProxy <contentful_management.webhooks_health_proxy.WebhooksHealthProxy>` object.
        :rtype: contentful.webhooks_health_proxy.WebhooksHealthProxy

        Usage:

            >>> webhooks_health_proxy = client.webhook_calls('cfexampleapi', 'my_webhook')
            <WebhooksHealthProxy space_id="cfexampleapi" webhook_id="my_webhook">
        """

        return WebhooksHealthProxy(self, space_id, webhook_id)

    def api_keys(self, space_id):
        """
        Provides access to API key management methods.

        API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/api-keys

        :return: :class:`ApiKeysProxy <contentful_management.api_keys_proxy.ApiKeysProxy>` object.
        :rtype: contentful.api_keys_proxy.ApiKeysProxy

        Usage:

            >>> api_keys_proxy = client.api_keys('cfexampleapi')
            <ApiKeysProxy space_id="cfexampleapi">
        """

        return ApiKeysProxy(self, space_id)

    def preview_api_keys(self, space_id):
        """
        Provides access to Preview API key management methods.

        API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/api-keys/preview-api-key/get-a-single-preview-api-key

        :return: :class:`PreviewApiKeysProxy <contentful_management.preview_api_keys_proxy.PreviewApiKeysProxy>` object.
        :rtype: contentful.preview_api_keys_proxy.PreviewApiKeysProxy

        Usage:

            >>> preview_api_keys_proxy = client.preview_api_keys('cfexampleapi')
            <PreviewApiKeysProxy space_id="cfexampleapi">
        """

        return PreviewApiKeysProxy(self, space_id)

    def personal_access_tokens(self):
        """
        Provides access to personal access token management methods.

        API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/personal-access-tokens

        :return: :class:`PersonalAccessTokensProxy <contentful_management.personal_access_tokens_proxy.PersonalAccessTokensProxy>` object.
        :rtype: contentful.personal_access_tokens_proxy.PersonalAccessTokensProxy

        Usage:

            >>> personal_access_tokens_proxy = client.personal_access_tokens()
            <PersonalAccessTokensProxy>
        """

        return PersonalAccessTokensProxy(self)

    def roles(self, space_id):
        """
        Provides access to role management methods.

        API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/roles

        :return: :class:`RolesProxy <contentful_management.roles_proxy.RolesProxy>` object.
        :rtype: contentful.roles_proxy.RolesProxy

        Usage:

            >>> roles_proxy = client.roles('cfexampleapi')
            <RolesProxy space_id="cfexampleapi">
        """

        return RolesProxy(self, space_id)

    def ui_extensions(self, space_id, environment_id):
        """
        Provides access to UI extensions management methods.

        API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/ui-extensions

        :return: :class:`UIExtensionsProxy <contentful_management.ui_extensions_proxy.UIExtensionsProxy>` object.
        :rtype: contentful.ui_extensions_proxy.UIExtensionsProxy

        Usage:

            >>> ui_extensions_proxy = client.ui_extensions('cfexampleapi', 'master')
            <UIExtensionsProxy space_id="cfexampleapi" environment_id="master">
        """

        return UIExtensionsProxy(self, space_id, environment_id)

    def editor_interfaces(self, space_id, environment_id, content_type_id):
        """
        Provides access to editor interfaces management methods.

        API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/editor-interface

        :return: :class:`EditorInterfacesProxy <contentful_management.editor_interfaces_proxy.EditorInterfacesProxy>` object.
        :rtype: contentful.editor_interfaces_proxy.EditorInterfacesProxy

        Usage:

            >>> editor_interfaces_proxy = client.editor_interfaces('cfexampleapi', 'master', 'cat')
            <EditorInterfacesProxy space_id="cfexampleapi" environment_id="master" content_type_id="cat">
        """

        return EditorInterfacesProxy(self, space_id, environment_id, content_type_id)

    def snapshots(self, space_id, environment_id, resource_id, resource_kind='entries'):
        """
        Provides access to snapshot management methods.

        API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/snapshots

        :return: :class:`SnapshotsProxy <contentful_management.snapshots_proxy.SnapshotsProxy>` object.
        :rtype: contentful.snapshots_proxy.SnapshotsProxy

        Usage:

            >>> entry_snapshots_proxy = client.snapshots('cfexampleapi', 'master', 'nyancat')
            <SnapshotsProxy[entries] space_id="cfexampleapi" environment_id="master" parent_resource_id="nyancat">

            >>> content_type_snapshots_proxy = client.snapshots('cfexampleapi', 'master', 'cat', 'content_types')
            <SnapshotsProxy[content_types] space_id="cfexampleapi" environment_id="master" parent_resource_id="cat">
        """

        return SnapshotsProxy(self, space_id, environment_id, resource_id, resource_kind)

    def entry_snapshots(self, space_id, environment_id, entry_id):
        """
        Provides access to entry snapshot management methods.

        API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/snapshots

        :return: :class:`SnapshotsProxy <contentful_management.snapshots_proxy.SnapshotsProxy>` object.
        :rtype: contentful.snapshots_proxy.SnapshotsProxy

        Usage:

            >>> entry_snapshots_proxy = client.entry_snapshots('cfexampleapi', 'master', 'nyancat')
            <SnapshotsProxy[entries] space_id="cfexampleapi" environment_id="master" parent_resource_id="nyancat">
        """

        return SnapshotsProxy(self, space_id, environment_id, entry_id, 'entries')

    def content_type_snapshots(self, space_id, environment_id, content_type_id):
        """
        Provides access to content type snapshot management methods.

        API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/snapshots

        :return: :class:`SnapshotsProxy <contentful_management.snapshots_proxy.SnapshotsProxy>` object.
        :rtype: contentful.snapshots_proxy.SnapshotsProxy

        Usage:

            >>> content_type_snapshots_proxy = client.content_type_snapshots('cfexampleapi', 'master', 'cat')
            <SnapshotsProxy[content_types] space_id="cfexampleapi" environment_id="master" parent_resource_id="cat">
        """

        return SnapshotsProxy(self, space_id, environment_id, content_type_id, 'content_types')

    def uploads(self, space_id):
        """
        Provides access to upload management methods.

        API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/uploads

        :return: :class:`UploadsProxy <contentful_management.uploads_proxy.UploadsProxy>` object.
        :rtype: contentful.uploads_proxy.UploadsProxy

        Usage:

            >>> uploads_proxy = client.uploads('cfexampleapi')
            <UploadsProxy space_id="cfexampleapi">
        """

        return UploadsProxy(self, space_id)

    def environments(self, space_id):
        """
        Provides access to environment management methods.

        API reference: TBD

        :return: :class:`TBD` object.
        :rtype: contentful.environments_proxy.EnvironmentsProxy

        Usage:

            >>> environments_proxy = client.environments('cfexampleapi')
            <EnvironmentsProxy space_id="cfexampleapi">
        """

        return EnvironmentsProxy(self, space_id)

    def _validate_configuration(self):
        """
        Validates that required parameters are present.
        """

        if not self.access_token:
            raise ConfigurationException(
                'You will need to initialize a client with an Access Token'
            )
        if not self.api_url:
            raise ConfigurationException(
                'The client configuration needs to contain an API URL'
            )
        if not self.default_locale:
            raise ConfigurationException(
                'The client configuration needs to contain a Default Locale'
            )
        if not self.api_version or self.api_version < 1:
            raise ConfigurationException(
                'The API Version must be a positive number'
            )

    def _contentful_user_agent(self):
        """
        Sets the X-Contentful-User-Agent header.
        """
        header = {}
        from . import __version__
        header['sdk'] = {
            'name': 'contentful-management.py',
            'version': __version__
        }
        header['app'] = {
            'name': self.application_name,
            'version': self.application_version
        }
        header['integration'] = {
            'name': self.integration_name,
            'version': self.integration_version
        }
        header['platform'] = {
            'name': 'python',
            'version': platform.python_version()
        }

        os_name = platform.system()
        if os_name == 'Darwin':
            os_name = 'macOS'
        elif not os_name or os_name == 'Java':
            os_name = None
        elif os_name and os_name not in ['macOS', 'Windows']:
            os_name = 'Linux'
        header['os'] = {
            'name': os_name,
            'version': platform.release()
        }

        def format_header(key, values):
            header = "{0} {1}".format(key, values['name'])
            if values['version'] is not None:
                header = "{0}/{1}".format(header, values['version'])
            return "{0};".format(header)

        result = []
        for k, values in header.items():
            if not values['name']:
                continue
            result.append(format_header(k, values))

        return ' '.join(result)

    def _request_headers(self):
        """
        Sets the default request headers.
        """

        headers = {
            'X-Contentful-User-Agent': self._contentful_user_agent(),
            'Content-Type':
                'application/vnd.contentful.management.v{0}+json'.format(
                    self.api_version
                ),
            'Authorization': 'Bearer {0}'.format(self.access_token)
        }

        if self.gzip_encoded:
            headers['Accept-Encoding'] = 'gzip'
        else:
            headers['Accept-Encoding'] = 'identity'

        return headers

    def _url(self, url, file_upload=False):
        """
        Creates the request URL.
        """

        host = self.api_url
        if file_upload:
            host = self.uploads_api_url

        protocol = 'https' if self.https else 'http'
        if url.endswith('/'):
            url = url[:-1]
        return '{0}://{1}/{2}'.format(
            protocol,
            host,
            url
        )

    def _normalize_query(self, query):
        """
        Converts arrays in the query to comma
        separated lists for proper API handling.
        """

        for k, v in query.items():
            if isinstance(v, list):
                query[k] = ','.join(v)

    def _http_request(self, method, url, request_kwargs=None):
        """
        Performs the requested HTTP request.
        """

        kwargs = request_kwargs if request_kwargs is not None else {}

        headers = self._request_headers()
        headers.update(self.additional_headers)
        if 'headers' in kwargs:
            headers.update(kwargs['headers'])
        kwargs['headers'] = headers

        if self._has_proxy():
            kwargs['proxies'] = self._proxy_parameters()

        request_url = self._url(
            url,
            file_upload=kwargs.pop('file_upload', False)
        )

        request_method = getattr(requests, method)
        response = request_method(request_url, **kwargs)
        response.encoding = 'utf-8'

        if response.status_code == 429:
            raise RateLimitExceededError(response)

        return response

    def _http_get(self, url, query, **kwargs):
        """
        Performs the HTTP GET request.
        """

        self._normalize_query(query)

        kwargs.update({'params': query})

        return self._http_request('get', url, kwargs)

    def _http_post(self, url, data, **kwargs):
        """
        Performs the HTTP POST request.
        """

        if not kwargs.get('file_upload', False):
            data = json.dumps(data)

        kwargs.update({'data': data})

        return self._http_request('post', url, kwargs)

    def _http_put(self, url, data, **kwargs):
        """
        Performs the HTTP PUT request.
        """

        kwargs.update({'data': json.dumps(data)})

        return self._http_request('put', url, kwargs)

    def _http_delete(self, url, _data, **kwargs):
        """
        Performs the HTTP DELETE request.
        """

        return self._http_request('delete', url, kwargs)

    def _request(self, method, url, query_or_data=None, **kwargs):
        """
        Wrapper for the HTTP requests,
        rate limit backoff is handled here,
        responses are processed with ResourceBuilder.
        """

        if query_or_data is None:
            query_or_data = {}

        request_method = getattr(self, '_http_{0}'.format(method))
        response = retry_request(self)(request_method)(url, query_or_data, **kwargs)

        if self.raw_mode:
            return response

        if response.status_code >= 300:
            error = get_error(response)
            if self.raise_errors:
                raise error
            return error

        # Return response object on NoContent
        if response.status_code == 204 or not response.text:
            return response

        return ResourceBuilder(
            self,
            self.default_locale,
            response.json()
        ).build()

    def _get(self, url, query=None, **kwargs):
        """
        Wrapper for the HTTP GET request.
        """

        return self._request('get', url, query, **kwargs)

    def _post(self, url, attributes=None, **kwargs):
        """
        Wrapper for the HTTP POST request.
        """

        return self._request('post', url, attributes, **kwargs)

    def _put(self, url, attributes=None, **kwargs):
        """
        Wrapper for the HTTP PUT request.
        """

        return self._request('put', url, attributes, **kwargs)

    def _delete(self, url, **kwargs):
        """
        Wrapper for the HTTP DELETE request.
        """

        response = retry_request(self)(self._http_delete)(url, **kwargs)

        if self.raw_mode:
            return response

        if response.status_code >= 300:
            error = get_error(response)
            if self.raise_errors:
                raise error
            return error

        return response

    def _has_proxy(self):
        """
        Checks if a proxy was set.
        """

        return self.proxy_host

    def _proxy_parameters(self):
        """
        Builds proxy parameters dict from
        client options.
        """

        proxy_protocol = ''
        if self.proxy_host.startswith('https'):
            proxy_protocol = 'https'
        else:
            proxy_protocol = 'http'

        proxy = '{0}://'.format(proxy_protocol)
        if self.proxy_username and self.proxy_password:
            proxy += '{0}:{1}@'.format(self.proxy_username, self.proxy_password)

        proxy += sub(r'https?(://)?', '', self.proxy_host)

        if self.proxy_port:
            proxy += ':{0}'.format(self.proxy_port)

        return {
            'http': proxy,
            'https': proxy
        }

    def __repr__(self):
        return "<contentful_management.Client access_token='{0}' default_locale='{1}'>".format(  # noqa: E501
            self.access_token,
            self.default_locale
        )
