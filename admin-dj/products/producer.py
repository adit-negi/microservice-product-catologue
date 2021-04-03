# amqps://qzpdnjsf:uJ_9zA55imCAcNFEOFuWjQTi3FAs_3DG@puffin.rmq2.cloudamqp.com/qzpdnjsf
import pika
import json
params = pika.URLParameters(
    'amqps://qzpdnjsf:uJ_9zA55imCAcNFEOFuWjQTi3FAs_3DG@puffin.rmq2.cloudamqp.com/qzpdnjsf')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    print('got data', properties, body)
    print(json.dumps(body))
    channel.basic_publish(exchange='', routing_key='main',
                          body=json.dumps(body), properties=properties)
    # check daf
