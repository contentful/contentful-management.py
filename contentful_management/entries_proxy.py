from .client_proxy import ClientProxy
from .entry import Entry
from .utils import normalize_select


"""
contentful.entries_proxy
~~~~~~~~~~~~~~~~~~~~~~~

This module implements the EntriesProxy class.

API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/entries

:copyright: (c) 2017 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class EntriesProxy(ClientProxy):
    """
    API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/entries
    """

    def __init__(self, client, space_id, content_type_id=None):
        super(EntriesProxy, self).__init__(client, space_id)
        self.content_type_id = content_type_id

    @property
    def _resource_class(self):
        return Entry

    def all(self, query=None):
        """
        Gets all entries of a Space.
        """

        if query is None:
            query = {}

        if self.content_type_id is not None:
            query['content_type'] = self.content_type_id

        normalize_select(query)

        return super(EntriesProxy, self).all(query=query)

    def find(self, entry_id, query=None):
        """
        Gets a single entry by ID.
        """

        if query is None:
            query = {}

        if self.content_type_id is not None:
            query['content_type'] = self.content_type_id

        normalize_select(query)

        return super(EntriesProxy, self).find(entry_id, query=query)

    def create(self, resource_id=None, attributes=None, **kwargs):
        """
        Creates an entry with a given ID (optional) and attributes.
        """

        if self.content_type_id is not None:
            if attributes is None:
                attributes = {}
            attributes['content_type_id'] = self.content_type_id

        return super(EntriesProxy, self).create(resource_id=resource_id, attributes=attributes)
