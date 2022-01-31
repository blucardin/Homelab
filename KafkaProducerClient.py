
from kafka import KafkaProducer
from kafka.errors import KafkaError
import logging
import random

#Add 100 random numbers to topic 'random numbers

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

for x in range(0, 100):

     future = producer.send('random-numbers', bytes(str(x) + ' Random Number: ' + str(random.randint(0, 1000000)), "utf-8"))

     try:

          record_metadata = future.get(timeout=10)
          print(record_metadata)

     except KafkaError:
          print(logging.exception())

