from .client_proxy import ClientProxy
from .ui_extension import UIExtension


class UIExtensionsProxy(ClientProxy):
    @property
    def _resource_class(self):
        return UIExtension
