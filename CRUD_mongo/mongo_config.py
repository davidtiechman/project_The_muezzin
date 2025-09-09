from os import getenv
HOST = getenv ('MONGO_HOST','localhost')
PORT = getenv ('MONGO_PORT','27018')
# COLLECTION = getenv ('ELASTICSEARCH_COLLECTION', 'referenses to files')
DATA_BASE = getenv ('MONGO_DB', 'project_IDF')
MONGO_COLLECTION = getenv ('MONGO_COLLECTION', 'reference')