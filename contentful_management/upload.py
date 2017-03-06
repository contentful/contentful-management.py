from .resource import Resource


"""
contentful.Upload
~~~~~~~~~~~~~~~~~~~~~~~

This module implements the Upload class.

API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/uploads

:copyright: (c) 2017 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class Upload(Resource):
    """
    API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/uploads
    """

    def __init__(self, item, **kwargs):
        super(Upload, self).__init__(item, **kwargs)

    @classmethod
    def create_headers(klass, _attributes):
        """Headers for resource creation"""

        return {
            'Content-Type': 'application/octet-stream'
        }

    def __repr__(self):
        return "<Upload id='{0}'>".format(
            self.sys.get('id', '')
        )
