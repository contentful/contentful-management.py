from .space_resource_proxy import SpaceResourceProxy
from .api_keys_proxy import ApiKeysProxy


"""
contentful_management.space_api_keys_proxy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the SpaceApiKeysProxy class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/api-keys

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class SpaceApiKeysProxy(SpaceResourceProxy):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/api-keys
    """

    def _resource_proxy_class(self):
        return ApiKeysProxy

    def create(self, attributes=None, **kwargs):
        """
        Creates an api key with given attributes.
        """

        return super(SpaceApiKeysProxy, self).create(None, attributes)
