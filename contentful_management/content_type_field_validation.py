from .utils import snake_case, camel_case


"""
contentful.content_type_field_validation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the ContentTypeFieldValidation class.

API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/content-types/content-type

:copyright: (c) 2016 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class ContentTypeFieldValidation(object):
    """
    API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/content-types/content-type
    """

    def __init__(self, validation_data):
        self.raw = validation_data
        self._data = {}
        for k, v in validation_data.items():
            self._data[snake_case(k)] = v

    def to_json(self):
        """Returns the JSON Representation of the Resource"""

        result = {}
        for k, v in self._data.items():
            result[camel_case(k)] = v
        return result

    def __getattr__(self, name):
        if name in self._data:
            return self._data[name]
        return super(ContentTypeFieldValidation, self).__getattr__(name)

    def __setattr__(self, name, value):
        if name not in ['raw', '_data']:
            self._data[name] = value
        super(ContentTypeFieldValidation, self).__setattr__(name, value)

    def __repr__(self):
        return "<ContentTypeFieldValidation {0}>".format(
            " ".join(
                ["{0}='{1}'".format(k, v)
                 for k, v in self._data.items()]
            )
        )
