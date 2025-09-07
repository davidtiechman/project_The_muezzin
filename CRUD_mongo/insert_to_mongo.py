import logging
import os
import pymongo

class InsertToMongo:
    def __init__(self):
        self.HOST = os.environ.get("MONGO_HOST", "localhost")
        self.PORT = int(os.environ.get("MONGO_PORT", 27017))
        self.DATABASE = os.environ.get("MONGO_DATABASE", "weak_12")
        self.COLLECTION = os.environ.get("MONGO_COLLECTION", "new_tweets_antisemitic")
        self.URL = f"mongodb://{self.HOST}:{self.PORT}/"

        self.client = pymongo.MongoClient(self.URL)
        self.db = self.client[self.DATABASE]
        self.collection = self.db[self.COLLECTION]

    def insert_collection_to_mongo(self,collection):
        self.collection.insert_many(collection)
        print('the collection has been inserted')
        logging.info('the collection has been inserted')

    def update_collection_to_mongo(self,id,document):
        self.collection.update_one({'_id':id},{'$set':document})
        print('the collection has been updated')
        logging.info('the collection has been updated')

    def delete_collection_to_mongo(self,id):
        self.collection.delete_one({'_id':id})
        print('the collection has been deleted')
        logging.info('the collection has been deleted')

# run = run_pipeline()
# a = InsertToMongo()
# a.insert_collection_to_mongo(run)

