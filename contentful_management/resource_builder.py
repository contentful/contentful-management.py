from .entry import Entry
from .asset import Asset
from .space import Space
from .content_type import ContentType
from .webhook import Webhook
from .locale import Locale
from .role import Role
from .editor_interface import EditorInterface
from .api_key import ApiKey
from .snapshot import Snapshot
from .upload import Upload
from .array import Array


"""
contentful.resource_builder
~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the Resource Builder class.

:copyright: (c) 2016 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class ResourceBuilder(object):
    """Creates objects of the proper Resource Type"""

    def __init__(self, client, default_locale, json):
        self.client = client
        self.default_locale = default_locale
        self.json = json

    def build(self):
        """Creates the objects from the JSON response"""

        if self.json['sys']['type'] == 'Array':
            return self._build_array()
        return self._build_item(self.json)

    def _build_array(self):
        return Array(self.json, [self._build_item(item) for item in self.json['items']])

    def _build_item(self, item):
        buildables = {
            'Entry': Entry,
            'Asset': Asset,
            'ContentType': ContentType,
            'Space': Space,
            'ApiKey': ApiKey,
            'Locale': Locale,
            'EditorInterface': EditorInterface,
            'WebhookDefinition': Webhook,
            'Role': Role,
            'Snapshot': Snapshot,
            'Upload': Upload
        }

        item_type = item['sys']['type']

        if item_type in buildables:
            return buildables[item_type](
                item,
                default_locale=self.default_locale,
                client=self.client
            )
