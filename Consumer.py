from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "input_topic",
    group_id="debug-consumer-group",  # Unique group to force re-read
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("Listening to filtered messages from 'output_topic'...\n")

try:
    for message in consumer:
        print("Received:", message.value)
finally:
    consumer.close()
