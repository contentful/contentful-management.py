from .client_proxy import ClientProxy
from .snapshot import Snapshot


"""
contentful_management.snapshots_proxy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the SnapshotsProxy class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/snapshots

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class SnapshotsProxy(ClientProxy):
    def __init__(self, client, space_id, environment_id, parent_resource_id, resource_kind='entries'):
        super(SnapshotsProxy, self).__init__(client, space_id, environment_id=environment_id)
        self.parent_resource_id = parent_resource_id
        self.resource_kind = resource_kind

    @property
    def _resource_class(self):
        return Snapshot

    def create(*args, **kwargs):
        """
        Not supported.
        """

        raise Exception("Not Supported")

    def delete(*args, **kwargs):
        """
        Not supported.
        """

        raise Exception("Not Supported")

    def _url(self, resource_id='', **kwargs):
        return self._resource_class.base_url(
            self.space_id,
            self.parent_resource_id,
            environment_id=self.environment_id,
            resource_url=self.resource_kind,
            resource_id=resource_id
        )

    def __repr__(self):
        return "<{0}[{1}] space_id='{2}' environment_id='{3}' parent_resource_id='{4}'>".format(
            self.__class__.__name__,
            self.resource_kind,
            self.space_id,
            self.environment_id,
            self.parent_resource_id
        )
