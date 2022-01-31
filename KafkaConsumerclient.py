from kafka import KafkaConsumer
consumer = KafkaConsumer('quickstart-events', bootstrap_servers='localhost:9092')
for x in consumer:
     print(x)

