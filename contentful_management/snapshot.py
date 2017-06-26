from .resource import Resource


"""
contentful.Snapshot
~~~~~~~~~~~~~~~~~~~~~~~

This module implements the Snapshot class.

API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/snapshots

:copyright: (c) 2016 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class Snapshot(Resource):
    """
    API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/snapshots
    """

    def __init__(self, item, **kwargs):
        super(Snapshot, self).__init__(item, **kwargs)

        from .entry import Entry
        from .content_type import ContentType
        entity_type = {
            'Entry': Entry,
            'ContentType': ContentType
        }
        self.snapshot = entity_type[self.sys['snapshot_entity_type']](item['snapshot'], **kwargs)

    @classmethod
    def base_url(klass, space_id, parent_resource_id, resource_url='entries', resource_id=None):
        """Returns the URI for the Resource"""

        return "spaces/{0}/{1}/{2}/snapshots/{3}".format(
            space_id,
            resource_url,
            parent_resource_id,
            resource_id if resource_id is not None else ''
        )

    def to_json(self):
        """Returns the JSON Representation of the Resource"""

        result = super(Snapshot, self).to_json()
        result.update({
            'snapshot': self.snapshot.to_json(),
        })
        return result

    def __repr__(self):
        return "<Snapshot[{0}] id='{1}'>".format(
            self.sys.get('snapshot_entity_type', ''),
            self.sys.get('id', '')
        )

    def save(self):
        """Not Supported"""

        raise Exception("Not Supported")

    def update(self, _attributes=None):
        """Not Supported"""

        raise Exception("Not Supported")
