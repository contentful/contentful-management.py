# Classes imported here are meant to be used via globals() on build
from .entry import Entry  # noqa: F401
from .asset import Asset  # noqa: F401
from .space import Space  # noqa: F401
from .content_type import ContentType  # noqa: F401
from .webhook import Webhook  # noqa: F401
from .locale import Locale  # noqa: F401
from .role import Role  # noqa: F401
from .editor_interface import EditorInterface  # noqa: F401
from .api_key import ApiKey  # noqa: F401
from .snapshot import Snapshot  # noqa: F401
from .upload import Upload  # noqa: F401


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
        return [self._build_item(item) for item in self.json['items']]

    def _build_item(self, item):
        buildables = [
            'Entry',
            'Asset',
            'ContentType',
            'Space',
            'ApiKey',
            'Locale',
            'EditorInterface',
            'Webhook',
            'Role',
            'Snapshot',
            'Upload'
        ]

        item_type = item['sys']['type']

        if item_type == 'WebhookDefinition':
            item_type = 'Webhook'

        if item_type in buildables:
            return globals()[item_type](
                item,
                default_locale=self.default_locale,
                client=self.client
            )
