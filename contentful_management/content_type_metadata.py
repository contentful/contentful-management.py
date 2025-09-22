"""
contentful_management.content_type_metadata
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the ContentTypeMetadata class.

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class ContentTypeMetadata(object):
    """
    Represents metadata for a content type.
    """

    def __init__(self, metadata_data):
        self.raw = metadata_data
        self.taxonomy = self._hydrate_taxonomy(metadata_data.get('taxonomy', []))

        # Add other metadata fields as-is for future extensibility
        for key, value in metadata_data.items():
            if key != 'taxonomy':
                setattr(self, key, value)

    def _hydrate_taxonomy(self, taxonomy_data):
        """
        Hydrates taxonomy with proper object types.
        """
        from .taxonomy_concept import TaxonomyConcept
        from .taxonomy_concept_scheme import TaxonomyConceptScheme

        taxonomy_objects = []
        for taxonomy in taxonomy_data:
            link_type = taxonomy.get('sys', {}).get('linkType')
            if link_type == 'TaxonomyConcept':
                taxonomy_objects.append(TaxonomyConcept(taxonomy))
            elif link_type == 'TaxonomyConceptScheme':
                taxonomy_objects.append(TaxonomyConceptScheme(taxonomy))
        return taxonomy_objects

    def to_json(self):
        """
        Returns the JSON representation of the content type metadata.
        """
        result = {}

        # Handle taxonomy specially
        if self.taxonomy:
            taxonomy_links = []
            for t in self.taxonomy:
                taxonomy_link = {
                    'sys': t.sys
                }
                # Try to get the required field from raw data if it exists
                if hasattr(t, 'raw') and 'required' in t.raw:
                    taxonomy_link['required'] = t.raw['required']
                taxonomy_links.append(taxonomy_link)
            result['taxonomy'] = taxonomy_links

        # Add other metadata fields
        for key, value in self.raw.items():
            if key != 'taxonomy':
                result[key] = value

        return result

    def __repr__(self):
        return "<ContentTypeMetadata taxonomy_count='{0}'>".format(
            len(self.taxonomy) if self.taxonomy else 0
        )
