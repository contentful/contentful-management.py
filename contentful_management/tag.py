from .resource import Resource

"""
contentful_management.tag
~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the Tag class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/tags

:copyright: (c) 2023 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class Tag(Resource):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/tags
    """

    def __init__(self, item, **kwargs):
        super(Tag, self).__init__(item, **kwargs)
        self.name = item.get('name', '')

    def delete(self):
        """
        Deletes this tag.
        """
        return self._client._delete(
            self.__class__.base_url(
                space_id=self.space.id,
                resource_id=self.sys['id'],
                environment_id=self._environment_id,
            ),
            headers=self._update_headers()
        )

    def to_json(self):
        """
        Returns the JSON representation of the tag.
        """

        result = super(Tag, self).to_json()
        result.update({
            'name': self.name
        })
        return result

    def __repr__(self):
        return "<Tag id='{0}' name='{1}'>".format(
            self.sys.get('id', ''),
            self.name
        )
