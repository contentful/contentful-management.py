"""
contentful_management.environment_resource_proxy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the EnvironmentResourceProxy class.

:copyright: (c) 2017 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class EnvironmentResourceProxy(object):
    """
    Base class for environment related resource proxies.
    """

    def __init__(self, client, space_id, environment):
        self.proxy = self._resource_proxy_class()(client, space_id)
        self.environment = environment

    def __repr__(self):
        return "<{0} space_id='{1}' environment='{2}'>".format(
            self.__class__.__name__,
            self.proxy.space_id,
            self.environment
        )

    def _resource_proxy_class(self):
        raise Exception("Must implement")

    def all(self, query=None):
        """
        Gets all resources related to the current space.
        """

        return self.proxy.all(query, environment=self.environment)

    def find(self, resource_id, query=None):
        """
        Finds a single resource by ID related to the current space.
        """

        return self.proxy.find(resource_id, query=query, environment=self.environment)

    def create(self, resource_id=None, attributes=None):
        """
        Creates a resource with a given ID (optional) and attributes for the current space.
        """

        return self.proxy.create(resource_id=resource_id, attributes=attributes, environment=self.environment)

    def delete(self, resource_id):
        """
        Deletes a resource by ID.
        """

        return self.proxy.delete(resource_id, environment=self.environment)