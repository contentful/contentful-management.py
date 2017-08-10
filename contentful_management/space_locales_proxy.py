from .space_resource_proxy import SpaceResourceProxy
from .locales_proxy import LocalesProxy


"""
contentful_management.space_locales_proxy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the SpaceLocalesProxy class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/locales

:copyright: (c) 2017 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class SpaceLocalesProxy(SpaceResourceProxy):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/locales
    """

    def _resource_proxy_class(self):
        return LocalesProxy
