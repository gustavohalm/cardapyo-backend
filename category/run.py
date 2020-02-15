from flask import Flask
from flask import Flask, jsonify, request
from app.Model import Category, CategorySchema, db

app = Flask(__name__)

categories_schema = CategorySchema(many=True)
category_schema = CategorySchema()


@app.route('/categories')
def get_categories():
    categories = Category.query.all()
    categories = categories_schema.dump(categories).data

    return jsonify(categories)


@app.route('/categories', methods=['POST'])
def insert_category():
    data = category_schema.load(request.get_json()).data
    category = Category(name=data['name'])
    db.session.add(category)
    db.session.commit()

    return jsonify(category)


@app.route("/")
def test():
    return 'test'
