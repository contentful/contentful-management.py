from .space_resource_proxy import SpaceResourceProxy
from .uploads_proxy import UploadsProxy


"""
contentful.space_uploads_proxy
~~~~~~~~~~~~~~~~~~~~~~~

This module implements the SpaceUploadsProxy class.

API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/uploads

:copyright: (c) 2017 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class SpaceUploadsProxy(SpaceResourceProxy):
    """
    API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/uploads
    """

    def _resource_proxy_class(self):
        return UploadsProxy
