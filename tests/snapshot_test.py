from unittest import TestCase
from contentful_management.snapshot import Snapshot

SNAPSHOT_ITEM = {
    'sys': {
        'id': 'foo',
        'type': 'Snapshot',
        'space': {
            'sys': {
                'id': 'foobar',
                'type': 'Link',
                'linkType': 'Space'
            }
        }
    },
    'snapshot': {
        'sys': {
            'id': 'foo',
            'type': 'Entry',
            'contentType': {
                'sys': {
                    'type': 'Link',
                    'linkType': 'ContentType',
                    'id' : 'foo'
                }
            }
        },
        'fields': {
            'name': {
                'en-US': 'foobar'
            }
        }
    }
}

class SnapshotTest(TestCase):
    def test_snapshot(self):
        snapshot = Snapshot(SNAPSHOT_ITEM)

        self.assertEqual(str(snapshot), "<Snapshot id='foo'>")

    def test_snapshot_to_json(self):
        snapshot = Snapshot(SNAPSHOT_ITEM)

        self.assertEqual(snapshot.to_json(), {
            'sys': {
                'id': 'foo',
                'type': 'Snapshot',
                'space': {
                    'sys': {
                        'id': 'foobar',
                        'type': 'Link',
                        'linkType': 'Space'
                    }
                }
            },
            'snapshot': {
                'sys': {
                    'id': 'foo',
                    'type': 'Entry',
                    'contentType': {
                        'sys': {
                            'type': 'Link',
                            'linkType': 'ContentType',
                            'id' : 'foo'
                        }
                    }
                },
                'fields': {
                    'name': {
                        'en-US': 'foobar'
                    }
                }
            }
        })

    def test_snapshot_to_link(self):
        snapshot = Snapshot(SNAPSHOT_ITEM)

        self.assertEqual(snapshot.to_link().to_json(), {
            'sys': {
                'id': 'foo',
                'type': 'Link',
                'linkType': 'Snapshot'
            }
        })

    def test_snapshot_not_supported_methods(self):
        with self.assertRaises(Exception):
            Snapshot(SNAPSHOT_ITEM).save()

        with self.assertRaises(Exception):
            Snapshot(SNAPSHOT_ITEM).update()

    def test_snapshots_snapshot_contains_an_entry(self):
        snapshot = Snapshot(SNAPSHOT_ITEM)

        self.assertEqual(snapshot.snapshot.name, 'foobar')
        self.assertEqual(str(snapshot.snapshot), "<Entry[foo] id='foo'>")
