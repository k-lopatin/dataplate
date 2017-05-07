from flask import Flask
from flask_restful import Resource, Api
import json
from analytics.router import Analytics_Router

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def __init__(self):
        self.answer = ''
        self.channel2 = None

    # def answer_callback(self, ch, method, properties, body):
    #     print('rest')
    #     print(body)
    #     self.answer = body
    #     self.channel2.stop_consuming()

    def create_message(self, language, func):
        return {
            'module': 'hh',
            'params': {
                'region': '1',
                'language': language,
                'function': func
            }
        }

    def get_languages(self):
        return ['php', 'java', 'python', 'c#', 'javascript', 'go', 'android']

    def create_average(self):
        average_result = []
        for language in self.get_languages():
            message = self.create_message(language, 'average')
            average_value = Analytics_Router().set_message(message).rpc()
            average_result.append({
                'name': language,
                'value': average_value
            })
        return average_result

    def get(self, task):
        if task == 'average':
            # print(self.create_average())
            return json.dumps(self.create_average()), 200, \
                   {
                       'Access-Control-Allow-Origin': '*',
                        'Access-Control-Allow-Methods': 'PUT,GET'
                   }
            # connection = pika.BlockingConnection(pika.ConnectionParameters(
            #     'localhost'))
            # channel = connection.channel()
            # channel.queue_declare(queue='hello')
            # channel.basic_publish(exchange='',
            #                       routing_key='hello',
            #                       body='Hello World!')
            # self.channel2 = connection.channel()
            # self.channel2.queue_declare(queue='answer')
            # self.channel2.basic_consume(self.answer_callback,
            #                             queue='answer',
            #                             no_ack=True)
            # self.channel2.start_consuming()
            # return {'hello': str(self.answer)}


api.add_resource(HelloWorld, '/<string:task>')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
