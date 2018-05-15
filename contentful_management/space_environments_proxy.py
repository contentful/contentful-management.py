from .space_resource_proxy import SpaceResourceProxy
from .environments_proxy import EnvironmentsProxy

"""
contentful_management.space_environments_proxy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the SpaceEnvironmentsProxy class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class SpaceEnvironmentsProxy(SpaceResourceProxy):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/
    """

    def _resource_proxy_class(self):
        return EnvironmentsProxy
