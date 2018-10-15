try:
    import simplejson as json
except ImportError:
    import json

import dateutil.parser
from .utils import unicode_class

"""
contentful_management.content_type_field_types
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the field coercion classes.

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class BasicField(object):
    """
    Base coercion class.
    """

    def __init__(self, items=None):
        self._items = items

    def coerce(self, value):
        """
        Just returns the value.
        """

        return value

    def __repr__(self):
        return "<{0}>".format(
            self.__class__.__name__
        )


class SymbolField(BasicField):
    """
    Symbol coercion class.
    """

    def coerce(self, value):
        """
        Coerces value to str.
        """

        return unicode_class()(value)


class TextField(SymbolField):
    """
    Text coercion class.
    """
    pass


class IntegerField(BasicField):
    """
    Integer coercion class.
    """

    def coerce(self, value):
        """
        Coerces value to int.
        """

        return int(value) if value is not None else None


class NumberField(BasicField):
    """
    Number coercion class.
    """

    def coerce(self, value):
        """
        Coerces value to float.
        """

        return float(value) if value is not None else None


class DateField(BasicField):
    """
    Date coercion class.
    """

    def coerce(self, value):
        """
        Coerces ISO8601 date to :class:`datetime.datetime` object.
        """

        return dateutil.parser.parse(value)


class BooleanField(BasicField):
    """
    Boolean coercion class.
    """

    def coerce(self, value):
        """
        Coerces value to boolean.
        """

        return bool(value)


class LinkField(BasicField):
    """
    LinkField

    Nothing should be done here as include resolution is handled within
    entries due to depth handling (explained within Entry).
    Only present as a placeholder for proper resolution within ContentType.
    """
    pass


class ArrayField(BasicField):
    """
    Array coercion class.

    Coerces items in collection with it's proper coercion class.
    """

    def __init__(self, items=None):
        super(ArrayField, self).__init__(items)
        self._coercion = self._get_coercion()

    def coerce(self, value):
        """
        Coerces array items with proper coercion.
        """

        result = []
        for v in value:
            result.append(self._coercion.coerce(v))
        return result

    def _get_coercion(self):
        return globals()["{0}Field".format(self._items.get('type'))]()


class ObjectField(BasicField):
    """
    Object coercion class.
    """

    def coerce(self, value):
        """
        Coerces value to JSON.
        """

        return json.loads(json.dumps(value))


class LocationField(BasicField):
    """
    Location coercion class.
    """

    def coerce(self, value):
        """
        Coerces value to location hash.
        """

        return {
            'lat': float(value.get('lat', value.get('latitude'))),
            'lon': float(value.get('lon', value.get('longitude')))
        }


class RichTextField(BasicField):
    """
    Rich Text coercion class.
    """

    def coerce(self, value):
        """
        Returns the rich text object as is.
        Include resolution and other particular processing is done for CDA only.
        """

        return value
