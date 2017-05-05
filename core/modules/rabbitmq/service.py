from config.service import ConfigService
import pika


class RabbitMQService(object):

    TYPE = 'fanout'

    message = ''

    def __init__(self, exchange_name='dataplate'):
        self.host = ConfigService().get('core', 'rabbitmq', 'server', 'host')
        self.connection = self._get_connection()
        self.channel = self.connection.channel()
        self.exchange_name = exchange_name
        self._exchange_declare()
        self.published = False

    def set_message(self, message):
        self.message = message
        return self

    def publish_message(self):
        if self.published:
            raise Exception('This message is already sent')
        self.channel.basic_publish(exchange=self.exchange_name,
                                   routing_key='',
                                   body=self.message)
        self.connection.close()

    def _get_connection(self):
        return pika.BlockingConnection(pika.ConnectionParameters(
            host=self.host))

    def _exchange_declare(self):
        self.channel.exchange_declare(exchange=self.exchange_name,
                                      type=self.TYPE)
