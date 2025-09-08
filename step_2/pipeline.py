from CRUD_elasticsarch.index_documents import IndexElasticsearch
from CRUD_mongo.insert_to_mongo import InsertToMongo
from load_audio.unique_id import unique_a_id
from publicher_to_kafka.subscriber_with_kafka import SubscriberWithKafka


def run():
    sub = SubscriberWithKafka()
    file = sub.read_messages()
    el = IndexElasticsearch()
    for fi in file:
        fi['uinque_id'] = unique_a_id(fi['size']+fi['name_file'])
        el.index_doc(fi,fi['uinque_id'])

    #                     'created': file['created'], 'size': file['size']})
    # mong = InsertToMongo()
    # mong.insert_cdc_to_mongo(file)
run()