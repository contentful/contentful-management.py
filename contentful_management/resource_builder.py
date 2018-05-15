from .role import Role
from .user import User
from .entry import Entry
from .array import Array
from .asset import Asset
from .space import Space
from .locale import Locale
from .upload import Upload
from .api_key import ApiKey
from .webhook import Webhook
from .snapshot import Snapshot
from .environment import Environment
from .ui_extension import UIExtension
from .content_type import ContentType
from .webhook_call import WebhookCall
from .organization import Organization
from .webhook_health import WebhookHealth
from .preview_api_key import PreviewApiKey
from .editor_interface import EditorInterface
from .space_membership import SpaceMembership
from .personal_access_token import PersonalAccessToken


"""
contentful_management.resource_builder
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the ResourceBuilder class.

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class ResourceBuilder(object):
    """
    Creates objects of the proper resource type.
    """

    def __init__(self, client, default_locale, json):
        self.client = client
        self.default_locale = default_locale
        self.json = json

    def build(self):
        """
        Creates the objects from the JSON response.
        """

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
            'SpaceMembership': SpaceMembership,
            'Organization': Organization,
            'ApiKey': ApiKey,
            'PreviewApiKey': PreviewApiKey,
            'PersonalAccessToken': PersonalAccessToken,
            'Locale': Locale,
            'EditorInterface': EditorInterface,
            'WebhookDefinition': Webhook,
            'WebhookCallOverview': WebhookCall,
            'WebhookCallDetails': WebhookCall,
            'Webhook': WebhookHealth,
            'Role': Role,
            'Extension': UIExtension,
            'Snapshot': Snapshot,
            'Upload': Upload,
            'User': User,
            'Environment': Environment
        }

        item_type = item['sys']['type']

        if item_type in buildables:
            return buildables[item_type](
                item,
                default_locale=self.default_locale,
                client=self.client
            )
        raise Exception("Resource not buildable")
