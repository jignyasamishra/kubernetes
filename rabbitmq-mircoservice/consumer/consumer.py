import pika
import json
import time
import os

def callback(ch, method, properties, body):
    message = json.loads(body)
    print(f" [x] Received {message}")
    # Simulate some work
    time.sleep(2)
    print(f" [x] Done processing {message}")
    ch.basic_ack(delivery_tag=method.delivery_tag)

def start_consuming():
    rabbitmq_host = os.environ.get('RABBITMQ_HOST', 'localhost')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
    channel = connection.channel()

    channel.queue_declare(queue='task_queue', durable=True)
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='task_queue', on_message_callback=callback)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

# Start the consumer
start_consuming()