from .environment_resource_proxy import EnvironmentResourceProxy
from .entries_proxy import EntriesProxy


"""
contentful_management.environment_entries_proxy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the EnvironmentEntriesProxy class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/entries

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class EnvironmentEntriesProxy(EnvironmentResourceProxy):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/entries
    """

    def _resource_proxy_class(self):
        return EntriesProxy
