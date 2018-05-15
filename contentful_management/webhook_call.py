from datetime import datetime
import dateutil.parser
from .resource import Resource


"""
contentful_management.webhook_call
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the WebhookCall class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/webhook-calls/webhook-call-overview

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class WebhookCall(Resource):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/webhook-calls/webhook-call-overview
    """

    def __init__(self, item, **kwargs):
        super(WebhookCall, self).__init__(item, **kwargs)
        self.request = item.get('request', {})
        self.response = item.get('response', {})
        self.status_code = item.get('statusCode', -1)
        self.errors = item.get('errors', [])
        self.event_type = item.get('eventType', '')
        self.url = item.get('url', '')
        try:
            self.request_at = dateutil.parser.parse(item.get('requestAt', ''))
        except:
            self.request_at = ''
        try:
            self.response_at = dateutil.parser.parse(item.get('responseAt', ''))
        except:
            self.response_at = ''

    @classmethod
    def base_url(klass, space_id, webhook_id, resource_id=None):
        """
        Returns the URI for the webhook call.
        """

        return "spaces/{0}/webhooks/{1}/calls/{2}".format(
            space_id,
            webhook_id,
            resource_id if resource_id is not None else ''
        )

    def __repr__(self):
        return "<WebhookCall[{0}] id='{1}' url='{2}' request_at='{3}' response_at='{4}'>".format(
            self.status_code,
            self.sys.get('id', ''),
            self.url,
            self.request_at.isoformat() if isinstance(self.request_at, datetime) else 'N/A',
            self.response_at.isoformat() if isinstance(self.request_at, datetime) else 'N/A'
        )
