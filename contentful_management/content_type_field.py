from .utils import snake_case
from .content_type_field_types import *  # noqa: F401
from .content_type_field_validation import ContentTypeFieldValidation

"""
contentful.content_type_field
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the ContentTypeField class.

API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/content-types/content-type

:copyright: (c) 2017 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class ContentTypeField(object):
    """
    API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/content-types/content-type
    """

    def __init__(self, field_data):
        self.raw = field_data
        self.id = snake_case(field_data.get('id', ''))
        self.name = field_data.get('name', '')
        self.type = field_data.get('type', '')
        self.link_type = field_data.get('linkType', '')
        self.items = field_data.get('items', {})
        self.localized = field_data.get('localized', False)
        self.omitted = field_data.get('omitted', False)
        self.required = field_data.get('required', False)
        self.disabled = field_data.get('disabled', False)
        self.validations = [ContentTypeFieldValidation(v)
                            for v in field_data.get('validations', [])]
        self._coercion = self._get_coercion()

    def to_json(self):
        """Returns the JSON Representation of the Resource"""

        result = {
            'name': self.name,
            'id': self.id,
            'type': self.type,
            'localized': self.localized,
            'omitted': self.omitted,
            'required': self.required,
            'disabled': self.disabled,
            'validations': [v.to_json() for v in self.validations]
        }

        if self.type == 'Array':
            result['items'] = self.items

        if self.type == 'Link':
            result['linkType'] = self.link_type

        return result

    def coerce(self, value):
        """Coerces the value to the proper type."""

        return self._coercion.coerce(value)

    def _get_coercion(self):
        """Gets the proper coercion type"""

        return globals()["{0}Field".format(self.type)](self.items)

    def __repr__(self):
        return "<ContentTypeField[{0}] id='{1}' type='{2}'>".format(
            self.name,
            self.id,
            self.type
        )
