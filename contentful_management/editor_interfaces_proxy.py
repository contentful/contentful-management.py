from .client_proxy import ClientProxy
from .editor_interface import EditorInterface


"""
contentful.editor_interfaces_proxy
~~~~~~~~~~~~~~~~~~~~~~~

This module implements the EditorInterfacesProxy class.

API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/editor-interface

:copyright: (c) 2017 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class EditorInterfacesProxy(ClientProxy):
    """
    API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/editor-interface
    """

    def __init__(self, client, space_id, content_type_id=None):
        super(EditorInterfacesProxy, self).__init__(client, space_id)
        self.content_type_id = content_type_id

    @property
    def _resource_class(self):
        return EditorInterface

    def all(self):
        """
        Gets the default Editor Interface.
        """

        return super(EditorInterfacesProxy, self).all()

    def find(self):
        """
        Gets the default Editor Interface.
        """

        return self.all()

    def create(self, *args, **kwargs):
        """Not Supported"""

        raise Exception("Not Supported")

    def delete(self, *args, **kwargs):
        """Not Supported"""

        raise Exception("Not Supported")

    def _url(self, **kwargs):
        return self._resource_class.base_url(self.space_id, self.content_type_id)

    def __repr__(self):
        return "<{0} space_id='{1}' content_type_id='{2}'>".format(
            self.__class__.__name__,
            self.space_id,
            self.content_type_id
        )
