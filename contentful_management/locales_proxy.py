from .client_proxy import ClientProxy
from .locale import Locale


"""
contentful.locales_proxy
~~~~~~~~~~~~~~~~~~~~~~~

This module implements the LocalesProxy class.

API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/locales

:copyright: (c) 2017 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class LocalesProxy(ClientProxy):
    """
    API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/locales
    """

    @property
    def _resource_class(self):
        return Locale

    def create(self, attributes=None, **kwargs):
        """Creates a Locale with given attributes."""

        return super(LocalesProxy, self).create(None, attributes)
