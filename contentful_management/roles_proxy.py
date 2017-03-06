from .client_proxy import ClientProxy
from .role import Role


class RolesProxy(ClientProxy):
    @property
    def _resource_class(self):
        return Role

    def create(self, attributes=None, **kwargs):
        """Creates a Role with given attributes."""

        return super(RolesProxy, self).create(None, attributes)
