from .space_resource_proxy import SpaceResourceProxy
from .webhooks_proxy import WebhooksProxy


"""
contentful_management.space_webhooks_proxy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the SpaceWebhooksProxy class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/webhooks

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class SpaceWebhooksProxy(SpaceResourceProxy):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/webhooks
    """

    def _resource_proxy_class(self):
        return WebhooksProxy

    def create(self, attributes=None, **kwargs):
        """
        Creates a webhook with given attributes.
        """

        return super(SpaceWebhooksProxy, self).create(None, attributes)
