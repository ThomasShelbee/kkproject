from flask import Flask, request, jsonify, send_file
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cd_collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)

# модель для хранения задачи
class Items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(15), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    s_size = db.Column(db.Integer, nullable=True)
    m_size = db.Column(db.Integer, nullable=True)
    l_size = db.Column(db.Integer, nullable=True)
    xl_size = db.Column(db.Integer, nullable=True)
    description = db.Column(db.String(500), nullable=False)

class Promos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(15), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)


with app.app_context():
    db.create_all()

def present_item(item):
    return {
        "id": item.id,
        "url": item.url,
        "title": item.title,
        "price": item.price,
        "quantity": item.quantity,
        "s_size": item.s_size,
        "m_size": item.m_size,
        "l_size": item.l_size,
        "xl_size": item.xl_size,
        "description": item.description
    }

def present_promo(promo):
    return {
        "id": promo.id,
        "title": promo.title,
        "quantity": promo.quantity,
        "price": promo.price
    }

# добавляем новую задачу
@app.route('/api/get-items', methods=['GET'])
def get_items():
    items = Items.query.all()
    return [present_item(item) for item in items]

@app.route('/api/get-promos', methods=['GET'])
def get_promos():
    promos = Promos.query.all()
    return [present_promo(promo) for promo in promos]

@app.route('/api/get-picture/<picture_url>', methods=['GET'])
def get_picture(picture_url):
    return send_file('static\\' + picture_url + '.png')

@app.route('/api/get-gif', methods=['GET'])
def get_gif():
    return send_file('static\\kk-gif.mp4')

@app.route('/api/delete-promo/<int:promo_id>', methods=['DELETE'])
def delete_promo(promo_id):
    promo = Promos.query.get(promo_id)
    if promo.quantity > 1:
        promo.quantity -= 1
        db.session.commit()
        return jsonify({"used_promo_id": promo_id})
    elif promo.quantity == 1:
        db.session.delete(promo)
        return jsonify({"deleted_id": promo_id})

# при запросе главной страницы возвращаем html файл с фронтендом как файл (без шаблонизатора)
@app.route('/')
def index():
    return "Hello"


if __name__ == '__main__':
    app.run(debug=True, port=8080)
