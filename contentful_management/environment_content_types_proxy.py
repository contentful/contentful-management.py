from .environment_resource_proxy import EnvironmentResourceProxy
from .content_types_proxy import ContentTypesProxy


"""
contentful_management.environment_content_types_proxy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the EnvironmentContentTypesProxy class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/content-types

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class EnvironmentContentTypesProxy(EnvironmentResourceProxy):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/content-types
    """

    def _resource_proxy_class(self):
        return ContentTypesProxy
