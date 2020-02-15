from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import fields


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://gustavo:1234@localhost/cat_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow()


class Category(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    def __init__(self, name):
        self.name = name


class CategorySchema(ma.Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
