from unittest import TestCase
from contentful_management.resource_builder import ResourceBuilder
from .test_helper import CLIENT

ITEM = {
    "sys": {
        "type": "Unknown"
    }
}


class ResourceBuilderTest(TestCase):
    def test_resource_builder_fails_on_unknown_type(self):
        resource_builder = ResourceBuilder(CLIENT, 'en-US', ITEM)

        with self.assertRaisesRegex(Exception, "Resource not buildable"):
            resource_builder.build()
