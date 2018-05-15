from .content_type_resource_proxy import ContentTypeResourceProxy
from .snapshots_proxy import SnapshotsProxy


"""
contentful_management.content_type_snapshots_proxy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the ContentTypeEntriesProxy class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/snapshots/content-type-snapshots-collection

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class ContentTypeSnapshotsProxy(ContentTypeResourceProxy):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/snapshots/content-type-snapshots-collection
    """

    def __init__(self, client, space_id, environment_id, content_type_id):
        self.proxy = self._resource_proxy_class()(client, space_id, environment_id, content_type_id, resource_kind='content_types')

    def _resource_proxy_class(self):
        return SnapshotsProxy

    def create(self, *args, **kwargs):
        """
        Not supported.
        """

        raise Exception("Not Supported")

    def delete(self, *args, **kwargs):
        """
        Not supported.
        """

        raise Exception("Not Supported")

    def __repr__(self):
        return "<{0} space_id='{1}' environment_id='{2}' content_type_id='{3}'>".format(
            self.__class__.__name__,
            self.proxy.space_id,
            self.proxy.environment_id,
            self.proxy.parent_resource_id
        )
