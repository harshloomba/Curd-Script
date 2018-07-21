# database.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///product.sqlite'
db = SQLAlchemy(app)


# create app
def create_app():
    db = SQLAlchemy(app)
    db.init_app(app)
    db.create_all()
    return db

def marsh():
	ma = Marshmallow(app)
	return ma

def appObj():
	return app