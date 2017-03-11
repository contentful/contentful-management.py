"""
contentful.content_type_resource_proxy
~~~~~~~~~~~~~~~~~~~~~~~

This module implements the ContentTypeResourceProxy class.

:copyright: (c) 2017 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class ContentTypeResourceProxy(object):
    """Base Class for Content Type related Resource Proxies"""

    def __init__(self, client, space_id, content_type_id):
        self.proxy = self._resource_proxy_class()(client, space_id, content_type_id)

    def __repr__(self):
        return "<{0} space_id='{1}' content_type_id='{2}'>".format(
            self.__class__.__name__,
            self.proxy.space_id,
            self.proxy.content_type_id
        )

    def _resource_proxy_class(self):
        raise Exception("Must implement")

    def all(self, query=None):
        """
        Gets all resources related to the current Content Type.
        """

        return self.proxy.all(query)

    def find(self, resource_id, query=None):
        """
        Finds a single resource by ID related to the current Content Type.
        """

        return self.proxy.find(resource_id, query)

    def create(self, resource_id=None, attributes=None):
        """
        Creates a resource with a given ID (optional) and attributes for the current Content Type.
        """

        return self.proxy.create(resource_id=resource_id, attributes=attributes)

    def delete(self, resource_id):
        """
        Deletes a Resource by ID.
        """

        return self.proxy.delete(resource_id)
