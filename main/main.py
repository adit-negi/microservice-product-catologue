from flask import Flask, jsonify, abort
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint
from dataclasses import dataclass
import requests
import json
from producer import publish

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123@db/main'
CORS(app)

db = SQLAlchemy(app)


@dataclass
class Product(db.Model):
    id: int
    title: str
    image: str
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))


@dataclass
class ProductUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)

    UniqueConstraint('user_id', 'product_id', name='user_product_unique')


@app.route('/api/products')
def index():
    products = Product.query.all()
    # json_response = []
    # for product in products:
    #     temp = product.__dict__
    #     del temp['_sa_instance_state']
    #     json_response.append(temp)
    return jsonify(products)


@app.route('/api/product/<int:id>/like', methods=['POST'])
def like(id):
    print('here')
    req = requests.get('http://172.17.0.1:8000/api/user')
    res = json.loads(req.text)
    print(res['id'])
    
    productUser = ProductUser(user_id=res['id'], product_id=id)
    db.session.add(productUser)
    db.session.commit()

    publish('product liked', id)

    return jsonify({'message': 'success'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
