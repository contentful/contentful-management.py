import vcr
from unittest import TestCase
from contentful_management.errors import NotFoundError
from contentful_management.organization import Organization
from contentful_management.taxonomy_concept import TaxonomyConcept
from .test_helper import CLIENT, PLAYGROUND_ORG, PLAYGROUND_SPACE

TAXONOMY_CONCEPT_ITEM = {
    "sys": {
        "id": "3kZdDUXy9n0l2Xi2cq8TPc",
        "type": "TaxonomyConcept",
    },
    "uri": "",
    "prefLabel": {
        "en-US": "Sofas"
    }
}


class TaxonomyConceptTest(TestCase):
    def test_taxonomy_concept(self):
        concept = TaxonomyConcept(TAXONOMY_CONCEPT_ITEM)
        self.assertEqual(str(concept), "<TaxonomyConcept id='3kZdDUXy9n0l2Xi2cq8TPc'>")

    def test_organization_taxonomy_concepts(self):
        org = Organization({'sys': {'id': PLAYGROUND_ORG}})
        self.assertEqual(str(org.taxonomy_concepts()), f"<TaxonomyConceptsProxy organization_id='{PLAYGROUND_ORG}'>")

    @vcr.use_cassette('fixtures/taxonomy/concept/find.yaml', decode_compressed_response=True)
    def test_find_taxonomy_concept(self):
        concept = CLIENT.taxonomy_concepts(PLAYGROUND_ORG).find('5iRG7dAusVFUOh9SrexDqQ')
        self.assertEqual(concept.sys['id'], '5iRG7dAusVFUOh9SrexDqQ')
        self.assertEqual(concept.uri, "https://example/testconcept")
        self.assertEqual(concept.pref_label['en-US'], "TestConcept")

    @vcr.use_cassette('fixtures/taxonomy/concept/create.yaml', decode_compressed_response=True)
    def test_create_taxonomy_concept(self):
        concept_attributes = {
            "prefLabel": {
                "en-US": "Sofas"
            },
            "altLabels": {
                "en-US": [
                    "Couches",
                    "Settees"
                ]
            },
            "hiddenLabels": {
                "en-US": [
                    "Davenports"
                ]
            },
            "notations": [
                "FURN0017B"
            ],
        }

        concept = CLIENT.taxonomy_concepts(PLAYGROUND_ORG).create(concept_attributes)

        self.assertEqual(concept.pref_label['en-US'], 'Sofas')
        self.assertEqual(concept.alt_labels['en-US'], ['Couches', 'Settees'])
        self.assertEqual(concept.hidden_labels['en-US'], ['Davenports'])
        self.assertEqual(concept.notations, ['FURN0017B'])
        self.assertTrue(concept.id)

    @vcr.use_cassette('fixtures/taxonomy/concept/create_with_id.yaml', decode_compressed_response=True)
    def test_create_taxonomy_concept_with_id(self):
        concept_attributes = {
            "uri": "",
            "prefLabel": {
                "en-US": "Sofas"
            }
        }

        concept = CLIENT.taxonomy_concepts(PLAYGROUND_ORG).create(
            resource_id='3kZdDUXy9n0l2Xi2cq8TPc',
            attributes=concept_attributes
        )

        self.assertEqual(concept.sys['id'], '3kZdDUXy9n0l2Xi2cq8TPc')
        self.assertEqual(concept.pref_label['en-US'], 'Sofas')

    @vcr.use_cassette('fixtures/taxonomy/concept/all.yaml', decode_compressed_response=True)
    def test_all_taxonomy_concepts(self):
        concepts = CLIENT.taxonomy_concepts(PLAYGROUND_ORG).all()

        self.assertEqual(len(concepts), 4)
        self.assertIsInstance(concepts[-1], TaxonomyConcept)
        self.assertEqual(concepts[-1].pref_label['en-US'], 'Sofas')

    @vcr.use_cassette('fixtures/taxonomy/concept/descendants.yaml', decode_compressed_response=True)
    def test_get_descendants_of_a_concept(self):
        descendants = CLIENT.taxonomy_concepts(PLAYGROUND_ORG).descendants('5KHXWlmxvntrrB09szapUp')

        self.assertEqual(len(descendants), 1)
        self.assertIsInstance(descendants[0], TaxonomyConcept)
        self.assertEqual(descendants[0].pref_label['en-US'], 'Green Sofas')

    @vcr.use_cassette('fixtures/taxonomy/concept/ancestors.yaml', decode_compressed_response=True)
    def test_get_ancestors_of_a_concept(self):
        ancestors = CLIENT.taxonomy_concepts(PLAYGROUND_ORG).ancestors('greenSofas')

        self.assertEqual(len(ancestors), 1)
        self.assertIsInstance(ancestors[0], TaxonomyConcept)
        self.assertEqual(ancestors[0].pref_label['en-US'], 'Sofas')

    @vcr.use_cassette('fixtures/taxonomy/concept/total.yaml', decode_compressed_response=True)
    def test_get_total_concepts(self):
        response = CLIENT.taxonomy_concepts(PLAYGROUND_ORG).total()

        self.assertIsInstance(response, dict)
        self.assertIn('total', response)
        self.assertIsInstance(response['total'], int)

    @vcr.use_cassette('fixtures/taxonomy/concept/update.yaml', decode_compressed_response=True)
    def test_update_taxonomy_concept(self):
        concept = CLIENT.taxonomy_concepts(PLAYGROUND_ORG).find('5iRG7dAusVFUOh9SrexDqQ')

        patches = [
            {
                'op': 'replace',
                'path': '/prefLabel/en-US',
                'value': 'Updated Sofas'
            }
        ]

        updated_concept = CLIENT.taxonomy_concepts(PLAYGROUND_ORG).update(
            '5iRG7dAusVFUOh9SrexDqQ',
            concept.sys['version'],
            patches
        )

        self.assertEqual(updated_concept.pref_label['en-US'], 'Updated Sofas')

    @vcr.use_cassette('fixtures/taxonomy/concept/delete.yaml', decode_compressed_response=True)
    def test_delete_taxonomy_concept(self):
        concept = CLIENT.taxonomy_concepts(PLAYGROUND_ORG).find('5iRG7dAusVFUOh9SrexDqQ')

        CLIENT.taxonomy_concepts(PLAYGROUND_ORG).delete(
            concept.sys['id'],
            concept.sys['version']
        )

        with vcr.use_cassette('fixtures/taxonomy/concept/not_found.yaml', decode_compressed_response=True):
            with self.assertRaises(NotFoundError):
                CLIENT.taxonomy_concepts(PLAYGROUND_ORG).find('5iRG7dAusVFUOh9SrexDqQ')

    @vcr.use_cassette('fixtures/taxonomy/concepts/add_concept_to_an_entry.yaml', decode_compressed_response=True)
    def test_update_entry_with_concepts(self):
        entry = CLIENT.entries(PLAYGROUND_SPACE, 'master').find('1emVC32ZCCjYvUgDgtZQR8')
        self.assertEqual(len(entry._metadata['concepts']), 0)

        entry.update({"_metadata": {"concepts": [{"sys": {"type": "Link", "linkType": "TaxonomyConcept", "id": "greenSofas"}}], "tags": []}})

        entry = CLIENT.entries(PLAYGROUND_SPACE, 'master').find('1emVC32ZCCjYvUgDgtZQR8')
        self.assertEqual(len(entry._metadata['concepts']), 1)

    @vcr.use_cassette('fixtures/taxonomy/concepts/add_concept_to_an_asset.yaml', decode_compressed_response=True)
    def test_update_asset_with_concepts(self):
        entry = CLIENT.assets(PLAYGROUND_SPACE, 'master').find('56PfMcxCLyzuXP3k7k0yL5')
        self.assertEqual(len(entry._metadata['concepts']), 0)

        entry.update({"_metadata": {"concepts": [{"sys": {"type": "Link", "linkType": "TaxonomyConcept", "id": "greenSofas"}}], "tags": []}})

        entry = CLIENT.assets(PLAYGROUND_SPACE, 'master').find('56PfMcxCLyzuXP3k7k0yL5')
        self.assertEqual(len(entry._metadata['concepts']), 1)
