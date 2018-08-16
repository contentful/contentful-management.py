from .resource import Resource, EnvironmentAwareResource
from copy import deepcopy


"""
contentful_management.ui_extension
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the UIExtension class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/ui-extensions

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class UIExtension(Resource, EnvironmentAwareResource):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/ui-extensions
    """

    def __init__(self, item, **kwargs):
        super(UIExtension, self).__init__(item, **kwargs)
        self.extension = deepcopy(item.get('extension', {}))

    @property
    def source(self):
        return self.extension.get('src', '') or self.extension.get('srcdoc', '')

    @source.setter
    def source(self, value):
        key = 'src' if value.startswith('http') else 'srcdoc'
        self.extension[key] = value

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

    @property
    def parameters(self):
        return self.extension.get('parameters', {})

    @parameters.setter
    def parameters(self, value):
        self.extension['parameters'] = value

    @classmethod
    def update_attributes_map(klass):
        """
        Defines keys and default values for non-generic attributes.
        """

        return {
            'extension': {}
        }

    def to_json(self):
        """
        Returns the JSON Representation of the UI extension.
        """

        result = super(UIExtension, self).to_json()
        result.update({
            'extension': self.extension
        })

        return result

    def __repr__(self):
        return "<UIExtension[{0}] id='{1}' field_types=[{2}]>".format(
            self.name,
            self.sys.get('id', ''),
            ', '.join(
                "'{0}'".format(t)
                for t in [
                    ft['type']
                    for ft in self.field_types
                ]
            )
        )
