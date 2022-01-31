

#NON OPERATIVE, DOES NOT WORK YET!!!

from kafka import KafkaConsumer
import json
# To consume latest messages and auto-commit offsets

consumer = KafkaConsumer('random-number-json-2', bootstrap_servers=['localhost:9092'])

KafkaConsumer(auto_offset_reset='earliest', enable_auto_commit=False) # consume json messages

KafkaConsumer(value_deserializer=lambda m: json.loads(m.decode('ascii'))) # consume msgpack KafkaConsumer(value_deserializer=msgpack.unpackb) # StopIteration if no message after 1sec KafkaConsumer(consumer_timeout_ms=1000)

for message in consumer:
    print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition, message.offset, message.key, message.value))
