from .space_resource_proxy import SpaceResourceProxy
from .preview_api_keys_proxy import PreviewApiKeysProxy


"""
contentful_management.space_api_keys_proxy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the SpacePreviewApiKeysProxy class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/api-keys/preview-api-key/get-a-single-preview-api-key

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class SpacePreviewApiKeysProxy(SpaceResourceProxy):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/api-keys/preview-api-key/get-a-single-preview-api-key
    """

    def _resource_proxy_class(self):
        return PreviewApiKeysProxy

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
