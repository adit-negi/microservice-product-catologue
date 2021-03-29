# amqps://qzpdnjsf:uJ_9zA55imCAcNFEOFuWjQTi3FAs_3DG@puffin.rmq2.cloudamqp.com/qzpdnjsf
import pika
import json
from main import Product, db

params = pika.URLParameters(
    'amqps://qzpdnjsf:uJ_9zA55imCAcNFEOFuWjQTi3FAs_3DG@puffin.rmq2.cloudamqp.com/qzpdnjsf')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')


def callback(cd, method, properties, body):
    print('recieved in main')
    data = json.loads(body)
    print(data)

    if properties.content_type == 'product_created':
        product = Product(
            id=data['id'], title=data['title'], image=data['image'])
        db.session.add(product)
        db.session.commit()
        print('product created')

    if properties.content_type == 'product_updated':
        product = Product.query.get(
            id=data['id'])
        product.title = data['title']
        product.image = data['image']
        db.session.commit()

    if properties.content_type == 'product_deleted':
        product = Product.query.get(
            id=data)
        db.session.delete(product)
        db.session.commit()


channel.basic_consume(
    queue='main', on_message_callback=callback, auto_ack=True)

print('started consuming')

channel.start_consuming()

channel.close()
