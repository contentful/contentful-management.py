from .resource import FieldsResource, PublishResource, ArchiveResource
from .utils import is_link, is_link_array, snake_case
from .entry_snapshots_proxy import EntrySnapshotsProxy


"""
contentful.entry
~~~~~~~~~~~~~~~~

This module implements the Entry class.

API Reference: https://www.contentful.com/developers/docs/references/content-delivery-api/#/reference/entries

:copyright: (c) 2016 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class Entry(FieldsResource, PublishResource, ArchiveResource):
    """
    API Reference: https://www.contentful.com/developers/docs/references/content-delivery-api/#/reference/entries
    """

    @classmethod
    def create_headers(klass, attributes):
        """Headers for resource creation"""

        if 'content_type_id' not in attributes:
            raise Exception("Content Type ID ('content_type_id') must be provided for this operation.")
        return {'x-contentful-content-type': attributes['content_type_id']}

    def __init__(self, *args, **kwargs):
        self.__CONTENT_TYPE__ = None
        super(Entry, self).__init__(*args, **kwargs)

    def snapshots(self):
        """Provides access to Snapshot management methods for the given Entry

        API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/snapshots

        :return: :class:`EntrySnapshotsProxy <contentful_management.entry_snapshots_proxy.EntrySnapshotsProxy>` object.
        :rtype: contentful.entry_snapshots_proxy.EntrySnapshotsProxy

        Usage:

            >>> entry_snapshots_proxy = entry.snapshots()
            <EntrySnapshotsProxy space_id="cfexampleapi" entry_id="nyancat">
        """
        return EntrySnapshotsProxy(self._client, self.sys['space'].id, self.sys['id'])

    def update(self, attributes=None):
        """Updates the Entry with attributes"""

        if attributes is None:
            attributes = {}

        attributes['content_type_id'] = self.sys['content_type'].id

        return super(Entry, self).update(attributes)

    def _coerce(self, value):
        if is_link(value):
            return self._build_link(value)
        elif is_link_array(value):
            return [self._build_link(link)
                    for link in value]
        return super(Entry, self)._coerce(value)

    def _missing_field_raw_id(self, name):
        for field in self._content_type().fields:
            if snake_case(field.id) == name:
                return field.id

    def _is_missing_field(self, name):
        """
        Fields that are voided in the WebApp will be not returned in
        API responses, therefore we need to check if they are part of
        the Content Type to determine if they should or should not be
        serialized.
        """

        return self._missing_field_raw_id(name) is not None

    def _content_type(self):
        if self.__CONTENT_TYPE__ is None:
            self.__CONTENT_TYPE__ = self.sys['content_type'].resolve(self.sys['space'].id)
        return self.__CONTENT_TYPE__

    def _real_field_id_for(self, field_id):
        raw_field_id = super(Entry, self)._real_field_id_for(field_id)
        if raw_field_id is None:
            return self._missing_field_raw_id(field_id)
        return raw_field_id

    def __repr__(self):
        return "<Entry[{0}] id='{1}'>".format(
            self.sys['content_type'].sys.get('id', ''),
            self.sys.get('id', '')
        )
