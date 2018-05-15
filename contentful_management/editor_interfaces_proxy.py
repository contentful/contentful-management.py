from .client_proxy import ClientProxy
from .editor_interface import EditorInterface


"""
contentful_management.editor_interfaces_proxy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the EditorInterfacesProxy class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/editor-interface

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class EditorInterfacesProxy(ClientProxy):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/editor-interface
    """

    def __init__(self, client, space_id, environment_id=None, content_type_id=None):
        super(EditorInterfacesProxy, self).__init__(client, space_id, environment_id)
        self.content_type_id = content_type_id

    @property
    def _resource_class(self):
        return EditorInterface

    def all(self):
        """
        Gets the default editor interface.
        """

        return super(EditorInterfacesProxy, self).all()

    def find(self):
        """
        Gets the default editor interface.
        """

        return self.all()

    def default(self):
        """
        Gets the default editor interface.
        """

        return self.all()

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

    def _url(self, **kwargs):
        return self._resource_class.base_url(
            self.space_id,
            self.content_type_id,
            environment_id=self.environment_id
        )

    def __repr__(self):
        return "<{0} space_id='{1}' environment_id='{2}' content_type_id='{3}'>".format(
            self.__class__.__name__,
            self.space_id,
            self.environment_id,
            self.content_type_id
        )
