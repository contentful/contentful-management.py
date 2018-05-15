from .content_type_resource_proxy import ContentTypeResourceProxy
from .editor_interfaces_proxy import EditorInterfacesProxy


"""
contentful_management.content_type_editor_interfaces_proxy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the ContentTypeEditorInterfacesProxy class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/editor-interface

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class ContentTypeEditorInterfacesProxy(ContentTypeResourceProxy):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/editor-interface
    """

    def _resource_proxy_class(self):
        return EditorInterfacesProxy

    def all(self):
        """
        Gets the default editor interface.
        """

        return self.proxy.all()

    def find(self, *args, **kwargs):
        """
        Gets the default editor interface.
        """

        return self.proxy.find()

    def default(self):
        """
        Gets the default editor interface.
        """

        return self.proxy.default()

    def create(self, **kwargs):
        """
        Not supported.
        """

        raise Exception("Not Supported")

    def delete(self, *args, **kwargs):
        """
        Not supported.
        """

        raise Exception("Not Supported")
