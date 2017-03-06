import vcr
from unittest import TestCase
from contentful_management.content_types_proxy import ContentTypesProxy
from .test_helper import CLIENT, PLAYGROUND_SPACE

class ContentTypesProxyTest(TestCase):
    def test_content_types_proxy(self):
        proxy = ContentTypesProxy(CLIENT, PLAYGROUND_SPACE)

        self.assertEqual(str(proxy), "<ContentTypesProxy space_id='{0}'>".format(PLAYGROUND_SPACE))

    @vcr.use_cassette('fixtures/content_type/all_published.yaml')
    def test_content_types_all_published(self):
        all_published = []

        self.assertFalse(all_published)

        all_published = ContentTypesProxy(CLIENT, PLAYGROUND_SPACE).all_published()

        self.assertTrue(all_published)
        self.assertTrue("ContentType" in str(all_published[0]))
