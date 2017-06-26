from .webhook_resource_proxy import WebhookResourceProxy
from .webhooks_health_proxy import WebhooksHealthProxy


"""
contentful.webhooks_health_proxy
~~~~~~~~~~~~~~~~~~~~~~~

This module implements the WebhookWebhooksHealthProxy class.

API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/webhook-calls/webhook-health

:copyright: (c) 2017 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class WebhookWebhooksHealthProxy(WebhookResourceProxy):
    """
    API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/webhook-calls/webhook-health
    """

    def _resource_proxy_class(self):
        return WebhooksHealthProxy

    def find(self, *args, **kwargs):
        """
        Gets Webhook Health.
        """

        return self.all()
