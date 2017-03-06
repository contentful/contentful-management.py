from .content_type_resource_proxy import ContentTypeResourceProxy
from .editor_interfaces_proxy import EditorInterfacesProxy


"""
contentful.content_type_editor_interfaces_proxy
~~~~~~~~~~~~~~~~~~~~~~~

This module implements the ContentTypeEditorInterfacesProxy class.

API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/editor-interface

:copyright: (c) 2017 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class ContentTypeEditorInterfacesProxy(ContentTypeResourceProxy):
    """
    API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/editor-interface
    """

    def _resource_proxy_class(self):
        return EditorInterfacesProxy

    def all(self):
        """Gets the Default Editor Interface"""

        return self.proxy.all()

    def find(self, *args, **kwargs):
        """Gets the Default Editor Interface"""

        return self.proxy.find()

    def create(self, **kwargs):
        """Not Supported"""

        raise Exception("Not Supported")

    def delete(self, *args, **kwargs):
        """Not Supported"""

        raise Exception("Not Supported")
