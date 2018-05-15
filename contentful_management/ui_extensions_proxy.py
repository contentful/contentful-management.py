from .client_proxy import ClientProxy
from .ui_extension import UIExtension


"""
contentful_management.ui_extensions_proxy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the UIExtensionsProxy class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/ui-extensions

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class UIExtensionsProxy(ClientProxy):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/ui-extensions
    """

    @property
    def _resource_class(self):
        return UIExtension
