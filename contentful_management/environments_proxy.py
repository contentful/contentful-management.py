from .client_proxy import ClientProxy
from .environment import Environment

"""
contentful_management.environment_proxy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the EnvironmentsProxy class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/spaces

:copyright: (c) 2017 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""

class EnvironmentsProxy(ClientProxy):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/
    """
    
    @property
    def _resource_class(self):
        return Environment

    def all(self, query=None, **kwargs):
        """
        Gets all environments.
        """

        return super(EnvironmentsProxy, self).all(query=query)

    def find(self, environment_id, query=None, **kwargs):
        """
        Gets an environment by ID.
        """

        return super(EnvironmentsProxy, self).find(environment_id, query=query)

    def create(self, attributes=None):
        """
        Creates an environment with given attributes.
        """

        return super(EnvironmentsProxy, self).create(None, attributes)

    def delete(self, environment_id):
        """
        Deletes an environment by ID.
        """

        return super(EnvironmentsProxy, self).delete(environment_id)
