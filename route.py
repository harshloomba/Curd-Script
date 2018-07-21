from flask import request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
import tempfile
import logging
from model import Product,db, ProductSchema, app
logger = logging.getLogger()
handler = logging.FileHandler('product_error.log')
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

db.init_app(app)
db.create_all()
product_schema = ProductSchema()
product_schema = ProductSchema(many=True)

# endpoint to create new product
@app.route("/product", methods=["POST"])
def add_product():
    try:
        ind = request.json['ind']
        description = request.json['description']
        datetime = request.json['datetime']
        longitude = request.json['longitude']
        latitude = request.json['latitude']
        elevation = request.json['elevation']
        new_product = Product(ind, description, datetime, longitude, latitude, elevation)
        db.session.add(new_product)
        db.session.commit()
        return str(new_product)    
    except Exception as e:
        logger.error('error while inserting the record', e)


# endpoint to show all products
@app.route("/product", methods=['GET'])
def get_product():
    try: 
        page = request.args.get('page', 1, type=int)
        per_page=3
        all_products = Product.query.paginate(page,per_page,error_out=False).items
        result = product_schema.dump(all_products)
        return jsonify(result)
    except Exception as e:
        logger.error('error while extracting all the record', e)

# endpoint to get product detail by id
@app.route("/product/<ind>", methods=["GET"])
def product_detail(ind):
    try: 
        product = Product.query.filter_by(ind = ind)
        return product_schema.jsonify(product)
    except Exception as e:
        logger.error("error while extracting record by id", e)


# endpoint to update product
@app.route("/product", methods=["PUT"])
def product_update():
    try: 
        ind = request.json['ind']
        description = request.json['description']
        datetime = request.json['datetime']
        longitude = request.json['longitude']
        latitude = request.json['latitude']
        elevation = request.json['elevation']
        print ('update', ind)
        product = Product.query.filter_by(ind=ind, description = description, datetime = datetime ).first()
        product.longitude = longitude
        product.latitude = latitude
        product.elevation = elevation
        db.session.commit()
        return product_schema.jsonify(product)
    except Exception as e:
        logger.error("error while updating the record", e)


# endpoint to delete product
@app.route("/product", methods=["DELETE"])
def product_delete():
    try:
        ind = request.json['ind']
        description = request.json['description']
        datetime = request.json['datetime']
        longitude = request.json['longitude']
        latitude = request.json['latitude']
        elevation = request.json['elevation']
        product = Product.query.filter_by(ind=ind, description = description, datetime = datetime )
        product.delete()
        db.session.commit()
        return product_schema.jsonify(product)
    except Exception as e:
        logger.error("error while deleting the record", e)


if __name__ == '__main__':
    app.run(debug=True)

