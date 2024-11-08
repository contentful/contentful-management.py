import vcr
from unittest import TestCase
from contentful_management.ui_extension import UIExtension
from contentful_management.errors import NotFoundError
from .test_helper import CLIENT, PLAYGROUND_SPACE

UI_EXTENSION_ITEM_SRC = {
    "extension": {
        "src": "https://example.com/my",
        "name": "My awesome extension",
        "fieldTypes": [
            {
                "type": "Symbol"
            },
            {
                "type": "Text"
            }
        ],
        "sidebar": False
    },
    "sys": {
        "id": "0xvkPW9FdQ1kkWlWZ8ga4x",
        "type": "Extension",
        "version": 1,
        "space": {
            "sys": {
                "type": "Link",
                "linkType": "Space",
                "id": "yadj1kx9rmg0"
            }
        },
        "createdAt": "2015-05-18T11:29:46.809Z",
        "createdBy": {
            "sys": {
                "type": "Link",
                "linkType": "User",
                "id": "4FLrUHftHW3v2BLi9fzfjU"
            }
        },
        "updatedAt": "2015-05-18T11:29:46.809Z",
        "updatedBy": {
            "sys": {
                "type": "Link",
                "linkType": "User",
                "id": "4FLrUHftHW3v2BLi9fzfjU"
            }
        }
    }
}

UI_EXTENSION_ITEM_SRCDOC = {
    "extension": {
        "srcdoc": "<html>foobar</html>",
        "name": "My awesome extension",
        "fieldTypes": [
            {
                "type": "Symbol"
            },
            {
                "type": "Text"
            }
        ],
        "sidebar": False
    },
    "sys": {
        "id": "0xvkPW9FdQ1kkWlWZ8ga4x",
        "type": "Extension",
        "version": 1,
        "space": {
            "sys": {
                "type": "Link",
                "linkType": "Space",
                "id": "yadj1kx9rmg0"
            }
        },
        "createdAt": "2015-05-18T11:29:46.809Z",
        "createdBy": {
            "sys": {
                "type": "Link",
                "linkType": "User",
                "id": "4FLrUHftHW3v2BLi9fzfjU"
            }
        },
        "updatedAt": "2015-05-18T11:29:46.809Z",
        "updatedBy": {
            "sys": {
                "type": "Link",
                "linkType": "User",
                "id": "4FLrUHftHW3v2BLi9fzfjU"
            }
        }
    }
}


class UIExtensionTest(TestCase):
    def test_ui_extension(self):
        ui_extension_src = UIExtension(UI_EXTENSION_ITEM_SRC)

        self.assertEqual(str(ui_extension_src), "<UIExtension[My awesome extension] id='0xvkPW9FdQ1kkWlWZ8ga4x' field_types=['Symbol', 'Text']>")

    def test_ui_extension_extension_getters(self):
        ui_extension_src = UIExtension(UI_EXTENSION_ITEM_SRC)

        self.assertEqual(ui_extension_src.name, "My awesome extension")
        self.assertEqual(ui_extension_src.field_types, [{'type': 'Symbol'}, {'type': 'Text'}])
        self.assertEqual(ui_extension_src.source, 'https://example.com/my')
        self.assertFalse(ui_extension_src.sidebar)

        ui_extension_srcdoc = UIExtension(UI_EXTENSION_ITEM_SRCDOC)

        self.assertEqual(ui_extension_srcdoc.name, "My awesome extension")
        self.assertEqual(ui_extension_srcdoc.field_types, [{'type': 'Symbol'}, {'type': 'Text'}])
        self.assertEqual(ui_extension_srcdoc.source, '<html>foobar</html>')
        self.assertFalse(ui_extension_srcdoc.sidebar)

    def test_ui_extension_extension_setters(self):
        ui_extension_src = UIExtension(UI_EXTENSION_ITEM_SRC)

        ui_extension_src.name = 'foo'
        self.assertEqual(ui_extension_src.extension['name'], "foo")

        ui_extension_src.field_types = [{'type': 'Symbol'}]
        self.assertEqual(ui_extension_src.extension['fieldTypes'], [{'type': 'Symbol'}])

        ui_extension_src.source = 'https://contentful.com/ui_ext'
        self.assertEqual(ui_extension_src.extension['src'], 'https://contentful.com/ui_ext')

        ui_extension_src.sidebar = True
        self.assertTrue(ui_extension_src.extension['sidebar'])

        ui_extension_srcdoc = UIExtension(UI_EXTENSION_ITEM_SRCDOC)

        ui_extension_srcdoc.source = '<html>foo</html>'
        self.assertEqual(ui_extension_srcdoc.extension['srcdoc'], '<html>foo</html>')

    def test_ui_extension_to_json(self):
        ui_extension_src = UIExtension(UI_EXTENSION_ITEM_SRC)

        self.assertEqual(ui_extension_src.to_json(), {
            "extension": {
                "src": "https://example.com/my",
                "name": "My awesome extension",
                "fieldTypes": [
                    {
                        "type": "Symbol"
                    },
                    {
                        "type": "Text"
                    }
                ],
                "sidebar": False
            },
            "sys": {
                "id": "0xvkPW9FdQ1kkWlWZ8ga4x",
                "type": "Extension",
                "version": 1,
                "space": {
                    "sys": {
                        "type": "Link",
                        "linkType": "Space",
                        "id": "yadj1kx9rmg0"
                    }
                },
                "createdAt": "2015-05-18T11:29:46.809000+00:00",
                "createdBy": {
                    "sys": {
                        "type": "Link",
                        "linkType": "User",
                        "id": "4FLrUHftHW3v2BLi9fzfjU"
                    }
                },
                "updatedAt": "2015-05-18T11:29:46.809000+00:00",
                "updatedBy": {
                    "sys": {
                        "type": "Link",
                        "linkType": "User",
                        "id": "4FLrUHftHW3v2BLi9fzfjU"
                    }
                }
            }
        })

        ui_extension_srcdoc = UIExtension(UI_EXTENSION_ITEM_SRCDOC)

        self.assertEqual(ui_extension_srcdoc.to_json(), {
            "extension": {
                "srcdoc": "<html>foobar</html>",
                "name": "My awesome extension",
                "fieldTypes": [
                    {
                        "type": "Symbol"
                    },
                    {
                        "type": "Text"
                    }
                ],
                "sidebar": False
            },
            "sys": {
                "id": "0xvkPW9FdQ1kkWlWZ8ga4x",
                "type": "Extension",
                "version": 1,
                "space": {
                    "sys": {
                        "type": "Link",
                        "linkType": "Space",
                        "id": "yadj1kx9rmg0"
                    }
                },
                "createdAt": "2015-05-18T11:29:46.809000+00:00",
                "createdBy": {
                    "sys": {
                        "type": "Link",
                        "linkType": "User",
                        "id": "4FLrUHftHW3v2BLi9fzfjU"
                    }
                },
                "updatedAt": "2015-05-18T11:29:46.809000+00:00",
                "updatedBy": {
                    "sys": {
                        "type": "Link",
                        "linkType": "User",
                        "id": "4FLrUHftHW3v2BLi9fzfjU"
                    }
                }
            }
        })

    def test_ui_extension_to_link(self):
        ui_extension = UIExtension(UI_EXTENSION_ITEM_SRC)

        self.assertEqual(ui_extension.to_link().to_json(), {
            'sys': {
                'id': '0xvkPW9FdQ1kkWlWZ8ga4x',
                'type': 'Link',
                'linkType': 'Extension'
            }
        })

    @vcr.use_cassette('fixtures/ui_extensions/all.yaml', decode_compressed_response=True)
    def test_ui_extensions_all(self):
        ui_extensions = CLIENT.ui_extensions('arqlnkt58eul', 'master').all()

        self.assertTrue(ui_extensions)
        self.assertEqual(str(ui_extensions[0]), "<UIExtension[My awesome extension by srcDoc] id='2ZJduY1pKEma6G8Y2ImqYU' field_types=['Symbol', 'Text']>")
        self.assertEqual(ui_extensions[0].source, ui_extensions[0].extension['srcdoc'])

        self.assertEqual(str(ui_extensions[2]), "<UIExtension[Hello World Editor] id='hello-world' field_types=['Text']>")
        self.assertEqual(ui_extensions[2].source, ui_extensions[2].extension['src'])

    @vcr.use_cassette('fixtures/ui_extensions/find.yaml', decode_compressed_response=True)
    def test_ui_extensions_find(self):
        ui_extension = CLIENT.ui_extensions('arqlnkt58eul', 'master').find('2ZJduY1pKEma6G8Y2ImqYU')

        self.assertEqual(str(ui_extension), "<UIExtension[My awesome extension by srcDoc] id='2ZJduY1pKEma6G8Y2ImqYU' field_types=['Symbol', 'Text']>")

    @vcr.use_cassette('fixtures/ui_extensions/create.yaml', decode_compressed_response=True)
    def test_ui_extensions_create(self):
        ui_extension = CLIENT.ui_extensions(PLAYGROUND_SPACE, 'master').create('test-extension', {
            "extension": {
                "name": "Test Extension",
                "srcdoc": "<html>foobar</html>",
                "fieldTypes": [{'type': 'Symbol'}],
                "sidebar": False
            }
        })

        self.assertEqual(str(ui_extension), "<UIExtension[Test Extension] id='test-extension' field_types=['Symbol']>")

    @vcr.use_cassette('fixtures/ui_extensions/find_2.yaml', decode_compressed_response=True)
    def test_ui_extensions_update(self):
        ui_extension = CLIENT.ui_extensions(PLAYGROUND_SPACE, 'master').find('test-extension')

        self.assertEqual(str(ui_extension), "<UIExtension[Test Extension] id='test-extension' field_types=['Symbol']>")

        with vcr.use_cassette('fixtures/ui_extensions/update.yaml'):
            ui_extension.name = 'Update Test Extension'
            ui_extension.save()

        with vcr.use_cassette('fixtures/ui_extensions/find_3.yaml', decode_compressed_response=True):
            ui_extension = CLIENT.ui_extensions(PLAYGROUND_SPACE, 'master').find('test-extension')
            self.assertEqual(str(ui_extension), "<UIExtension[Update Test Extension] id='test-extension' field_types=['Symbol']>")

    @vcr.use_cassette('fixtures/ui_extensions/find_3.yaml', decode_compressed_response=True)
    def test_ui_extensions_delete(self):
        ui_extension = CLIENT.ui_extensions(PLAYGROUND_SPACE, 'master').find('test-extension')

        with vcr.use_cassette('fixtures/ui_extensions/delete.yaml'):
            ui_extension.delete()

        with vcr.use_cassette('fixtures/ui_extensions/not_found.yaml'):
            with self.assertRaises(NotFoundError):
                CLIENT.ui_extensions(PLAYGROUND_SPACE, 'master').find('test-extension')

    @vcr.use_cassette('fixtures/ui_extensions/create_with_parameters.yaml', decode_compressed_response=True)
    def test_ui_extensions_create_with_parameters(self):
        ui_extension = CLIENT.ui_extensions(PLAYGROUND_SPACE, 'master').create('test-with-parameters', {
            "extension": {
                "name": "Test Extension with Parameters",
                "srcdoc": "<html>foobar</html>",
                "fieldTypes": [{'type': 'Symbol'}],
                "sidebar": False,
                "parameters": {
                    "installation": [
                        {
                            "id": "devMode",
                            "type": "Boolean",
                            "name": "Run in development mode"
                        },
                        {
                            "id": "retries",
                            "type": "Number",
                            "name": "Number of retries for API calls",
                            "required": True,
                            "default": 3
                        }
                    ],
                    "instance": [
                        {
                            "id": "helpText",
                            "type": "Symbol",
                            "name": "Help text",
                            "description": "Help text for a user to help them understand the editor"
                        },
                        {
                            "id": "theme",
                            "type": "Enum",
                            "name": "Theme",
                            "options": [{"light": "Solarized light"}, {"dark": "Solarized dark"}],
                            "default": "light",
                            "required": True
                        }
                    ]
                }
            }
        })

        self.assertTrue(ui_extension.parameters)
        self.assertEqual(ui_extension.parameters, {
            "installation": [
                {
                    "id": "devMode",
                    "type": "Boolean",
                    "name": "Run in development mode"
                },
                {
                    "id": "retries",
                    "type": "Number",
                    "name": "Number of retries for API calls",
                    "required": True,
                    "default": 3
                }
            ],
            "instance": [
                {
                    "id": "helpText",
                    "type": "Symbol",
                    "name": "Help text",
                    "description": "Help text for a user to help them understand the editor"
                },
                {
                    "id": "theme",
                    "type": "Enum",
                    "name": "Theme",
                    "options": [{"light": "Solarized light"}, {"dark": "Solarized dark"}],
                    "default": "light",
                    "required": True
                }
            ]
        })
