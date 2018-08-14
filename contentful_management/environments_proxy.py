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
