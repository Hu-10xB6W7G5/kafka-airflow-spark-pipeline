from sys import api_version
from kafka import KafkaProducer
from kafka.errors import KafkaError

import logging

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    # b-1.batch6w7.6qsgnf.c19.kafka.us-east-1.amazonaws.com:9092,
    # b-2.batch6w7.6qsgnf.c19.kafka.us-east-1.amazonaws.com:9092
    client_id='my-producer',
)

# Asynchronous by default
future = producer.send('g5-topic-1', b'apple')

# Block for 'synchronous' sends
try:
    record_metadata = future.get(timeout=30)
except KafkaError:
    # Decide what to do if produce request failed...
    logging.exception("Delivery failed")
    pass

# Successful result returns assigned partition and offset
print (record_metadata.topic)
print (record_metadata.partition)
print (record_metadata.offset)