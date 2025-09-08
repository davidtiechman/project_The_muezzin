from CRUD_elasticsarch.index_documents import IndexElasticsearch
from convert_audio_to_binery.convert_audio_to_binary import convert_audio_to_binary
from CRUD_mongo.insert_to_mongo import InsertToMongo
from load_audio.unique_id import unique_a_id
from publicher_to_kafka.subscriber_with_kafka import SubscriberWithKafka


def run():
    sub = SubscriberWithKafka()
    file = sub.read_messages()
    el = IndexElasticsearch()
    mongo = InsertToMongo()
    for fi in file:
        fi['uinque_id'] = unique_a_id(fi['size']+fi['name_file'])
        binary_data = convert_audio_to_binary(fi['reference'])
        doc = {
            'uinque_id': fi['uinque_id'],
            'binary_data': binary_data,
        }
        mongo.insert_doc_to_mongo(doc)


        el.index_doc(fi,fi['uinque_id'])



    #                     'created': file['created'], 'size': file['size']})
    # mong = InsertToMongo()
    # mong.insert_cdc_to_mongo(file)
run()