import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

# We have already declared/ created channel
# in send.py but creating again won't create
# a new channel if already exist
# this is done to be 100% sure that the hello  queue
# exist
channel.queue_declare(queue='hello')


# call back function to listen/ subscribe to the queue.
# this method will be called by the queue whenever there is a queue element.
def callback(ch, method, properties, body):
    print(' [x] Received %r ' % body)


# now we need to let rabbitmq that we are subscribing by callback method.
channel.basic_consume(
    queue='hello',
    on_message_callback=callback,
    auto_ack=True,
)

print(' [*] Waiting for message. To exit press Ctrl+C ')
channel.start_consuming()