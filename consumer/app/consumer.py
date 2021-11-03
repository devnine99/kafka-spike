import json

from kafka import KafkaConsumer


class MessageConsumer:
    def __init__(self):
        self.consumer = self._create_consumer()

    def receive(self):
        for message in self.consumer:
            yield message

    @staticmethod
    def _create_consumer():
        return KafkaConsumer(
            'test',
            bootstrap_servers=['localhost:9092'],
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='my-group',
            value_deserializer=lambda value: json.loads(value.decode('utf-8')),
            key_deserializer=lambda key: json.loads(key.decode('utf-8')),
            # consumer_timeout_ms=1000
        )
