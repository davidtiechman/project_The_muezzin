import logging
import os
import pymongo
from logger import Logger
from CRUD_mongo.mongo_config import DATA_BASE, MONGO_COLLECTION, HOST, PORT


class InsertToMongo:
    def __init__(self):
        self.HOST = HOST
        self.PORT = PORT
        self.DATABASE = DATA_BASE
        self.COLLECTION = MONGO_COLLECTION
        self.URL = f'{self.HOST}:{self.PORT}'
        self.logger = Logger.get_logger()

        self.client = pymongo.MongoClient(self.URL)
        self.db = self.client[self.DATABASE]
        self.collection = self.db[self.COLLECTION]

    def insert_collection_to_mongo(self,collection):
        try:
            self.collection.insert_many(collection)
            self.logger.info('the collection has been inserted in mongodb')
        except:
            self.logger.error('not cant insert collection to mongo')
    def insert_doc_to_mongo(self,doc):
        try:
            self.collection.insert_one(doc)
            self.logger.info('the doc has been inserted in mongodb')
        except:
            self.logger.error('not cant insert doc to mongo')

    def update_collection_to_mongo(self,id,document):
        self.collection.update_one({'_id':id},{'$set':document})
        print('the collection has been updated')
        logging.info('the collection has been updated')

    def delete_collection_to_mongo(self,id):
        self.collection.delete_one({'_id':id})
        print('the collection has been deleted')
        logging.info('the collection has been deleted')

# # run = run_pipeline()
# doc = {'name':'david'}
# a = InsertToMongo()
# a.insert_doc_to_mongo(1,doc)

