from datetime import time
from os import name
from flask import Flask, request, jsonify
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =False
db = SQLAlchemy(app)
ma = Marshmallow(app)


#Product Model
class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)

    def __init__(self, title, description, price, qty):
        self.title = title
        self.description = description
        self.price = price
        self.qty = price

class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description', 'price', 'qty')


product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

@app.route('/add-product', methods=['POST'])
def add_product():
    title = request.json['title']
    description = request.json['description']
    price = request.json['price']
    qty = request.json['qty']

    new_product = Products(title, description, price, qty)

    db.session.add(new_product)
    db.session.commit()

    return ({"Resp":"Product created successfully!"})


@app.route('/products', methods=['GET'])
def get_products():
    products = Products.query.all()
    result = products_schema.dump(products)
    return jsonify(result)



@app.route('/product/<id>', methods=['GET'])
def get_single_product(id):
    product = Products.query.get(id)
    return product_schema.jsonify(product)


@app.route('/update-product/<id>', methods=['PUT'])
def update_product(id):
    product = Products.query.get(id)

    title = request.json['title']
    description = request.json['description']
    price = request.json['price']
    qty = request.json['qty']

    product.title = title
    product.description = description
    product.price = price
    product.qty = qty

    db.session.commit()

    return ({"Resp":"Product updated successfully!"})



@app.route('/delete-product/<id>', methods=['DELETE'])
def delete_product(id):
    product = Products.query.get(id)
    db.session.delete(product)
    db.session.commit()

    return ({"Resp":"Product deleted successfully!"})





if __name__ == '__main__':
    app.run(debug=True)