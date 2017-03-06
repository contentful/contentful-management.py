from .resource import Resource


"""
contentful.editor_interface
~~~~~~~~~~~~~~~~~~~~~~~

This module implements the EditorInterface class.

API Reference: https://www.contentful.com/developers/docs/references/content-delivery-api/#/reference/editor-interfaces

:copyright: (c) 2016 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class EditorInterface(Resource):
    """
    API Reference: https://www.contentful.com/developers/docs/references/content-delivery-api/#/reference/editor-interfaces
    """

    def __init__(self, item, **kwargs):
        super(EditorInterface, self).__init__(item, **kwargs)
        self.controls = item.get('controls', [])

    @classmethod
    def base_url(self, space_id, content_type_id, **kwargs):
        """URL Handler"""

        return "spaces/{0}/content_types/{1}/editor_interface".format(
            space_id,
            content_type_id
        )

    @classmethod
    def update_attributes_map(klass):
        """Attributes for object mapping"""

        return {'controls': []}

    def to_json(self):
        """Returns the JSON Representation of the Resource"""

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
