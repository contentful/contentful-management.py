from .client_proxy import ClientProxy
from .content_type import ContentType


"""
contentful_management.content_types_proxy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the ContentTypesProxy class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/editor-interface

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class ContentTypesProxy(ClientProxy):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/content-types/content-type
    """

    @property
    def _resource_class(self):
        return ContentType

    def all_published(self):
        """
        Gets all the published content types for a space.

        API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/content-types/activated-content-type-collection
        """

        return self.client._get(
            self._url(public=True)
        )

    def _url(self, resource_id='', **kwargs):
        return self._resource_class.base_url(self.space_id, resource_id=resource_id, environment_id=self.environment_id, **kwargs)
