from .client_proxy import ClientProxy
from .webhook_health import WebhookHealth


"""
contentful_management.webhooks_health_proxy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the WebhooksHealthProxy class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/webhook-calls/webhook-health

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class WebhooksHealthProxy(ClientProxy):
    def __init__(self, client, space_id, webhook_id):
        super(WebhooksHealthProxy, self).__init__(client, space_id)
        self.webhook_id = webhook_id

    @property
    def _resource_class(self):
        return WebhookHealth

    def find(self, *args, **kwargs):
        """
        Gets the webhook health.
        """

        return self.all()

    def create(self, *args, **kwargs):
        """
        Not supported.
        """

        raise Exception("Not Supported")

    def delete(self, *args, **kwargs):
        """
        Not supported.
        """

        raise Exception("Not Supported")

    def _url(self, **kwargs):
        return self._resource_class.base_url(
            self.space_id,
            self.webhook_id
        )

    def __repr__(self):
        return "<{0} space_id='{1}' webhook_id='{2}'>".format(
            self.__class__.__name__,
            self.space_id,
            self.webhook_id
        )
