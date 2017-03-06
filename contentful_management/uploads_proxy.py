from .client_proxy import ClientProxy
from .upload import Upload
from .utils import str_type


"""
contentful.uploads_proxy
~~~~~~~~~~~~~~~~~~~~~~~

This module implements the UploadsProxy class.

API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/uploads

:copyright: (c) 2017 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class UploadsProxy(ClientProxy):
    """
    API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/uploads
    """

    @property
    def _resource_class(self):
        return Upload

    def all(*args, **kwargs):
        """Not Supported"""

        raise Exception("Not supported")

    def create(self, file_or_path, **kwargs):
        """Creates an Upload for the given file or path."""

        opened = False
        if isinstance(file_or_path, str_type()):
            file_or_path = open(file_or_path, 'rb')
            opened = True
        elif not getattr(file_or_path, 'read', False):
            raise Exception("A file or path to a file is required for this operation.")

        try:
            return self.client._post(
                self._url(),
                file_or_path,
                headers=self._resource_class.create_headers({}),
                file_upload=True
            )
        finally:
            if opened:
                file_or_path.close()

    def find(self, upload_id, **kwargs):
        """Finds an Upload by ID."""

        return super(UploadsProxy, self).find(upload_id, file_upload=True)

    def delete(self, upload_id):
        """Deletes an Upload by ID."""

        return super(UploadsProxy, self).delete(upload_id, file_upload=True)
