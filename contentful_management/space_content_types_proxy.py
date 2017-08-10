from .space_resource_proxy import SpaceResourceProxy
from .content_types_proxy import ContentTypesProxy


"""
contentful_management.space_content_types_proxy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the SpaceContentTypesProxy class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/content-types

:copyright: (c) 2017 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class SpaceContentTypesProxy(SpaceResourceProxy):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/content-types
    """

    def _resource_proxy_class(self):
        return ContentTypesProxy
