import json
import time

from kafka import KafkaProducer


def main():
    producer = KafkaProducer(
        acks=0,
        compression_type='gzip',
        bootstrap_servers=['localhost:9092'],
        value_serializer=lambda value: json.dumps(value).encode('utf-8'),
        key_serializer=lambda key: json.dumps(key).encode('utf-8'),
    )
    for i in range(1000):
        keys = [None, 'test', 'test2', 'test3']
        data = {'str': 'result' + str(i)}
        producer.send('test', value=data, key=keys[i % len(keys)])
        producer.flush()
        time.sleep(1)


if __name__ == '__main__':
    main()
