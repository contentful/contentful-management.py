from .client_proxy import ClientProxy
from .space import Space


"""
contentful_management.spaces_proxy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the SpacesProxy class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/spaces

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class SpacesProxy(ClientProxy):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/spaces
    """

    def __init__(self, client):
        super(SpacesProxy, self).__init__(client, None)

    def __repr__(self):
        return "<SpacesProxy>"

    @property
    def _resource_class(self):
        return Space

    def all(self, query=None, **kwargs):
        """
        Gets all spaces.
        """

        return super(SpacesProxy, self).all(query=query)

    def find(self, space_id, query=None, **kwargs):
        """
        Gets a space by ID.
        """

        try:
            self.space_id = space_id
            return super(SpacesProxy, self).find(space_id, query=query)
        finally:
            self.space_id = None

    def create(self, attributes=None, **kwargs):
        """
        Creates a space with given attributes.
        """

        if attributes is None:
            attributes = {}
        if 'default_locale' not in attributes:
            attributes['default_locale'] = self.client.default_locale

        return super(SpacesProxy, self).create(resource_id=None, attributes=attributes)

    def delete(self, space_id):
        """
        Deletes a space by ID.
        """

        try:
            self.space_id = space_id
            return super(SpacesProxy, self).delete(space_id)
        finally:
            self.space_id = None
