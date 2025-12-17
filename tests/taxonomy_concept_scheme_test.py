import vcr
from unittest import TestCase
from contentful_management.errors import NotFoundError
from contentful_management.taxonomy_concept_scheme import TaxonomyConceptScheme
from .test_helper import CLIENT, PLAYGROUND_ORG

TAXONOMY_CONCEPT_SCHEME_ITEM = {
    "sys": {
        "id": "homeProducts",
        "type": "TaxonomyConceptScheme",
    },
    "prefLabel": {
        "en-US": "Home Products"
    }
}


class TaxonomyConceptSchemeTest(TestCase):
    def test_taxonomy_concept_scheme(self):
        scheme = TaxonomyConceptScheme(TAXONOMY_CONCEPT_SCHEME_ITEM)
        self.assertEqual(str(scheme), "<TaxonomyConceptScheme id='homeProducts'>")

    @vcr.use_cassette('fixtures/taxonomy/concept_scheme/find.yaml', decode_compressed_response=True)
    def test_find_taxonomy_concept_scheme(self):
        scheme = CLIENT.taxonomy_concept_schemes(PLAYGROUND_ORG).find('homeProducts')
        self.assertEqual(scheme.sys['id'], 'homeProducts')
        self.assertEqual(scheme.pref_label['en-US'], "Home Products")
        self.assertEqual(scheme.total_concepts, 1)

    @vcr.use_cassette('fixtures/taxonomy/concept_scheme/create.yaml', decode_compressed_response=True)
    def test_create_taxonomy_concept_scheme(self):
        scheme_attributes = {
            "prefLabel": {
                "en-US": "Home Products"
            },
            "definition": {
                "en-US": ""
            },
            "topConcepts": [
                {
                    "sys": {
                        "id": "5KHXWlmxvntrrB09szapUp"
                    }
                }
            ],
            "concepts": [
                {
                    "sys": {
                        "id": "5KHXWlmxvntrrB09szapUp"
                    }
                }
            ]
        }

        scheme = CLIENT.taxonomy_concept_schemes(PLAYGROUND_ORG).create(scheme_attributes)
        self.assertEqual(scheme.pref_label['en-US'], 'Home Products')
        self.assertEqual(scheme.top_concepts[0]['sys']['id'], '5KHXWlmxvntrrB09szapUp')
        self.assertEqual(scheme.concepts[0]['sys']['id'], '5KHXWlmxvntrrB09szapUp')

    @vcr.use_cassette('fixtures/taxonomy/concept_scheme/create_with_id.yaml', decode_compressed_response=True)
    def test_create_taxonomy_concept_scheme_with_id(self):
        scheme_attributes = {
            "uri": "",
            "prefLabel": {
                "en-US": "Home Products"
            },
            "definition": {
                "en-US": ""
            }
        }

        scheme = CLIENT.taxonomy_concept_schemes(PLAYGROUND_ORG).create(
            '2s0F7127ajju1AoMaCtE',
            attributes=scheme_attributes
        )
        self.assertEqual(scheme.sys['id'], '2s0F7127ajju1AoMaCtE')
        self.assertEqual(scheme.pref_label['en-US'], 'Home Products')

    @vcr.use_cassette('fixtures/taxonomy/concept_scheme/all.yaml', decode_compressed_response=True)
    def test_all_taxonomy_concept_schemes(self):
        schemes = CLIENT.taxonomy_concept_schemes(PLAYGROUND_ORG).all()
        self.assertEqual(len(schemes), 2)
        self.assertIsInstance(schemes[-1], TaxonomyConceptScheme)
        self.assertEqual(schemes[-1].pref_label['en-US'], 'Home Products')

    @vcr.use_cassette('fixtures/taxonomy/concept_scheme/update.yaml', decode_compressed_response=True)
    def test_update_taxonomy_concept_scheme(self):
        scheme = CLIENT.taxonomy_concept_schemes(PLAYGROUND_ORG).find('homeProducts')

        patches = [
            {
                'op': 'replace',
                'path': '/prefLabel/en-US',
                'value': 'Updated Home Products'
            }
        ]

        updated_scheme = CLIENT.taxonomy_concept_schemes(PLAYGROUND_ORG).update(
            'homeProducts',
            scheme.sys['version'],
            patches
        )

        self.assertEqual(updated_scheme.pref_label['en-US'], 'Updated Home Products')

    @vcr.use_cassette('fixtures/taxonomy/concept_scheme/delete.yaml', decode_compressed_response=True)
    def test_delete_taxonomy_concept_scheme(self):
        scheme = CLIENT.taxonomy_concept_schemes(PLAYGROUND_ORG).find('homeProducts')

        CLIENT.taxonomy_concept_schemes(PLAYGROUND_ORG).delete(
            'homeProducts',
            scheme.sys['version']
        )

        with vcr.use_cassette('fixtures/taxonomy/concept_scheme/not_found.yaml', decode_compressed_response=True):
            with self.assertRaises(NotFoundError):
                CLIENT.taxonomy_concept_schemes(PLAYGROUND_ORG).find('homeProducts')

    @vcr.use_cassette('fixtures/taxonomy/concept_scheme/total.yaml', decode_compressed_response=True)
    def test_get_total_concept_schemes(self):
        response = CLIENT.taxonomy_concept_schemes(PLAYGROUND_ORG).total()

        self.assertIsInstance(response, dict)
        self.assertIn('total', response)
        self.assertIsInstance(response['total'], int)
