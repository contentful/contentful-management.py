"""
contentful_management.webhook_resource_proxy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the WebhookResourceProxy class.

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class WebhookResourceProxy(object):
    """Base Class for Webhook related Resource Proxies"""

    def __init__(self, client, space_id, webhook_id):
        self.proxy = self._resource_proxy_class()(client, space_id, webhook_id)

    def __repr__(self):
        return "<{0} space_id='{1}' webhook_id='{2}'>".format(
            self.__class__.__name__,
            self.proxy.space_id,
            self.proxy.webhook_id
        )

    def _resource_proxy_class(self):
        raise Exception("Must implement")

    def all(self, query=None):
        """
        Gets all resources related to the current webhook.
        """

        return self.proxy.all(query)

    def find(self, resource_id, query=None):
        """
        Finds a single resource by ID related to the current webhook.
        """

        return self.proxy.find(resource_id, query)

    def create(self, resource_id=None, attributes=None):
        """
        Not supported.
        """

        raise Exception("Not Supported")

    def delete(self, resource_id):
        """
        Not supported.
        """

        raise Exception("Not Supported")
