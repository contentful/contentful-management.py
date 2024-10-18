from unittest import TestCase
from contentful_management.snapshot import Snapshot

ENTRY_SNAPSHOT_ITEM = {
    'sys': {
        'id': 'foo',
        'type': 'Snapshot',
        'snapshotEntityType': 'Entry',
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

CONTENT_TYPE_SNAPSHOT_ITEM = {
    "snapshot": {
        "name": "Blog Post",
        "displayField": "title",
        "fields": [
            {
                "id": "title",
                "name": "Title",
                "required": True,
                "localized": True,
                "type": "Text"
            },
            {
                "id": "body",
                "name": "Body",
                "required": True,
                "localized": True,
                "type": "Text"
            }
        ],
        "sys": {
            "firstPublishedAt": "2015-05-15T13:38:11.311Z",
            "publishedCounter": 2,
            "publishedAt": "2015-05-15T13:38:11.311Z",
            "id": "blogPost",
            "publishedBy": {
                "sys": {
                    "type": "Link",
                    "linkType": "User",
                    "id": "4FLrUHftHW3v2BLi9fzfjU"
                }
            },
            "publishedVersion": 9
        }
    },
    "sys": {
        "space": {
            "sys": {
                "type": "Link",
                "linkType": "Space",
                "id": "yadj1kx9rmg0"
            }
        },
        "type": "Snapshot",
        "id": "cat",
        "createdBy": {
            "sys": {
                "type": "Link",
                "linkType": "User",
                "id": "4FLrUHftHW3v2BLi9fzfjU"
            }
        },
        "createdAt": "2015-05-18T11:29:46.809Z",
        "snapshotType": "publish",
        "snapshotEntityType": "ContentType"
    }
}

UNBUILDABLE_SNAPSHOT_ITEM = {
    'sys': {
        'id': 'foo',
        'type': 'Snapshot',
        'snapshotEntityType': 'NotBuildable',
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
            'type': 'NotBuildable'
        }
    }
}


class SnapshotTest(TestCase):
    def test_snapshot(self):
        entry_snapshot = Snapshot(ENTRY_SNAPSHOT_ITEM)
        self.assertEqual(str(entry_snapshot), "<Snapshot[Entry] id='foo'>")

        ct_snapshot = Snapshot(CONTENT_TYPE_SNAPSHOT_ITEM)
        self.assertEqual(str(ct_snapshot), "<Snapshot[ContentType] id='cat'>")

    def test_unbuildable_snapshot(self):
        with self.assertRaisesRegex(Exception, "Object 'NotBuildable' not buildable"):
            Snapshot(UNBUILDABLE_SNAPSHOT_ITEM)

    def test_snapshot_to_json(self):
        entry_snapshot = Snapshot(ENTRY_SNAPSHOT_ITEM)
        self.assertEqual(entry_snapshot.to_json(), {
            'sys': {
                'id': 'foo',
                'type': 'Snapshot',
                'snapshotEntityType': 'Entry',
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
                            'id': 'foo'
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

        ct_snapshot = Snapshot(CONTENT_TYPE_SNAPSHOT_ITEM)
        self.assertEqual(ct_snapshot.to_json(), {
            "snapshot": {
                "name": "Blog Post",
                "description": "",
                "displayField": "title",
                "fields": [
                    {
                        "id": "title",
                        "name": "Title",
                        "required": True,
                        "localized": True,
                        "disabled": False,
                        "omitted": False,
                        "type": "Text",
                        "validations": [],
                    },
                    {
                        "id": "body",
                        "name": "Body",
                        "required": True,
                        "localized": True,
                        "disabled": False,
                        "omitted": False,
                        "type": "Text",
                        "validations": [],
                    }
                ],
                "sys": {
                    "firstPublishedAt": "2015-05-15T13:38:11.311000+00:00",
                    "publishedCounter": 2,
                    "publishedAt": "2015-05-15T13:38:11.311000+00:00",
                    "id": "blogPost",
                    "publishedBy": {
                        "sys": {
                            "type": "Link",
                            "linkType": "User",
                            "id": "4FLrUHftHW3v2BLi9fzfjU"
                        }
                    },
                    "publishedVersion": 9
                }
            },
            "sys": {
                "space": {
                    "sys": {
                        "type": "Link",
                        "linkType": "Space",
                        "id": "yadj1kx9rmg0"
                    }
                },
                "type": "Snapshot",
                "id": "cat",
                "createdBy": {
                    "sys": {
                        "type": "Link",
                        "linkType": "User",
                        "id": "4FLrUHftHW3v2BLi9fzfjU"
                    }
                },
                "createdAt": "2015-05-18T11:29:46.809000+00:00",
                "snapshotType": "publish",
                "snapshotEntityType": "ContentType"
            }
        })

    def test_snapshot_to_link(self):
        entry_snapshot = Snapshot(ENTRY_SNAPSHOT_ITEM)
        self.assertEqual(entry_snapshot.to_link().to_json(), {
            'sys': {
                'id': 'foo',
                'type': 'Link',
                'linkType': 'Snapshot'
            }
        })

        ct_snapshot = Snapshot(CONTENT_TYPE_SNAPSHOT_ITEM)
        self.assertEqual(ct_snapshot.to_link().to_json(), {
            'sys': {
                'id': 'cat',
                'type': 'Link',
                'linkType': 'Snapshot'
            }
        })

    def test_snapshot_not_supported_methods(self):
        with self.assertRaises(Exception):
            Snapshot(ENTRY_SNAPSHOT_ITEM).save()

        with self.assertRaises(Exception):
            Snapshot(ENTRY_SNAPSHOT_ITEM).update()

    def test_snapshots_snapshot_contains_an_entry(self):
        snapshot = Snapshot(ENTRY_SNAPSHOT_ITEM)

        self.assertEqual(snapshot.snapshot.name, 'foobar')
        self.assertEqual(str(snapshot.snapshot), "<Entry[foo] id='foo'>")

    def test_snapshots_snapshot_contains_a_content_type(self):
        snapshot = Snapshot(CONTENT_TYPE_SNAPSHOT_ITEM)
        self.assertEqual(snapshot.snapshot.name, 'Blog Post')
        self.assertEqual(str(snapshot.snapshot), "<ContentType[Blog Post] id='blogPost'>")
