from .resource import Resource, PublishResource, EnvironmentAwareResource
from .content_type_field import ContentTypeField
from .content_type_entries_proxy import ContentTypeEntriesProxy
from .content_type_snapshots_proxy import ContentTypeSnapshotsProxy
from .content_type_editor_interfaces_proxy import ContentTypeEditorInterfacesProxy


"""
contentful_management.content_type
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the ContentType class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/content-types

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class ContentType(Resource, PublishResource, EnvironmentAwareResource):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/content-types
    """

    def __init__(self, item, **kwargs):
        super(ContentType, self).__init__(item, **kwargs)
        self.name = item.get('name', '')
        self.description = item.get('description', '')
        self.display_field = item.get('displayField', '')
        self.fields = [ContentTypeField(field)
                       for field in item.get('fields', [])]

    @classmethod
    def base_url(klass, space_id, resource_id=None, public=False, environment_id=None, **kwargs):
        """
        Returns the URI for the content type.
        """

        if public:
            environment_slug = ""
            if environment_id is not None:
                environment_slug = "/environments/{0}".format(environment_id)
            return "spaces/{0}{1}/public/content_types".format(space_id, environment_slug)
        return super(ContentType, klass).base_url(
            space_id,
            resource_id=resource_id,
            environment_id=environment_id,
            **kwargs
        )

    @classmethod
    def create_attributes(klass, attributes, previous_object=None):
        """
        Attributes for content type creation.
        """

        result = super(ContentType, klass).create_attributes(attributes, previous_object)

        if 'fields' not in result:
            result['fields'] = []
        return result

    @classmethod
    def update_attributes_map(klass):
        """
        Attributes for object mapping.
        """

        return {
            'name': '',
            'description': '',
            'display_field': '',
            'fields': []
        }

    def to_json(self):
        """
        Returns the JSON representation of the content type.
        """

        result = super(ContentType, self).to_json()
        result.update({
            'name': self.name,
            'description': self.description,
            'displayField': self.display_field,
            'fields': [f.to_json() for f in self.fields]
        })
        return result

    def entries(self):
        """
        Provides access to entry management methods for the given content type.

        API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/entries

        :return: :class:`ContentTypeEntriesProxy <contentful_management.content_type_entries_proxy.ContentTypeEntriesProxy>` object.
        :rtype: contentful.content_type_entries_proxy.ContentTypeEntriesProxy

        Usage:

            >>> content_type_entries_proxy = content_type.entries()
            <ContentTypeEntriesProxy space_id="cfexampleapi" environment_id="master" content_type_id="cat">
        """
        return ContentTypeEntriesProxy(self._client, self.space.id, self._environment_id, self.id)

    def editor_interfaces(self):
        """
        Provides access to editor interface management methods for the given content type.

        API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/editor-interface

        :return: :class:`ContentTypeEditorInterfacesProxy <contentful_management.content_type_editor_interfaces_proxy.ContentTypeEditorInterfacesProxy>` object.
        :rtype: contentful.content_type_editor_interfaces_proxy.ContentTypeEditorInterfacesProxy

        Usage:

            >>> content_type_editor_interfaces_proxy = content_type.editor_interfaces()
            <ContentTypeEditorInterfacesProxy space_id="cfexampleapi" environment_id="master" content_type_id="cat">
        """
        return ContentTypeEditorInterfacesProxy(self._client, self.space.id, self._environment_id, self.id)

    def snapshots(self):
        """
        Provides access to snapshot management methods for the given content type.

        API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/snapshots/content-type-snapshots-collection

        :return: :class:`ContentTypeSnapshotsProxy <contentful_management.content_type_snapshots_proxy.ContentTypeSnapshotsProxy>` object.
        :rtype: contentful.content_type_snapshots_proxy.ContentTypeSnapshotsProxy

        Usage:

            >>> content_type_snapshots_proxy = content_type.entries()
            <ContentTypeSnapshotsProxy space_id="cfexampleapi" environment_id="master" content_type_id="cat">
        """
        return ContentTypeSnapshotsProxy(self._client, self.space.id, self._environment_id, self.id)

    def __repr__(self):
        return "<ContentType[{0}] id='{1}'>".format(
            self.name,
            self.sys.get('id', '')
        )
