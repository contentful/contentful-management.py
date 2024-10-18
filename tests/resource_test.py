import vcr
from copy import deepcopy
from unittest import TestCase
from .test_helper import CLIENT, PLAYGROUND_SPACE


class ResourceTest(TestCase):
    @vcr.use_cassette('fixtures/resource/copy.yaml', decode_compressed_response=True)
    def test_can_properly_deepcopy(self):
        entry = CLIENT.spaces().find(PLAYGROUND_SPACE).environments().find('master').entries().all()[0]

        copied_entry = deepcopy(entry)

        self.assertEqual(entry.raw, copied_entry.raw)
        self.assertEqual(entry.fields(), copied_entry.fields())
        self.assertEqual(entry.id, copied_entry.id)


class LinkTest(TestCase):
    @vcr.use_cassette('fixtures/link/space_resolve.yaml', decode_compressed_response=True)
    def test_space_link_resolve(self):
        space = CLIENT.spaces().find(PLAYGROUND_SPACE)

        resolved_space = space.to_link().resolve()

        self.assertEqual(resolved_space.id, PLAYGROUND_SPACE)
        self.assertEqual(str(resolved_space), str(space))

    @vcr.use_cassette('fixtures/link/resolve.yaml', decode_compressed_response=True)
    def test_link_resolve(self):
        content_type = CLIENT.content_types(PLAYGROUND_SPACE, 'master').find('foo')

        resolved_ct = content_type.to_link().resolve(PLAYGROUND_SPACE, 'master')

        self.assertEqual(resolved_ct.id, 'foo')
        self.assertEqual(str(resolved_ct), str(content_type))
