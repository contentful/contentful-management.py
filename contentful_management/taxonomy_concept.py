from .resource import Resource


class TaxonomyConcept(Resource):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/taxonomy/concept
    """

    def __init__(self, item, **kwargs):
        super(TaxonomyConcept, self).__init__(item, **kwargs)
        self.uri = item.get('uri', '')
        self.pref_label = item.get('prefLabel', {})
        self.alt_labels = item.get('altLabels', {})
        self.hidden_labels = item.get('hiddenLabels', {})
        self.notations = item.get('notations', [])
        self.note = item.get('note', {})
        self.change_note = item.get('changeNote', {})
        self.definition = item.get('definition', {})
        self.editorial_note = item.get('editorialNote', {})
        self.example = item.get('example', {})
        self.history_note = item.get('historyNote', {})
        self.scope_note = item.get('scopeNote', {})
        self.broader = item.get('broader', [])
        self.related = item.get('related', [])
        self.concept_schemes = item.get('conceptSchemes', [])

    @classmethod
    def create_attributes(klass, attributes, previous_object=None):
        """
        Attributes for taxonomy concept creation.
        """
        if previous_object is not None:
            attributes_map = {
                'uri': attributes.get('uri', previous_object.uri),
                'prefLabel': attributes.get('prefLabel', previous_object.pref_label),
                'altLabels': attributes.get('altLabels', previous_object.alt_labels),
                'hiddenLabels': attributes.get('hiddenLabels', previous_object.hidden_labels),
                'notations': attributes.get('notations', previous_object.notations),
                'note': attributes.get('note', previous_object.note),
                'changeNote': attributes.get('changeNote', previous_object.change_note),
                'definition': attributes.get('definition', previous_object.definition),
                'editorialNote': attributes.get('editorialNote', previous_object.editorial_note),
                'example': attributes.get('example', previous_object.example),
                'historyNote': attributes.get('historyNote', previous_object.history_note),
                'scopeNote': attributes.get('scopeNote', previous_object.scope_note),
                'broader': attributes.get('broader', previous_object.broader),
                'related': attributes.get('related', previous_object.related),
                'conceptSchemes': attributes.get('conceptSchemes', previous_object.concept_schemes)
            }
        else:
            attributes_map = {
                'uri': attributes.get('uri', ''),
                'prefLabel': attributes.get('prefLabel', {}),
                'altLabels': attributes.get('altLabels', {}),
                'hiddenLabels': attributes.get('hiddenLabels', {}),
                'notations': attributes.get('notations', []),
                'note': attributes.get('note', {}),
                'changeNote': attributes.get('changeNote', {}),
                'definition': attributes.get('definition', {}),
                'editorialNote': attributes.get('editorialNote', {}),
                'example': attributes.get('example', {}),
                'historyNote': attributes.get('historyNote', {}),
                'scopeNote': attributes.get('scopeNote', {}),
                'broader': attributes.get('broader', []),
                'related': attributes.get('related', []),
                'conceptSchemes': attributes.get('conceptSchemes', [])
            }

        if 'uri' in attributes_map and not attributes_map['uri']:
            del attributes_map['uri']

        return attributes_map

    def to_json(self):
        """
        Returns the JSON representation of the taxonomy concept.
        """

        result = super(TaxonomyConcept, self).to_json()
        result.update({
            'uri': self.uri,
            'prefLabel': self.pref_label,
            'altLabels': self.alt_labels,
            'hiddenLabels': self.hidden_labels,
            'notations': self.notations,
            'note': self.note,
            'changeNote': self.change_note,
            'definition': self.definition,
            'editorialNote': self.editorial_note,
            'example': self.example,
            'historyNote': self.history_note,
            'scopeNote': self.scope_note,
            'broader': self.broader,
            'related': self.related,
            'conceptSchemes': self.concept_schemes
        })
        return result

    def __repr__(self):
        return f"<TaxonomyConcept id='{self.sys.get('id', '')}'>"
