from .client_proxy import ClientProxy
from .tag import Tag

"""
contentful_management.tags_proxy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the TagsProxy class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/tags

:copyright: (c) 2023 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class TagsProxy(ClientProxy):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/tags
    """

    @property
    def _resource_class(self):
        return Tag
