import vcr
from unittest import TestCase
from contentful_management.assets_proxy import AssetsProxy
from .test_helper import CLIENT, PLAYGROUND_SPACE


class AssetsProxyTest(TestCase):
    def test_assets_proxy(self):
        proxy = AssetsProxy(CLIENT, PLAYGROUND_SPACE, 'master')

        self.assertEqual(str(proxy), "<AssetsProxy space_id='{0}' environment_id='master'>".format(PLAYGROUND_SPACE))

    @vcr.use_cassette('fixtures/asset/all.yaml', decode_compressed_response=True)
    def test_assets_proxy_all(self):
        proxy = AssetsProxy(CLIENT, PLAYGROUND_SPACE, 'master')

        assets = []

        self.assertFalse(assets)

        assets = proxy.all()

        self.assertTrue(assets)

    @vcr.use_cassette('fixtures/asset/select_operator.yaml', decode_compressed_response=True)
    def test_assets_proxy_select_operator(self):
        proxy = AssetsProxy(CLIENT, PLAYGROUND_SPACE, 'master')

        asset = proxy.all({'select': 'sys'})[0]

        self.assertFalse(asset.fields())
        self.assertTrue(asset.sys)
