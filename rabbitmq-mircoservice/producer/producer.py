import pika
import json
import os
import time
import logging

logging.basicConfig(level=logging.INFO)

def publish_message(message):
    rabbitmq_host = os.environ.get('RABBITMQ_HOST', 'localhost')
    try:
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
        
        logging.info(f" [x] Sent {message}")
        connection.close()
    except pika.exceptions.AMQPConnectionError as error:
        logging.error(f"Unable to connect to RabbitMQ: {error}")
        time.sleep(5)  # Wait before trying to reconnect
    except Exception as error:
        logging.error(f"An error occurred: {error}")

# Continuously publish messages
while True:
    try:
        publish_message({"task": "process_data", "data": [1, 2, 3, 4, 5]})
        time.sleep(5)  # Wait for 5 seconds before sending the next message
    except KeyboardInterrupt:
        break
    except Exception as error:
        logging.error(f"Unexpected error in main loop: {error}")
        time.sleep(5)  # Wait before trying again