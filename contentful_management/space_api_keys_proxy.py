from .space_resource_proxy import SpaceResourceProxy
from .api_keys_proxy import ApiKeysProxy


"""
contentful.space_api_keys_proxy
~~~~~~~~~~~~~~~~~~~~~~~

This module implements the SpaceApiKeysProxy class.

API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/api-keys

:copyright: (c) 2017 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class SpaceApiKeysProxy(SpaceResourceProxy):
    """
    API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/api-keys
    """

    def _resource_proxy_class(self):
        return ApiKeysProxy
