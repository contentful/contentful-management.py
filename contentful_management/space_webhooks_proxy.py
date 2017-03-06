from .space_resource_proxy import SpaceResourceProxy
from .webhooks_proxy import WebhooksProxy


"""
contentful.space_webhooks_proxy
~~~~~~~~~~~~~~~~~~~~~~~

This module implements the SpaceWebhooksProxy class.

API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/webhooks

:copyright: (c) 2017 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class SpaceWebhooksProxy(SpaceResourceProxy):
    """
    API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/webhooks
    """

    def _resource_proxy_class(self):
        return WebhooksProxy
