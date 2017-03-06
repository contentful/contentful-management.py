from .client_proxy import ClientProxy
from .asset import Asset
from .utils import normalize_select


"""
contentful.assets_proxy
~~~~~~~~~~~~~~~~

This module implements the AssetsProxy class.

API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/assets

:copyright: (c) 2017 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class AssetsProxy(ClientProxy):
    """
    API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/assets
    """

    @property
    def _resource_class(self):
        return Asset

    def all(self, query=None, **kwargs):
        """
        Gets all assets of a Space.
        """

        if query is None:
            query = {}

        normalize_select(query)

        return super(AssetsProxy, self).all(query, **kwargs)

    def find(self, asset_id, query=None, **kwargs):
        """
        Gets a single asset by ID.
        """

        if query is None:
            query = {}

        normalize_select(query)

        return super(AssetsProxy, self).find(asset_id, query=query, **kwargs)
