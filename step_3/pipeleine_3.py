from CRUD_mongo.find_mongodb import GetCollection

mongo = GetCollection()


def run():
    collect = mongo.get_collection()
    with collect:

