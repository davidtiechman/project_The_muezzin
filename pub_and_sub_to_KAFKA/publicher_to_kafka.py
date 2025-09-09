import logging
from kafka import KafkaProducer
import json

from .kafka_configurations import BOOTSTRAP_SERVERS,TOPIC_NAME,GROUP_ID,GROUP_ID

class PublicherToKafka:
    def __init__(self):
        self.TOPIC = TOPIC_NAME
        self.producer = KafkaProducer(
            bootstrap_servers=BOOTSTRAP_SERVERS,
            value_serializer=lambda m: json.dumps(m).encode('utf-8'))
    def publishing_to_kafka(self,topic,message):
        self.producer.send(topic, value=message)
        self.producer.flush()
        print('message published')
        logging.info('message published')
        print(f'the message is {message}')

# producer = KafkaProducer(
#     bootstrap_servers=BOOTSTRAP_SERVERS,
#     value_serializer=lambda v: json.dumps(v).encode('utf-8')
# )

# kaf = PublicherToKafka()
# kaf.publishing_to_kafka('references_and_metadata',[{"name": "nachmen", "action": "test"},{"name": "nachmen", "action": "five"}])