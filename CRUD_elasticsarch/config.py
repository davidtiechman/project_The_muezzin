from os import getenv
HOST = getenv ('ELASTICSEARCH_HOST', 'http://localhost:9200')
PORT = getenv ('ELASTICSEARCH_PORT', '9200')
# COLLECTION = getenv ('ELASTICSEARCH_COLLECTION', 'referenses to files')
INDEX_NAME = getenv ('ELASTICSEARCH_INDEX_NAME', 'reference-to-files')