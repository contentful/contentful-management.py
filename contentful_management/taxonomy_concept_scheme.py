from .resource import Resource


class TaxonomyConceptScheme(Resource):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/taxonomy/concept-scheme
    """

    def __init__(self, item, **kwargs):
        super(TaxonomyConceptScheme, self).__init__(item, **kwargs)
        self.uri = item.get('uri', '')
        self.pref_label = item.get('prefLabel', {})
        self.definition = item.get('definition', {})
        self.top_concepts = item.get('topConcepts', [])
        self.concepts = item.get('concepts', [])
        self.total_concepts = item.get('totalConcepts', 0)

    @classmethod
    def create_attributes(klass, attributes, previous_object=None):
        """
        Attributes for taxonomy concept scheme creation.
        """
        if previous_object is not None:
            attributes_map = {
                'uri': attributes.get('uri', previous_object.uri),
                'prefLabel': attributes.get('prefLabel', previous_object.pref_label),
                'definition': attributes.get('definition', previous_object.definition),
                'topConcepts': attributes.get('topConcepts', previous_object.top_concepts),
                'concepts': attributes.get('concepts', previous_object.concepts)
            }
        else:
            attributes_map = {
                'uri': attributes.get('uri', ''),
                'prefLabel': attributes.get('prefLabel', {}),
                'definition': attributes.get('definition', {}),
                'topConcepts': attributes.get('topConcepts', []),
                'concepts': attributes.get('concepts', [])
            }

        if 'uri' in attributes_map and not attributes_map['uri']:
            del attributes_map['uri']

        return attributes_map

    def to_json(self):
        """
        Returns the JSON representation of the taxonomy concept scheme.
        """

        result = super(TaxonomyConceptScheme, self).to_json()
        result.update({
            'uri': self.uri,
            'prefLabel': self.pref_label,
            'definition': self.definition,
            'topConcepts': self.top_concepts,
            'concepts': self.concepts,
            'totalConcepts': self.total_concepts
        })
        return result

    def __repr__(self):
        return f"<TaxonomyConceptScheme id='{self.sys.get('id', '')}'>"
