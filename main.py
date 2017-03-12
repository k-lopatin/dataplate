# import pika
#
# rabbitmq_connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# rabbitmq_channel = rabbitmq_connection.channel()
#
# rabbitmq_channel.queue_declare(queue='main')
# rabbitmq_channel.basic_publish(exchange='',
#                                routing_key='main',
#                                body='')

from collector.modules.github.auth import AuthService

auth_service = AuthService()