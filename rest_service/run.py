from flask import Flask
from flask_restful import Resource, Api
import pika

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def __init__(self):
        self.answer = ''
        self.channel2 = None

    def answer_callback(self, ch, method, properties, body):
        print('rest')
        print(body)
        self.answer = body
        self.channel2.stop_consuming()

    def get(self, component_name, module_name, task):
        connection = pika.BlockingConnection(pika.ConnectionParameters(
            'localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='hello')
        channel.basic_publish(exchange='',
                              routing_key='hello',
                              body='Hello World!')
        self.channel2 = connection.channel()
        self.channel2.queue_declare(queue='answer')
        self.channel2.basic_consume(self.answer_callback,
                                    queue='answer',
                                    no_ack=True)
        self.channel2.start_consuming()
        return {'hello': str(self.answer)}


api.add_resource(HelloWorld, '/<string:component_name>/<string:module_name>/<string:task>')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
