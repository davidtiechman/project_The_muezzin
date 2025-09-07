# import uuid
from CRUD_elasticsarch.index_documents import IndexElasticsearch
from CRUD_mongo.insert_to_mongo import InsertToMongo
from load_audio.given_metadata import GetMetadata
from load_audio.unique_id import unique_a_id
from publicher_to_kafka.publicher_to_kafka import PublicherToKafka
from publicher_to_kafka.subscriber_with_kafka import SubscriberWithKafka


def run():
    # path = "C:\hostile audio files\podcasts"
    # for i,file in enumerate(path):
    #     print(i)
    get = GetMetadata("C:\hostile audio files\podcasts\download (1).wav")
    meta = get.get_metadata()
    kaf = PublicherToKafka()
    kaf.publishing_to_kafka(kaf.TOPIC,meta)
    sub = SubscriberWithKafka()
    sub.read_messages()
    unique_id = unique_a_id(meta)
    el = IndexElasticsearch()
    el.index_doc('aa',{'_id': unique_id,
    'created': meta['created'], 'size': meta['size']})
    mong = InsertToMongo()
    mong.insert_cdc_to_mongo(meta)

run()