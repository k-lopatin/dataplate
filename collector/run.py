import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    'localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print('collector')
    print(" [x] Received %r" % body)
    channel2 = connection.channel()
    channel2.queue_declare(queue='answer')
    channel2.basic_publish(exchange='',
                           routing_key='answer',
                           body='rabbitmq works!')


channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

channel.start_consuming()
