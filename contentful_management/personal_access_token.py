import dateutil.parser
from .resource import Resource


"""
contentful_management.PersonalAccessToken
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the PersonalAccessToken class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/personal-access-tokens

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class PersonalAccessToken(Resource):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/personal-access-tokens
    """

    def __init__(self, item, **kwargs):
        super(PersonalAccessToken, self).__init__(item, **kwargs)
        self.name = item.get('name', '')
        self.scopes = item.get('scopes', [])
        self.token = item.get('token', '')
        try:
            self.revoked_at = dateutil.parser.parse(item.get('revokedAt', ''))
        except:
            self.revoked_at = None

    @classmethod
    def base_url(klass, resource_id=None, **kwargs):
        """
        Returns the URI for the personal access token.
        """

        return "users/me/access_tokens/{0}".format(
            resource_id if resource_id is not None else ''
        )

    @property
    def is_revoked(self):
        return bool(self.revoked_at)

    def __repr__(self):
        return "<PersonalAccessToken[{0}] id='{1}' scopes=[{2}] revoked={3}>".format(
            self.name,
            self.sys.get('id', ''),
            ', '.join("'{0}'".format(s) for s in self.scopes),
            self.is_revoked
        )
