from .resource import Resource, PublishResource
from .content_type_field import ContentTypeField
from .content_type_entries_proxy import ContentTypeEntriesProxy
from .content_type_editor_interfaces_proxy import ContentTypeEditorInterfacesProxy


"""
contentful.content_type
~~~~~~~~~~~~~~~~~~~~~~~

This module implements the ContentType class.

API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/content-types

:copyright: (c) 2017 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class ContentType(Resource, PublishResource):
    """
    API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/content-types
    """

    def __init__(self, item, **kwargs):
        super(ContentType, self).__init__(item, **kwargs)
        self.name = item.get('name', '')
        self.description = item.get('description', '')
        self.display_field = item.get('displayField', '')
        self.fields = [ContentTypeField(field)
                       for field in item.get('fields', [])]

    @classmethod
    def base_url(klass, space_id, resource_id=None, public=False, **kwargs):
        """Returns the URI for the Resource"""

        if public:
            return "spaces/{0}/public/content_types".format(space_id)
        return super(ContentType, klass).base_url(
            space_id,
            resource_id=resource_id,
            **kwargs
        )

    @classmethod
    def create_attributes(klass, attributes, previous_object=None):
        """Attributes for resource creation"""

        result = super(ContentType, klass).create_attributes(attributes, previous_object)

        if 'fields' not in result:
            result['fields'] = []
        return result

    @classmethod
    def update_attributes_map(klass):
        """Attributes for object mapping"""

        return {
            'name': '',
            'description': '',
            'display_field': '',
            'fields': []
        }

    def to_json(self):
        """Returns the JSON Representation of the Resource"""

        result = super(ContentType, self).to_json()
        result.update({
            'name': self.name,
            'description': self.description,
            'displayField': self.display_field,
            'fields': [f.to_json() for f in self.fields]
        })
        return result

    def entries(self):
        """Provides access to Entries management methods for the given Content Type

        API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/entries

        :return: :class:`ContentTypeEntriesProxy <contentful_management.content_type_entries_proxy.ContentTypeEntriesProxy>` object.
        :rtype: contentful.content_type_entries_proxy.ContentTypeEntriesProxy

        Usage:

            >>> content_type_entries_proxy = content_type.entries()
            <ContentTypeEntriesProxy space_id="cfexampleapi" content_type_id="cat">
        """
        return ContentTypeEntriesProxy(self._client, self.space.id, self.id)

    def editor_interfaces(self):
        """Provides access to Editor Interfaces management methods for the given Content Type

        API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/editor-interface

        :return: :class:`ContentTypeEditorInterfacesProxy <contentful_management.content_type_editor_interfaces_proxy.ContentTypeEditorInterfacesProxy>` object.
        :rtype: contentful.content_type_editor_interfaces_proxy.ContentTypeEditorInterfacesProxy

        Usage:

            >>> content_type_editor_interfaces_proxy = content_type.editor_interfaces()
            <ContentTypeEditorInterfacesProxy space_id="cfexampleapi" content_type_id="cat">
        """
        return ContentTypeEditorInterfacesProxy(self._client, self.space.id, self.id)

    def __repr__(self):
        return "<ContentType[{0}] id='{1}'>".format(
            self.name,
            self.sys.get('id', '')
        )
