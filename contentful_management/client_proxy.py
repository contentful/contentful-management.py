"""
contentful.client_proxy
~~~~~~~~~~~~~~~~

This module implements the ClientProxy class.

:copyright: (c) 2017 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class ClientProxy(object):
    """Base Class for Proxies"""

    def __init__(self, client, space_id):
        self.client = client
        self.space_id = space_id

    def __repr__(self):
        return "<{0} space_id='{1}'>".format(
            self.__class__.__name__,
            self.space_id
        )

    @property
    def _resource_class(self):
        raise Exception("Must Implement")

    def all(self, query=None):
        """Gets resource collection for _resource_class"""

        if query is None:
            query = {}
        return self.client._get(
            self._url(),
            query
        )

    def find(self, resource_id, query=None, **kwargs):
        """Gets a single resource"""

        if query is None:
            query = {}
        return self.client._get(
            self._url(resource_id),
            query,
            **kwargs
        )

    def create(self, resource_id=None, attributes=None):
        """Creates a resource with the given ID (optional) and Attributes"""

        if attributes is None:
            attributes = {}

        result = None
        if not resource_id:
            result = self.client._post(
                self._url(resource_id),
                self._resource_class.create_attributes(attributes),
                headers=self._resource_class.create_headers(attributes)
            )
        else:
            result = self.client._put(
                self._url(resource_id),
                self._resource_class.create_attributes(attributes),
                headers=self._resource_class.create_headers(attributes)
            )

        return result

    def delete(self, resource_id, **kwargs):
        """Deletes a resource by ID"""

        return self.client._delete(self._url(resource_id), **kwargs)

    def _url(self, resource_id='', **kwargs):
        return self._resource_class.base_url(self.space_id, resource_id=resource_id, **kwargs)
