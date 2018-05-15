from .resource import Resource, EnvironmentAwareResource


"""
contentful_management.snapshot
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the Snapshot class.

API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/snapshots

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class Snapshot(Resource, EnvironmentAwareResource):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/snapshots
    """

    def __init__(self, item, **kwargs):
        super(Snapshot, self).__init__(item, **kwargs)

        from .entry import Entry
        from .content_type import ContentType
        entity_type = {
            'Entry': Entry,
            'ContentType': ContentType
        }

        if self.sys['snapshot_entity_type'] not in entity_type:
            raise Exception("Object '{0}' not buildable".format(self.sys['snapshot_entity_type']))

        self.snapshot = entity_type[self.sys['snapshot_entity_type']](item['snapshot'], **kwargs)

    @classmethod
    def base_url(klass, space_id, parent_resource_id, resource_url='entries', resource_id=None, environment_id=None):
        """
        Returns the URI for the snapshot.
        """

        return "spaces/{0}{1}/{2}/{3}/snapshots/{4}".format(
            space_id,
            '/environments/{0}'.format(environment_id) if environment_id is not None else '',
            resource_url,
            parent_resource_id,
            resource_id if resource_id is not None else ''
        )

    def to_json(self):
        """
        Returns the JSON representation of the snapshot.
        """

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
        """
        Not supported.
        """

        raise Exception("Not Supported")

    def update(self, _attributes=None):
        """
        Not supported.
        """

        raise Exception("Not Supported")
