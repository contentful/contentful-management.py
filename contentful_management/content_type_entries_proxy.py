from .content_type_resource_proxy import ContentTypeResourceProxy
from .entries_proxy import EntriesProxy


"""
contentful.content_type_entries_proxy
~~~~~~~~~~~~~~~~~~~~~~~

This module implements the ContentTypeEntriesProxy class.

API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/entries

:copyright: (c) 2017 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class ContentTypeEntriesProxy(ContentTypeResourceProxy):
    """
    API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/entries
    """

    def _resource_proxy_class(self):
        return EntriesProxy
