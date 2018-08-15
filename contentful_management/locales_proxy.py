from .client_proxy import ClientProxy
from .locale import Locale


"""
contentful_management.locales_proxy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the LocalesProxy class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/locales

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class LocalesProxy(ClientProxy):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/locales
    """

    @property
    def _resource_class(self):
        return Locale

    def create(self, attributes=None, **kwargs):
        """
        Creates a locale with given attributes.
        """

        return super(LocalesProxy, self).create(None, attributes)
