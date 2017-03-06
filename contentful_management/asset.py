from .resource import FieldsResource, PublishResource, ArchiveResource


"""
contentful.asset
~~~~~~~~~~~~~~~~

This module implements the Asset class.

API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/assets

:copyright: (c) 2017 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class Asset(FieldsResource, PublishResource, ArchiveResource):
    """
    API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/assets
    """

    def url(self, **kwargs):
        """
        Returns a formatted URL for the Asset's File
        with serialized parameters.

        Usage:
            >>> my_asset.url()
            "//images.contentful.com/spaces/foobar/..."
            >>> my_asset.url(w=120, h=160)
            "//images.contentful.com/spaces/foobar/...?w=120&h=160"
        """

        url = self.fields(self._locale()).get('file', {}).get('url', '')
        args = ['{0}={1}'.format(k, v) for k, v in kwargs.items()]

        if args:
            url += '?{0}'.format('&'.join(args))

        return url

    def process(self):
        """
        Calls the Process endpoint for all locales of the asset.

        API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/assets/asset-processing
        """

        for locale in self._fields.keys():
            self._client._put(
                "{0}/files/{1}/process".format(
                    self.__class__.base_url(self.space.id, self.id),
                    locale
                ),
                {},
                headers=self._update_headers()
            )
        return self.reload()

    def __repr__(self):
        return "<Asset id='{0}' url='{1}'>".format(
            self.sys.get('id', ''),
            self.url()
        )
