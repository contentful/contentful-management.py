from .client_proxy import ClientProxy
from .snapshot import Snapshot


class SnapshotsProxy(ClientProxy):
    def __init__(self, client, space_id, entry_id):
        super(SnapshotsProxy, self).__init__(client, space_id)
        self.entry_id = entry_id

    @property
    def _resource_class(self):
        return Snapshot

    def create(*args, **kwargs):
        """Not Supported"""

        raise Exception("Not Supported")

    def delete(*args, **kwargs):
        """Not Supported"""

        raise Exception("Not Supported")

    def _url(self, resource_id='', **kwargs):
        return self._resource_class.base_url(
            self.space_id,
            self.entry_id,
            resource_id=resource_id
        )

    def __repr__(self):
        return "<{0} space_id='{1}' entry_id='{2}'>".format(
            self.__class__.__name__,
            self.space_id,
            self.entry_id
        )
