from kafka import KafkaConsumer
import json
from .kafka_configurations import BOOTSTRAP_SERVERS, TOPIC_NAME, GROUP_ID

class SubscriberWithKafka:
    def __init__(self):
        self.BOOTSTRAP_SERVERS = BOOTSTRAP_SERVERS
        self.TOPIC = TOPIC_NAME
    def read_messages(self):
        consumer = KafkaConsumer(
        self.TOPIC,
        bootstrap_servers= self.BOOTSTRAP_SERVERS,
        group_id = GROUP_ID,
        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
        consumer_timeout_ms=5000)
        print('the consumer has started')
        if consumer:
            for message in consumer:
                print("Received:", message.value)
        else:
            print("No messages")

# sub = SubscriberWithKafka()
# sub.read_messages()

