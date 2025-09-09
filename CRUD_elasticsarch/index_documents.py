from logger import Logger
from elasticsearch import Elasticsearch
from CRUD_elasticsarch.config import HOST, INDEX_NAME


class IndexElasticsearch:
    def __init__(self):
        self.es = Elasticsearch(HOST)
        self.INDEX_NAME = INDEX_NAME
        self.logger = Logger.get_logger()

    def index_doc(self,doc,id_field=None):
        if not self.es.indices.exists(index=self.INDEX_NAME):
            self.es.indices.create(index=self.INDEX_NAME)
            self.logger.info("Index created in elasticsearch")
        try:
            res = self.es.index(index=self.INDEX_NAME,id=id_field,document=doc)
            self.logger.info('the doc has been indexed in elasticsearch')
        except:
            self.logger.error('the doc has not been indexed in elasticsearch')

    def index_documents(self, new_index,docs,id_field=None):
        if not self.es.indices.exists(index=self.INDEX_NAME):
            self.es.indices.create(index=self.INDEX_NAME)
            self.es.index(index=INDEX_NAME, id=id_field, body=docs)

    def update_doc(self,unique_id,new_field,new_text):
        self.es.update(
            index=self.INDEX_NAME,
            id=unique_id,
            doc={new_field: new_text}
        )

# docs = [{'title': 'document 1', "content": "content 1"},
#     {'title': 'document 2', "content": "content 2"},
#     {'title': 'document 3', "content": "content 3"}]
# doc = [{'a':1,'b':2},{'a':3,'b':4}]
# a = IndexElasticsearch()
# a.index_doc('new_ind',doc)