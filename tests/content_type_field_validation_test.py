from unittest import TestCase
from contentful_management.content_type_field_validation import ContentTypeFieldValidation


class ContentTypeFieldValidationTest(TestCase):
    def test_content_type_field_validation(self):
        validation = ContentTypeFieldValidation({
            'size': {'min': 3}
        })

        self.assertEqual(str(validation), "<ContentTypeFieldValidation size='{'min': 3}'>")
        self.assertEqual(validation.to_json(), {
            'size': {'min': 3}
        })

        self.assertEqual(validation.size, {'min': 3})

        with self.assertRaises(Exception):
            validation.foobar

        validation.foo = 'bar'
        self.assertEqual(validation.to_json(), {
            'size': {'min': 3},
            'foo': 'bar'
        })
