import pika
import json
import time

def process_message(message):
    print(f"processing message: {message}")
    # Simulating the time taken to process the message
    time.sleep(1)
    # Transform/Process the message and load to PostgreSQL for later querying
    print(f"processed message: {message}")

def start_worker():
    def callback(ch, method, properties, body):
        print(f"body {body}")
        message = json.loads(body)
        print(f"Received message: {message}")
        process_message(message) # process message synchronously (within this thread)

    print("Trying to establish Connection...")
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    print("Connection Established...")
    channel = connection.channel()
    print("Channel connection created...")
    channel.queue_declare(queue="user-task-queue")
    print("Queue declared...")

    # start consuming the messages from the queue
    channel.basic_consume(queue="user-task-queue",
                          on_message_callback=callback,
                          auto_ack=True)
    print("Started consuming messages...")
    channel.start_consuming()
