from .resource import Resource, Link


"""
contentful_management.preview_api_key
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the PreviewApiKey class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/api-keys/preview-api-key/get-a-single-preview-api-key

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class PreviewApiKey(Resource):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/api-keys/preview-api-key/get-a-single-preview-api-key
    """

    def __init__(self, item, **kwargs):
        super(PreviewApiKey, self).__init__(item, **kwargs)
        self.name = item.get('name', '')
        self.description = item.get('description', '')
        self.access_token = item.get('accessToken', '')
        self.environments = [Link(e, **kwargs) for e in item.get('environments', [])]

    def __repr__(self):
        return "<PreviewApiKey[{0}] id='{1}' access_token='{2}'>".format(
            self.name,
            self.sys.get('id', ''),
            self.access_token
        )
