from .client_proxy import ClientProxy
from .taxonomy_concept import TaxonomyConcept


class TaxonomyConceptsProxy(ClientProxy):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/taxonomy/concept
    """

    @property
    def _resource_class(self):
        return TaxonomyConcept

    def __init__(self, client, organization_id):
        super(TaxonomyConceptsProxy, self).__init__(client, None)
        self.organization_id = organization_id

    def find(self, concept_id, **kwargs):
        """
        Finds a taxonomy concept.
        """
        return super(TaxonomyConceptsProxy, self).find(concept_id, **kwargs)

    def all(self, query=None, **kwargs):
        """
        Gets all taxonomy concepts.
        """
        return super(TaxonomyConceptsProxy, self).all(query=query)

    def create(self, resource_id=None, attributes=None, **kwargs):
        """
        Creates a taxonomy concept with an optional user-defined ID.
        """
        if attributes is None:
            attributes = {}

        if resource_id is None:
            result = self.client._post(
                self._url(),
                self._resource_class.create_attributes(attributes),
                headers=self._resource_class.create_headers(attributes)
            )
        else:
            result = self.client._put(
                self._url(resource_id=resource_id),
                self._resource_class.create_attributes(attributes),
                headers=self._resource_class.create_headers(attributes)
            )

        return result

    def update(self, concept_id, version, attributes):
        """
        Updates a taxonomy concept.
        """
        return self.client._patch(
            self._url(resource_id=concept_id),
            attributes,
            headers={
                'X-Contentful-Version': str(version),
                'Content-Type': 'application/json-patch+json'
            }
        )

    def delete(self, concept_id, version):
        """
        Deletes a taxonomy concept.
        """
        return self.client._delete(
            self._url(resource_id=concept_id),
            headers={'X-Contentful-Version': str(version)}
        )

    def _url(self, resource_id=None, **kwargs):
        if resource_id is None:
            return f"organizations/{self.organization_id}/taxonomy/concepts"
        return f"organizations/{self.organization_id}/taxonomy/concepts/{resource_id}"

    def descendants(self, concept_id, query=None, **kwargs):
        """
        Gets descendants of a taxonomy concept.
        """
        if query is None:
            query = {}

        url = f"organizations/{self.organization_id}/taxonomy/concepts/{concept_id}/descendants"
        return self.client._get(url, query, **kwargs)

    def ancestors(self, concept_id, query=None, **kwargs):
        """
        Gets ancestors of a taxonomy concept.
        """
        if query is None:
            query = {}

        url = f"organizations/{self.organization_id}/taxonomy/concepts/{concept_id}/ancestors"
        return self.client._get(url, query, **kwargs)

    def total(self, **kwargs):
        """
        Gets the total number of taxonomy concepts.
        """
        url = f"organizations/{self.organization_id}/taxonomy/concepts/total"
        response = self.client._http_get(url, {}, **kwargs)
        return response.json()

    def __repr__(self):
        return f"<TaxonomyConceptsProxy organization_id='{self.organization_id}'>"
