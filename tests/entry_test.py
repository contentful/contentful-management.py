import vcr
from unittest import TestCase
from contentful_management.entry import Entry
from contentful_management.errors import NotFoundError
from .test_helper import CLIENT, PLAYGROUND_SPACE

BASE_ENTRY_ITEM = {
    'sys': {
        'id': 'foo',
        'type': 'Entry',
        'space': {
            'sys': {
                'id': 'foobar',
                'type': 'Link',
                'linkType': 'Space'
            }
        },
        'contentType': {
            'sys': {
                'id': 'foo',
                'type': 'Link',
                'linkType': 'ContentType'
            }
        }
    },
    'fields': {
        'name': {
            'en-US': 'foobar'
        }
    }
}

class EntryTest(TestCase):
    def test_entry(self):
        entry = Entry(BASE_ENTRY_ITEM)

        self.assertEqual(str(entry), "<Entry[foo] id='foo'>")

    def test_entry_to_json(self):
        entry = Entry(BASE_ENTRY_ITEM)

        self.assertEqual(entry.to_json(), {
            'sys': {
                'id': 'foo',
                'type': 'Entry',
                'space': {
                    'sys': {
                        'id': 'foobar',
                        'type': 'Link',
                        'linkType': 'Space'
                    }
                },
                'contentType': {
                    'sys': {
                        'id': 'foo',
                        'type': 'Link',
                        'linkType': 'ContentType'
                    }
                }
            },
            'fields': {
                'name': {
                    'en-US': 'foobar'
                }
            }
        })

    def test_entry_to_link(self):
        entry = Entry(BASE_ENTRY_ITEM)

        self.assertEqual(entry.to_link().to_json(), {
            'sys': {
                'id': 'foo',
                'type': 'Link',
                'linkType': 'Entry'
            }
        })

    def test_entry_with_link(self):
        entry_data = {
            'sys': {
                'id': 'foo',
                'type': 'Entry',
                'space': {
                    'sys': {
                        'id': 'foobar',
                        'type': 'Link',
                        'linkType': 'Space'
                    }
                },
                'contentType': {
                    'sys': {
                        'id': 'foo',
                        'type': 'Link',
                        'linkType': 'ContentType'
                    }
                }
            },
            'fields': {
                'link': {
                    'en-US': {
                        'sys': {
                            'id': 'something',
                            'type': 'Link',
                            'linkType': 'Entry'
                        }
                    }
                }
            }
        }

        entry = Entry(entry_data)

        self.assertEqual(str(entry.link), "<Link[Entry] id='something'>")

    def test_entry_with_link_array(self):
        entry_data = {
            'sys': {
                'id': 'foo',
                'type': 'Entry',
                'space': {
                    'sys': {
                        'id': 'foobar',
                        'type': 'Link',
                        'linkType': 'Space'
                    }
                },
                'contentType': {
                    'sys': {
                        'id': 'foo',
                        'type': 'Link',
                        'linkType': 'ContentType'
                    }
                }
            },
            'fields': {
                'links': {
                    'en-US': [
                        {
                            'sys': {
                                'id': 'something',
                                'type': 'Link',
                                'linkType': 'Entry'
                            }
                        }
                    ]
                }
            }
        }

        entry = Entry(entry_data)

        self.assertEqual(str(entry.links[0]), "<Link[Entry] id='something'>")

    @vcr.use_cassette('fixtures/entry/create.yaml')
    def test_create_entry(self):
        entry = CLIENT.entries(PLAYGROUND_SPACE).create(None, {
            'content_type_id': 'foo',
            'fields': {
                'name': {
                    'en-US': 'foobar'
                }
            }
        })

        self.assertEqual(entry.name, 'foobar')
        self.assertTrue(entry.id)

    @vcr.use_cassette('fixtures/entry/id_create.yaml')
    def test_create_entry_with_id(self):
        entry = CLIENT.entries(PLAYGROUND_SPACE).create('id_create_entry_test', {
            'content_type_id': 'foo',
            'fields': {
                'name': {
                    'en-US': 'foobar'
                }
            }
        })

        self.assertEqual(entry.id, 'id_create_entry_test')
        self.assertEqual(entry.name, 'foobar')

    @vcr.use_cassette('fixtures/entry/create_no_fields.yaml')
    def test_create_entry_no_fields(self):
        entry = CLIENT.entries(PLAYGROUND_SPACE).create(None, {
            'content_type_id': 'foo'
        })

        self.assertTrue(entry.id)
        self.assertEqual(entry.fields(), {})

    def test_create_entry_fails_without_content_type(self):
        with self.assertRaises(Exception):
            CLIENT.entries(PLAYGROUND_SPACE).create(None, None)

    @vcr.use_cassette('fixtures/entry/find.yaml')
    def test_snapshots_entries(self):
        entry = CLIENT.entries(PLAYGROUND_SPACE).find('5gQdVmPHKwIk2MumquYwOu')

        proxy = entry.snapshots()

        self.assertEqual(str(proxy), "<EntrySnapshotsProxy space_id='{0}' entry_id='5gQdVmPHKwIk2MumquYwOu'>".format(PLAYGROUND_SPACE))

    @vcr.use_cassette('fixtures/entry/find_2.yaml')
    def test_delete_entry(self):
        entry = CLIENT.entries(PLAYGROUND_SPACE).find('4RToqNcBfW6MAK0UGU0qWc')

        with vcr.use_cassette('fixtures/entry/delete.yaml'):
            entry.delete()

        with vcr.use_cassette('fixtures/entry/not_found.yaml'):
            with self.assertRaises(NotFoundError):
                CLIENT.entries(PLAYGROUND_SPACE).find('4RToqNcBfW6MAK0UGU0qWc')

    @vcr.use_cassette('fixtures/entry/find_3.yaml')
    def test_publish_entry(self):
        entry = CLIENT.entries(PLAYGROUND_SPACE).find('5gQdVmPHKwIk2MumquYwOu')

        published_counter = getattr(entry, 'published_counter', 0)

        with vcr.use_cassette('fixtures/entry/publish.yaml'):
            entry.publish()

        self.assertEqual(entry.published_counter, published_counter + 1)
        self.assertTrue(entry.is_published)

    @vcr.use_cassette('fixtures/entry/find_4.yaml')
    def test_unpublish_entry(self):
        entry = CLIENT.entries(PLAYGROUND_SPACE).find('5gQdVmPHKwIk2MumquYwOu')

        with vcr.use_cassette('fixtures/entry/unpublish.yaml'):
            entry.unpublish()

        self.assertFalse(entry.is_published)

    @vcr.use_cassette('fixtures/entry/find_5.yaml')
    def test_update_entry(self):
        entry = CLIENT.entries(PLAYGROUND_SPACE).find('1dYTHwMZlU2wm88SA8I2Q0')

        self.assertEqual(entry.name, 'foobar')

        with vcr.use_cassette('fixtures/entry/update.yaml'):
            entry.name = 'something else'
            entry.save()

        self.assertEqual(entry.name, 'something else')

    # Issues
    def test_update_entry_field_that_was_undefined_in_the_webapp(self):
        entry = None
        with vcr.use_cassette('fixtures/entry/undefined_fields.yaml'):
            entry = CLIENT.entries(PLAYGROUND_SPACE).find('33uj74Wln2Oc02CAyEY8CK')

            self.assertEqual(entry.fields(), {})

            with vcr.use_cassette('fixtures/entry/undefined_fields_write.yaml'):
                entry.name = 'foo'

                self.assertEqual(entry.fields()['name'], 'foo')

                entry.save()

                updated_entry = CLIENT.entries(PLAYGROUND_SPACE).find('33uj74Wln2Oc02CAyEY8CK')

                self.assertEqual(updated_entry.fields(), {'name': 'foo'})


    def test_update_entry_field_with_undefined_but_non_present_field(self):
        entry = None
        with vcr.use_cassette('fixtures/entry/undefined_fields.yaml'):
            entry = CLIENT.entries(PLAYGROUND_SPACE).find('33uj74Wln2Oc02CAyEY8CK')

            self.assertEqual(entry.fields(), {})

            with vcr.use_cassette('fixtures/entry/undefined_fields_non_present.yaml'):
                entry.non_existent = 'foo'

                self.assertEqual(entry.non_existent, 'foo')
                self.assertEqual(entry.fields(), {})

    def test_update_entry_field_with_field_that_was_not_present(self):
        entry = None
        with vcr.use_cassette('fixtures/entry/added_fields_1.yaml'):
            entry = CLIENT.entries(PLAYGROUND_SPACE).find('3fTNzlQsDmge6YQEikEuME')

            self.assertEqual(entry.fields(), {'name': 'A Name', 'other': 'Other Stuff'})

            with vcr.use_cassette('fixtures/entry/added_fields_2.yaml'):
                entry.different = 'A Different Field'

                self.assertEqual(entry.different, 'A Different Field')
                self.assertEqual(entry.fields(), {'name': 'A Name', 'other': 'Other Stuff', 'different': 'A Different Field'})

                self.assertEqual(entry.to_json()['fields']['different']['en-US'], 'A Different Field')

                entry.save()

            with vcr.use_cassette('fixtures/entry/added_fields_3.yaml'):
                entry = CLIENT.entries(PLAYGROUND_SPACE).find('3fTNzlQsDmge6YQEikEuME')
                self.assertEqual(entry.different, 'A Different Field')
