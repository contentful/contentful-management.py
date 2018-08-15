from .environment_resource_proxy import EnvironmentResourceProxy
from .locales_proxy import LocalesProxy


"""
contentful_management.environment_locales_proxy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the EnvironmentLocalesProxy class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/entries

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class EnvironmentLocalesProxy(EnvironmentResourceProxy):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/entries
    """

    def _resource_proxy_class(self):
        return LocalesProxy

    def create(self, attributes=None, **kwargs):
        """
        Creates a locale with given attributes.
        """

        return super(EnvironmentLocalesProxy, self).create(None, attributes)
