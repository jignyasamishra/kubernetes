import pika
import json
import os
import time

def publish_message(message):
    rabbitmq_host = os.environ.get('RABBITMQ_HOST', 'localhost')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
    channel = connection.channel()
    
    channel.queue_declare(queue='task_queue', durable=True)
    
    channel.basic_publish(
        exchange='',
        routing_key='task_queue',
        body=json.dumps(message),
        properties=pika.BasicProperties(
            delivery_mode=2,  # make message persistent
        ))
    
    print(f" [x] Sent {message}")
    connection.close()

# Continuously publish messages
while True:
    publish_message({"task": "process_data", "data": [1, 2, 3, 4, 5]})
    time.sleep(5)  # Wait for 5 seconds before sending the next message
