from .resource import Resource


"""
contentful.ui_extension
~~~~~~~~~~~~~~~~~~~~~~~

This module implements the UIExtension class.

API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/ui-extensions

:copyright: (c) 2017 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class UIExtension(Resource):
    """
    API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/ui-extensions
    """

    def __init__(self, item, **kwargs):
        super(UIExtension, self).__init__(item, **kwargs)
        self.extension = item.get('extension', {})

    @property
    def source(self):
        return self.extension.get('src', '')

    @source.setter
    def source(self, value):
        self.extension['src'] = value

    @property
    def name(self):
        return self.extension.get('name', '')

    @name.setter
    def name(self, value):
        self.extension['name'] = value

    @property
    def field_types(self):
        return self.extension.get('fieldTypes', [])

    @field_types.setter
    def field_types(self, value):
        self.extension['fieldTypes'] = value

    @property
    def sidebar(self):
        return self.extension.get('sidebar', False)

    @sidebar.setter
    def sidebar(self, value):
        self.extension['sidebar'] = value

    @classmethod
    def update_attributes_map(klass):
        """Defines keys and default values for non-generic attributes"""

        return {
            'extension': {}
        }

    def to_json(self):
        """Returns the JSON Representation of the Resource"""

        result = super(UIExtension, self).to_json()
        result.update({
            'extension': self.extension
        })
        return result

    def __repr__(self):
        return "<UIExtension[{0}] id='{1}'>".format(
            self.name,
            self.sys.get('id', '')
        )