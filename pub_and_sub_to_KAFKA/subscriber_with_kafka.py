import logging

from kafka import KafkaConsumer
import json
from .kafka_configurations import BOOTSTRAP_SERVERS, TOPIC_NAME, GROUP_ID

class SubscriberWithKafka:
    def __init__(self):
        self.BOOTSTRAP_SERVERS = BOOTSTRAP_SERVERS
        self.TOPIC = TOPIC_NAME
    def read_messages(self):
        consumer = KafkaConsumer(
        # self.TOPIC,
        'references_and_metadata',
        bootstrap_servers= self.BOOTSTRAP_SERVERS,
        group_id = GROUP_ID,
        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
        consumer_timeout_ms=5000)
        file_references = []
        if consumer:
            print('consumer has started')
            logging.info('consumer has started')
            for message in consumer:
                arr_ref = {
                'reference' : message.value['reference'],
                'created' : message.value['created'],
                'size' : message.value['size'],
                'name_file' : message.value['name_file']
                }
                file_references.append(arr_ref)
                print("Received:", message.value)
        else:
            print("No messages")
        return file_references

# sub = SubscriberWithKafka()
# sub.read_messages()

