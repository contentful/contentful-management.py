from unittest import TestCase
from contentful_management.content_type_field import ContentTypeField

SIMPLE_FIELD = {
    'name': 'foo',
    'id': 'foo',
    'type': 'Symbol'
}

LINK_FIELD = {
    'name': 'foo',
    'id': 'foo',
    'type': 'Link',
    'linkType': 'Entry'
}

ARRAY_FIELD = {
    'name': 'foo',
    'id': 'foo',
    'type': 'Array',
    'items': {
        'type': 'Symbol'
    }
}

ARRAY_LINK_FIELD = {
    'name': 'foo',
    'id': 'foo',
    'type': 'Array',
    'items': {
        'type': 'Link',
        'linkType': 'Entry'
    }
}

FIELD_WITH_VALIDATIONS = {
    'name': 'foo',
    'id': 'foo',
    'type': 'Symbol',
    'validations': [
        {'size': {'min': 3}}
    ]
}

FIELD_WITH_DEFAULT_VALUE = {
    'name': 'foo',
    'id': 'foo',
    'type': 'Symbol',
    'defaultValue': 'bar'
}


class ContentTypeFieldTest(TestCase):
    def test_simple_field_test(self):
        field = ContentTypeField(SIMPLE_FIELD)

        self.assertEqual(str(field), "<ContentTypeField[foo] id='foo' type='Symbol'>")
        self.assertEqual(field.to_json(), {
            'id': 'foo',
            'name': 'foo',
            'type': 'Symbol',
            'localized': False,
            'omitted': False,
            'required': False,
            'disabled': False,
            'validations': [],
        })

    def test_link_field_test(self):
        field = ContentTypeField(LINK_FIELD)

        self.assertEqual(str(field), "<ContentTypeField[foo] id='foo' type='Link'>")
        self.assertEqual(field.to_json(), {
            'id': 'foo',
            'name': 'foo',
            'type': 'Link',
            'linkType': 'Entry',
            'localized': False,
            'omitted': False,
            'required': False,
            'disabled': False,
            'validations': [],
        })

    def test_array_field_test(self):
        field = ContentTypeField(ARRAY_FIELD)

        self.assertEqual(str(field), "<ContentTypeField[foo] id='foo' type='Array'>")
        self.assertEqual(field.to_json(), {
            'id': 'foo',
            'name': 'foo',
            'type': 'Array',
            'items': {
                'type': 'Symbol'
            },
            'localized': False,
            'omitted': False,
            'required': False,
            'disabled': False,
            'validations': []
        })

    def test_link_array_field_test(self):
        field = ContentTypeField(ARRAY_LINK_FIELD)

        self.assertEqual(str(field), "<ContentTypeField[foo] id='foo' type='Array'>")
        self.assertEqual(field.to_json(), {
            'id': 'foo',
            'name': 'foo',
            'type': 'Array',
            'items': {
                'type': 'Link',
                'linkType': 'Entry'
            },
            'localized': False,
            'omitted': False,
            'required': False,
            'disabled': False,
            'validations': [],
        })

    def test_validations_field_test(self):
        field = ContentTypeField(FIELD_WITH_VALIDATIONS)

        self.assertEqual(str(field), "<ContentTypeField[foo] id='foo' type='Symbol'>")
        self.assertEqual(field.to_json(), {
            'id': 'foo',
            'name': 'foo',
            'type': 'Symbol',
            'localized': False,
            'omitted': False,
            'required': False,
            'disabled': False,
            'validations': [{
                'size': {'min': 3}
            }],
        })

    def test_coercion(self):
        field = ContentTypeField(SIMPLE_FIELD)

        self.assertEqual(field.coerce(123), '123')

    def test_default_value_test(self):
        field = ContentTypeField(FIELD_WITH_DEFAULT_VALUE)

        self.assertEqual(str(field), "<ContentTypeField[foo] id='foo' type='Symbol'>")
        self.assertEqual(field.to_json(), {
            'id': 'foo',
            'name': 'foo',
            'type': 'Symbol',
            'localized': False,
            'omitted': False,
            'required': False,
            'disabled': False,
            'validations': [],
            'defaultValue': 'bar'
        })
