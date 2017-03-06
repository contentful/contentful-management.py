from .resource import Resource


"""
contentful.locale
~~~~~~~~~~~~~~~~~

This module implements the Locale class.

API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/locales

:copyright: (c) 2017 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class Locale(Resource):
    """
    API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/locales
    """

    def __init__(self, item, **kwargs):
        super(Locale, self).__init__(item, **kwargs)
        self.code = item.get('code', '')
        self.name = item.get('name', '')
        self.fallback_code = item.get('fallbackCode', '')
        self.default = item.get('default', False)
        self.optional = item.get('optional', True)
        self.content_delivery_api = item.get('contentDeliveryApi', True)
        self.content_management_api = item.get('contentManagementApi', True)

    @classmethod
    def update_attributes_map(klass):
        """Attributes for object mapping"""

        return {
            'code': '',
            'name': '',
            'fallback_code': '',
            'default': False,
            'optional': True,
            'content_delivery_api': True,
            'content_management_api': True
        }

    def to_json(self):
        """Returns the JSON Representation of the Resource"""

        result = super(Locale, self).to_json()
        result.update({
            'code': self.code,
            'name': self.name,
            'fallbackCode': self.fallback_code,
            'optional': self.optional,
            'contentDeliveryApi': self.content_delivery_api,
            'contentManagementApi': self.content_management_api
        })
        return result

    def __repr__(self):
        return "<Locale[{0}] code='{1}' default={2}>".format(
            self.name,
            self.code,
            self.default
        )
