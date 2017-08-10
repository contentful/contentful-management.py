from .space_resource_proxy import SpaceResourceProxy
from .assets_proxy import AssetsProxy


"""
contentful_management.space_assets_proxy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the SpaceAssetsProxy class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/assets

:copyright: (c) 2017 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class SpaceAssetsProxy(SpaceResourceProxy):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/assets
    """

    def _resource_proxy_class(self):
        return AssetsProxy
