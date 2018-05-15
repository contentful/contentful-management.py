from .client_proxy import ClientProxy
from .webhook_call import WebhookCall


"""
contentful_management.webhooks_call_proxy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the WebhooksCallProxy class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/webhook-calls/webhook-call-overview

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class WebhooksCallProxy(ClientProxy):
    def __init__(self, client, space_id, webhook_id):
        super(WebhooksCallProxy, self).__init__(client, space_id)
        self.webhook_id = webhook_id

    @property
    def _resource_class(self):
        return WebhookCall

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

    def _url(self, resource_id='', **kwargs):
        return self._resource_class.base_url(
            self.space_id,
            self.webhook_id,
            resource_id=resource_id
        )

    def __repr__(self):
        return "<{0} space_id='{1}' webhook_id='{2}'>".format(
            self.__class__.__name__,
            self.space_id,
            self.webhook_id
        )
