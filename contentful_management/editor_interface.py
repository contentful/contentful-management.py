from .resource import Resource


"""
contentful_management.editor_interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the EditorInterface class.

API reference: https://www.contentful.com/developers/docs/references/content-delivery-api/#/reference/editor-interfaces

:copyright: (c) 2017 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class EditorInterface(Resource):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-delivery-api/#/reference/editor-interfaces
    """

    def __init__(self, item, **kwargs):
        super(EditorInterface, self).__init__(item, **kwargs)
        self.controls = item.get('controls', [])

    @classmethod
    def base_url(self, space_id, content_type_id, **kwargs):
        """
        Returns the URI for the editor interface.
        """

        return "spaces/{0}/content_types/{1}/editor_interface".format(
            space_id,
            content_type_id
        )

    @classmethod
    def update_attributes_map(klass):
        """
        Attributes for object mapping.
        """

        return {'controls': []}

    def to_json(self):
        """
        Returns the JSON representation of the editor interface.
        """

        result = super(EditorInterface, self).to_json()
        result.update({'controls': self.controls})
        return result

    def _update_url(self):
        return self.__class__.base_url(
            self.space.id,
            self.content_type.id
        )

    def __repr__(self):
        return "<EditorInterface id='{0}'>".format(
            self.sys.get('id', '')
        )
