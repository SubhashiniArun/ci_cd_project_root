import pika
import json

def send_task_to_process_data(batch_data):
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()

    print(f"Channel: {channel}")

    # Declare the queue (in case it doesn't exist)
    channel.queue_declare(queue="user-task-queue")
    
    for item in batch_data:
        message = json.dumps(item)
        channel.basic_publish(exchange='',
                            routing_key='user-task-queue',
                            body=message)
        
        print(f"Sent task for User ID : {id} with message {message}")

    print(f"Sent all the messages of length: {len(batch_data)}")
    
    connection.close()
