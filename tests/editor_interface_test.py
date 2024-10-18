import vcr
from unittest import TestCase
from contentful_management.editor_interface import EditorInterface
from .test_helper import CLIENT, PLAYGROUND_SPACE


EDITOR_INTERFACE_DATA = {
    'sys': {
        'id': 'default',
        'type': 'EditorInterface'
    },
    'controls': [
        {
          "widgetId": "singleLine",
          "fieldId": "name",
          "settings": {}
        }
    ]
}


class EditorInterfaceTest(TestCase):
    def test_editor_interface(self):
        editor_interface = EditorInterface(EDITOR_INTERFACE_DATA)

        self.assertEqual(str(editor_interface), "<EditorInterface id='default'>")

    def test_editor_interface_to_json(self):
        editor_interface = EditorInterface(EDITOR_INTERFACE_DATA)

        self.assertEqual(editor_interface.to_json(), {
            'sys': {
                'id': 'default',
                'type': 'EditorInterface'
            },
            'controls': [
                {
                    "widgetId": "singleLine",
                    "fieldId": "name",
                    "settings": {}
                }
            ]
        })

    @vcr.use_cassette('fixtures/editor_interface/find.yaml', decode_compressed_response=True)
    def test_editor_interface_update(self):
        editor_interface = CLIENT.editor_interfaces(PLAYGROUND_SPACE, 'master', 'foo').find()

        self.assertEqual(editor_interface.controls[0]['widgetId'], 'multiLine')

        with vcr.use_cassette('fixtures/editor_interface/update.yaml'):
            editor_interface.controls[0]['widgetId'] = 'singleLine'
            editor_interface.save()

        self.assertEqual(editor_interface.controls[0]['widgetId'], 'singleLine')
