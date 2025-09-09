import pymongo
from CRUD_mongo.mongo_config import HOST, PORT, DATA_BASE, MONGO_COLLECTION
from logger import Logger


class GetCollection:
    def __init__(self):
        self.HOST = HOST
        self.PORT = PORT
        self.DATABASE = DATA_BASE
        self.COLLECTION = MONGO_COLLECTION
        self.URL = f'{self.HOST}:{self.PORT}'
        self.logger = Logger.get_logger()

        self.logger = Logger.get_logger()

        self.client = pymongo.MongoClient(self.URL)
        self.db = self.client[self.DATABASE]
        self.collection = self.db[self.COLLECTION]

    def get_collection(self):
        try:
            doc = self.collection.find({})
            self.logger.info('the collection is load')
            return list(doc)
        except:
            self.logger.error('the collection is not load')
            return None

    def get_doc(self, id):
        try:
            doc = self.collection.find_one({"unique_id": id })
            # self.logger.info(f"the document with {id}  is found")
            print(doc)
            return doc
        except :
            self.logger.error(f"Document with unique_id {id} not found")



# get = GetCollection()
# get_doc = list(get.get_collection())
# print(len(get_doc))
# coll = get.get_doc("4745e1a6-94be-5b93-9f92-3f9b066d9945")
# print(coll['binary_data'])
# print(coll)