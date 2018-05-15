from .environment_resource_proxy import EnvironmentResourceProxy
from .ui_extensions_proxy import UIExtensionsProxy


"""
contentful_management.environment_ui_extensions_proxy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the EnvironmentLocalesProxy class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/entries

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class EnvironmentUIExtensionsProxy(EnvironmentResourceProxy):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/entries
    """

    def _resource_proxy_class(self):
        return UIExtensionsProxy
