import os
from contentful_management import Client

PLAYGROUND_KEY = os.environ.get('CF_TEST_CMA_TOKEN', 'foobar')
PLAYGROUND_SPACE = 'facgnwwgj5fe'
PLAYGROUND_ORG = 'some_org'
CLIENT = Client(PLAYGROUND_KEY, gzip_encoded=False)
