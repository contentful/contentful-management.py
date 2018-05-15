from .webhook_resource_proxy import WebhookResourceProxy
from .webhooks_call_proxy import WebhooksCallProxy


"""
contentful_management.webhook_webhooks_call_proxy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the WebhookWebhooksCallProxy class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/webhook-calls

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class WebhookWebhooksCallProxy(WebhookResourceProxy):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/webhook-calls
    """

    def _resource_proxy_class(self):
        return WebhooksCallProxy
