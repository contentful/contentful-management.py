from .client_proxy import ClientProxy
from .taxonomy_concept_scheme import TaxonomyConceptScheme


class TaxonomyConceptSchemesProxy(ClientProxy):
    """
    API reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/taxonomy/concept-scheme
    """
    @property
    def _resource_class(self):
        return TaxonomyConceptScheme

    def __init__(self, client, organization_id):
        super(TaxonomyConceptSchemesProxy, self).__init__(client, None)
        self.organization_id = organization_id

    def total(self, **kwargs):
        """
        Gets the total number of taxonomy concept schemes.
        """
        url = f"organizations/{self.organization_id}/taxonomy/concept-schemes/total"
        response = self.client._http_get(url, {}, **kwargs)
        return response.json()

    def find(self, concept_scheme_id, **kwargs):
        """
        Finds a taxonomy concept scheme.
        """
        return super(TaxonomyConceptSchemesProxy, self).find(concept_scheme_id, **kwargs)

    def all(self, query=None, **kwargs):
        """
        Gets all taxonomy concept schemes.
        """
        return super(TaxonomyConceptSchemesProxy, self).all(query=query)

    def create(self, resource_id=None, attributes=None, **kwargs):
        """
        Creates a taxonomy concept scheme with an optional user-defined ID.
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

    def update(self, concept_scheme_id, version, attributes):
        """
        Updates a taxonomy concept scheme.
        """
        return self.client._patch(
            self._url(resource_id=concept_scheme_id),
            attributes,
            headers={
                'X-Contentful-Version': str(version),
                'Content-Type': 'application/json-patch+json'
            }
        )

    def delete(self, concept_scheme_id, version):
        """
        Deletes a taxonomy concept scheme.
        """
        return self.client._delete(
            self._url(resource_id=concept_scheme_id),
            headers={'X-Contentful-Version': str(version)}
        )

    def _url(self, resource_id=None, **kwargs):
        if resource_id is None:
            return f"organizations/{self.organization_id}/taxonomy/concept-schemes"
        return f"organizations/{self.organization_id}/taxonomy/concept-schemes/{resource_id}"

    def __repr__(self):
        return f"<TaxonomyConceptSchemesProxy organization_id='{self.organization_id}'>"
