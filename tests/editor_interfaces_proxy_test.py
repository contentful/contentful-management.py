from unittest import TestCase
from contentful_management.editor_interfaces_proxy import EditorInterfacesProxy
from .test_helper import CLIENT, PLAYGROUND_SPACE


class EditorInterfacesProxyTest(TestCase):
    def test_editor_interfaces_proxy(self):
        proxy = EditorInterfacesProxy(CLIENT, PLAYGROUND_SPACE, 'master', 'foo')

        self.assertEqual(str(proxy), "<EditorInterfacesProxy space_id='{0}' environment_id='master' content_type_id='foo'>".format(PLAYGROUND_SPACE))

    def test_editor_interfaces_proxy_not_supported_methods(self):
        proxy = EditorInterfacesProxy(CLIENT, PLAYGROUND_SPACE)

        with self.assertRaises(Exception):
            proxy.create()

        with self.assertRaises(Exception):
            proxy.delete()
