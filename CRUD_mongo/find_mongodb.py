import pymongo
import os
from bson.objectid import ObjectId

class GetCollection:
    def __init__(self):
        self.HOST = os.environ.get("MONGO_HOST", "localhost")
        self.PORT = int(os.environ.get("MONGO_PORT", 27017))
        self.DATABASE = os.environ.get("MONGO_DATABASE", "weak_12")
        self.COLLECTION = os.environ.get("MONGO_COLLECTION", "new_tweets_antisemitic")
        self.URL = f"mongodb://{self.HOST}:{self.PORT}/"

        self.client = pymongo.MongoClient(self.URL)
        self.db = self.client[self.DATABASE]
        self.collection = self.db[self.COLLECTION]

    def get_collection(self):
        return list(self.collection.find({}))

    def get_doc(self, id):
        try:
            return self.collection.find_one({"_id": ObjectId(id)})
        except Exception as e:
            return {"error": str(e)}
