from .client_proxy import ClientProxy
from .personal_access_token import PersonalAccessToken


"""
contentful_management.personal_access_token_proxy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the PersonalAccessTokensProxy class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/personal-access-tokens

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class PersonalAccessTokensProxy(ClientProxy):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/personal-access-tokens
    """

    def __init__(self, client):
        super(PersonalAccessTokensProxy, self).__init__(client, None)

    def __repr__(self):
        return "<PersonalAccessTokensProxy>"

    def _url(self, resource_id='', **kwargs):
        return self._resource_class.base_url(resource_id=resource_id, **kwargs)

    @property
    def _resource_class(self):
        return PersonalAccessToken

    def create(self, attributes):
        return super(PersonalAccessTokensProxy, self).create(None, attributes)

    def delete(self, token_id, *args, **kwargs):
        """
        Revokes a personal access token.
        """

        return self.client._put(
            "{0}/revoked".format(
                self._url(token_id)
            ),
            None,
            *args,
            **kwargs
        )

    def revoke(self, token_id, *args, **kwargs):
        """
        Revokes a personal access token.
        """

        return self.delete(token_id, *args, **kwargs)
