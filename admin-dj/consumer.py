# amqps://qzpdnjsf:uJ_9zA55imCAcNFEOFuWjQTi3FAs_3DG@puffin.rmq2.cloudamqp.com/qzpdnjsf


import pika
import json
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()
from products.models import Product

params = pika.URLParameters(
    'amqps://qzpdnjsf:uJ_9zA55imCAcNFEOFuWjQTi3FAs_3DG@puffin.rmq2.cloudamqp.com/qzpdnjsf')

connection = pika.BlockingConnection(params)

channel = connection.channel()
 
channel.queue_declare(queue='admin')


def callback(cd, method, properties, body):
    print('recieved in admin')
    print('body')
    data = json.loads(body)
    print(data)
    product = Product.objects.get(id=data)
    product.likes = product.likes + 1
    product.save()
    print('product saved with likes')


channel.basic_consume(
    queue='admin', on_message_callback=callback, auto_ack=True)

print('started consuming')

channel.start_consuming()

channel.close()
