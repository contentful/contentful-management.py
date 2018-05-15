from .client_proxy import ClientProxy
from .webhook import Webhook


"""
contentful_management.webhooks_proxy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the WebhooksProxy class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/webhooks

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class WebhooksProxy(ClientProxy):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/webhooks
    """

    @property
    def _resource_class(self):
        return Webhook

    def create(self, attributes=None, **kwargs):
        """
        Creates a webhook with given attributes.
        """

        return super(WebhooksProxy, self).create(resource_id=None, attributes=attributes)
