from elasticsearch import Elasticsearch
from CRUD_elasticsarch.config import HOST, INDEX_NAME


class IndexElasticsearch:
    def __init__(self):
        self.es = Elasticsearch(HOST)
        self.INDEX_NAME = INDEX_NAME

    def index_doc(self,new_index,doc,id_field=None):
        if not self.es.indices.exists(index=self.INDEX_NAME):
            self.es.indices.create(index=self.INDEX_NAME)
            self.es.index(index=INDEX_NAME,id='25',body=doc)
            # if i % 100 == 0:
            #     print(f'{i} docs indexed')

# docs = [{'title': 'document 1', "content": "content 1"},
#     {'title': 'document 2', "content": "content 2"},
#     {'title': 'document 3', "content": "content 3"}]
doc = [{'a':1,'b':2},{'a':3,'b':4}]
a = IndexElasticsearch()
a.index_doc('new_ind',doc)