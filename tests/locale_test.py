import vcr
from unittest import TestCase
from contentful_management.locale import Locale
from contentful_management.errors import NotFoundError
from .test_helper import CLIENT, PLAYGROUND_SPACE

LOCALE_ITEM = {
    'name': 'Klingon',
    'code': 'tlg',
    'fallbackCode': 'en-US',
    'sys': {
        'id': 'foo',
        'type': 'Locale',
        'space': {
            'sys': {
                'id': 'foobar',
                'type': 'Link',
                'linkType': 'Space'
            }
        }
    }
}

class LocaleTest(TestCase):
    def test_locale(self):
        locale = Locale(LOCALE_ITEM)

        self.assertEqual(str(locale), "<Locale[Klingon] code='tlg' default=False>")

    def test_locale_to_json(self):
        locale = Locale(LOCALE_ITEM)

        self.assertEqual(locale.to_json(), {
            'code': 'tlg',
            'name': 'Klingon',
            'fallbackCode': 'en-US',
            'optional': True,
            'contentDeliveryApi': True,
            'contentManagementApi': True,
            'sys': {
                'id': 'foo',
                'type': 'Locale',
                'space': {
                    'sys': {
                        'id': 'foobar',
                        'type': 'Link',
                        'linkType': 'Space'
                    }
                }
            }
        })

    def test_locale_to_link(self):
        locale = Locale(LOCALE_ITEM)

        self.assertEqual(locale.to_link().to_json(), {
            'sys': {
                'id': 'foo',
                'type': 'Link',
                'linkType': 'Locale'
            }
        })

    @vcr.use_cassette('fixtures/locale/create.yaml')
    def test_create_locale(self):
        locale = CLIENT.locales(PLAYGROUND_SPACE, 'master').create({
            'name': 'Klingon',
            'fallbackCode': 'en-US',
            'code': 'tlg'
        })

        self.assertEqual(locale.name, 'Klingon')
        self.assertEqual(locale.code, 'tlg')

    @vcr.use_cassette('fixtures/locale/find.yaml')
    def test_update_locale(self):
        locale = CLIENT.locales(PLAYGROUND_SPACE, 'master').find('3OFlsZyYYM5fNhCtfFctX8')

        with vcr.use_cassette('fixtures/locale/update.yaml'):
            locale.name = 'Not Klingon'
            locale.save()

        self.assertEqual(locale.name, 'Not Klingon')

    @vcr.use_cassette('fixtures/locale/find_2.yaml')
    def test_delete_locale(self):
        locale = CLIENT.locales(PLAYGROUND_SPACE, 'master').find('3OFlsZyYYM5fNhCtfFctX8')

        with vcr.use_cassette('fixtures/locale/delete.yaml'):
            locale.delete()

        with vcr.use_cassette('fixtures/locale/not_found.yaml'):
            with self.assertRaises(NotFoundError):
                CLIENT.locales(PLAYGROUND_SPACE, 'master').find('3OFlsZyYYM5fNhCtfFctX8')

