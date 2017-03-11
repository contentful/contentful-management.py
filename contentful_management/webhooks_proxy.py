from .client_proxy import ClientProxy
from .webhook import Webhook


"""
contentful.webhooks_proxy
~~~~~~~~~~~~~~~~~~~~~~~

This module implements the WebhooksProxy class.

API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/webhooks

:copyright: (c) 2017 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class WebhooksProxy(ClientProxy):
    """
    API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/webhooks
    """

    @property
    def _resource_class(self):
        return Webhook

    def create(self, attributes=None, **kwargs):
        """Creates a Webhook with given attributes."""

        return super(WebhooksProxy, self).create(resource_id=None, attributes=attributes)
