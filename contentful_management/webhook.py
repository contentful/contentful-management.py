from .resource import Resource


"""
contentful.Webhook
~~~~~~~~~~~~~~~~~~~~~~~

This module implements the Webhook class.

API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/webhooks

:copyright: (c) 2017 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class Webhook(Resource):
    """
    API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/webhooks
    """

    def __init__(self, item, **kwargs):
        super(Webhook, self).__init__(item, **kwargs)
        self.name = item.get('name', '')
        self.url = item.get('url', '')
        self.topics = item.get('topics', [])
        self.http_basic_username = item.get('httpBasicUsername', '')
        self.headers = item.get('headers', [])

    @classmethod
    def update_attributes_map(klass):
        """Defines keys and default values for non-generic attributes"""

        return {
            'name': '',
            'url': '',
            'topics': [],
            'http_basic_username': '',
            'headers': []
        }

    @classmethod
    def create_attributes(klass, attributes, previous_object=None):
        """Attributes for resource creation"""

        result = super(Webhook, klass).create_attributes(attributes, previous_object)

        if 'topics' not in result:
            raise Exception("Topics ('topics') must be provided for this operation.")
        return result

    def to_json(self):
        """Returns the JSON Representation of the Resource"""

        result = super(Webhook, self).to_json()
        result.update({
            'name': self.name,
            'url': self.url,
            'topics': self.topics,
            'httpBasicUsername': self.http_basic_username,
            'headers': self.headers
        })
        return result

    def __repr__(self):
        return "<Webhook[{0}] id='{1}'>".format(
            self.name,
            self.sys.get('id', '')
        )
