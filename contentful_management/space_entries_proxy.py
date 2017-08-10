from .space_resource_proxy import SpaceResourceProxy
from .entries_proxy import EntriesProxy


"""
contentful_management.space_entries_proxy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the SpaceEntriesProxy class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/entries

:copyright: (c) 2017 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class SpaceEntriesProxy(SpaceResourceProxy):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/entries
    """

    def _resource_proxy_class(self):
        return EntriesProxy
