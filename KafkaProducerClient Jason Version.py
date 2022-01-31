
from kafka import KafkaProducer
from kafka.errors import KafkaError
import msgpack
import logging
import random

#Add 100 random numbers to topic 'random numbers

producer = KafkaProducer(value_serializer=msgpack.dumps)

for x in range(0, 100):
    producer.send('random-numbers-json-2', {'index': x,'Random Number': random.randint(0, 100000)})


producer = KafkaProducer(value_serializer=lambda m: json.dumps(m).encode('ascii'))