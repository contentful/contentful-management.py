from .entry_resource_proxy import EntryResourceProxy
from .snapshots_proxy import SnapshotsProxy


"""
contentful_management.entry_snapshots_proxy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the EntrySnapshotsProxy class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/snapshots

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class EntrySnapshotsProxy(EntryResourceProxy):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/snapshots
    """
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
