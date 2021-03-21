# amqps://qzpdnjsf:uJ_9zA55imCAcNFEOFuWjQTi3FAs_3DG@puffin.rmq2.cloudamqp.com/qzpdnjsf
import pika

params = pika.URLParameters(
    'amqps://qzpdnjsf:uJ_9zA55imCAcNFEOFuWjQTi3FAs_3DG@puffin.rmq2.cloudamqp.com/qzpdnjsf')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish():
    channel.basic_publish(exchange='', routing_key='main', body='hello')
