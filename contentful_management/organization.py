from .resource import Resource


"""
contentful_management.organization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the Organization class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/organizations

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class Organization(Resource):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/organizations
    """

    def __init__(self, item, **kwargs):
        super(Organization, self).__init__(item, **kwargs)
        self.name = item.get('name', '')

    @classmethod
    def base_url(klass, *args, **kwargs):
        """
        Returns the URI for the organization.
        """

        return "organizations"

    def __repr__(self):
        return "<Organization[{0}] id='{1}'>".format(
            self.name,
            self.id
        )
