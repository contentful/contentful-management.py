from .client_proxy import ClientProxy
from .content_type import ContentType


"""
contentful.content_types_proxy
~~~~~~~~~~~~~~~~~~~~~~~

This module implements the ContentTypesProxy class.

API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/editor-interface

:copyright: (c) 2017 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class ContentTypesProxy(ClientProxy):
    """
    API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/content-types/content-type
    """

    @property
    def _resource_class(self):
        return ContentType

    def all_published(self):
        """
        Gets all the Published Content Types for a Space.

        API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/content-types/activated-content-type-collection
        """

        return self.client._get(
            self._url(public=True)
        )
