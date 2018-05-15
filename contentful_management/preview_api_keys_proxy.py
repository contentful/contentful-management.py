from .client_proxy import ClientProxy
from .preview_api_key import PreviewApiKey


"""
contentful_management.preview_api_keys_proxy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the PreviewApiKeysProxy class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/api-keys

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class PreviewApiKeysProxy(ClientProxy):
    @property
    def _resource_class(self):
        return PreviewApiKey

    def create(*args, **kwargs):
        """
        Not supported.
        """

        raise Exception("Not Supported")

    def delete(*args, **kwargs):
        """
        Not supported.
        """

        raise Exception("Not Supported")
