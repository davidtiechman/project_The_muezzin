from CRUD_elasticsarch.index_documents import IndexElasticsearch
from convert_audio_to_binery.convert_audio_to_binary import convert_audio_to_binary
from CRUD_mongo.insert_to_mongo import InsertToMongo
from load_audio.unique_id import unique_a_id
from pub_and_sub_to_KAFKA.subscriber_with_kafka import SubscriberWithKafka


def run():
    sub = SubscriberWithKafka()
    file = sub.read_messages()
    el = IndexElasticsearch()
    mongo = InsertToMongo()
    for fi in file:
        fi['unique_id'] = unique_a_id(fi['size']+fi['name_file'])
        binary_data = convert_audio_to_binary(fi['reference'])
        doc = {
            'unique_id': fi['unique_id'],
            'binary_data': binary_data,
        }
        mongo.insert_doc_to_mongo(doc)
        el.index_doc(fi,fi['unique_id'])

run()