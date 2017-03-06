from .resource import FieldsResource


"""
contentful.Snapshot
~~~~~~~~~~~~~~~~~~~~~~~

This module implements the Snapshot class.

API Reference: https://www.contentful.com/developers/docs/references/content-delivery-api/#/reference/content-types

:copyright: (c) 2016 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class Snapshot(FieldsResource):
    """
    API Reference: https://www.contentful.com/developers/docs/references/content-delivery-api/#/reference/content-types
    """

    def __init__(self, item, **kwargs):
        super(Snapshot, self).__init__(item, **kwargs)

    @classmethod
    def base_url(klass, space_id, entry_id, resource_id=None):
        """Returns the URI for the Resource"""

        return "spaces/{0}/entries/{1}/snapshots/{2}".format(
            space_id,
            entry_id,
            resource_id if resource_id is not None else ''
        )

    def __repr__(self):
        return "<Snapshot id='{0}'>".format(
            self.sys.get('id', '')
        )

    def save(self):
        """Not Supported"""

        raise Exception("Not Supported")

    def update(self, _attributes=None):
        """Not Supported"""

        raise Exception("Not Supported")
