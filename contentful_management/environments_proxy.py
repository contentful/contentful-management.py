from .client_proxy import ClientProxy
from .environment import Environment

"""
contentful_management.environment_proxy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the EnvironmentsProxy class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/spaces

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class EnvironmentsProxy(ClientProxy):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/
    """

    def __init__(self, client, space_id):
        super(EnvironmentsProxy, self).__init__(client, space_id)

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

    def create(self, environment_id=None, attributes=None):
        """
        Creates an environment with a given ID (optional) and attributes.
        """

        return super(EnvironmentsProxy, self).create(environment_id, attributes)

    def delete(self, environment_id):
        """
        Deletes an environment by ID.
        """

        return super(EnvironmentsProxy, self).delete(environment_id)
