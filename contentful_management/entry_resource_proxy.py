"""
contentful_management.entry_resource_proxy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the EntryResourceProxy class.

:copyright: (c) 2017 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class EntryResourceProxy(object):
    """Base Class for Entry related Resource Proxies"""

    def __init__(self, client, space_id, environment_id, entry_id):
        self.proxy = self._resource_proxy_class()(client, space_id, environment_id, entry_id)

    def __repr__(self):
        return "<{0} space_id='{1}' environment_id='{2}' entry_id='{3}'>".format(
            self.__class__.__name__,
            self.proxy.space_id,
            self.proxy.environment_id,
            self.proxy.parent_resource_id
        )

    def _resource_proxy_class(self):
        raise Exception("Must implement")

    def all(self, query=None):
        """
        Gets all resources related to the current entry.
        """

        return self.proxy.all(query)

    def find(self, resource_id, query=None):
        """
        Finds a single resource by ID related to the current entry.
        """

        return self.proxy.find(resource_id, query)

    def create(self, resource_id=None, attributes=None):
        """
        Creates a resource with a given ID (optional) and attributes for the current entry.
        """

        return self.proxy.create(resource_id=resource_id, attributes=attributes)

    def delete(self, resource_id):
        """
        Deletes a resource by ID.
        """

        return self.proxy.delete(resource_id)
