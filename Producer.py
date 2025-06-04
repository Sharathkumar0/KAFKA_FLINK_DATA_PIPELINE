#Imported required libraries
from kafka import KafkaProducer 
from faker import Faker
import json
import random
import time

#For Dummy data
faker = Faker()

#Created producer
producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

#User defined function to generated mock data
def generate_mock_items():
    return {
        'title': faker.sentence(nb_words=4), 
        'price': round(random.uniform(50, 1500), 2), 
        'currency': 'USD',
        'url': faker.url()}

print("Producing mock eBay items to Kafka")
for count in range(15):  # Send 15 mock items
    item = generate_mock_items()
    producer.send('input_topic', value=item)   #Topic Name: input-Topic
    print("Sent:", item)
    time.sleep(1)
 
producer.flush()
print("Producer done..\n")    