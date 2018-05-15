from .client_proxy import ClientProxy
from .api_key import ApiKey


"""
contentful_management.api_keys_proxy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the ApiKeysProxy class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/api-keys

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class ApiKeysProxy(ClientProxy):
    @property
    def _resource_class(self):
        return ApiKey

    def create(self, attributes=None, **kwargs):
        """
        Creates an API key with given attributes.
        """

        return super(ApiKeysProxy, self).create(None, attributes)
