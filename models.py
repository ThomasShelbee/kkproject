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
    s_size = db.Column(db.Integer, nullable=False)
    m_size = db.Column(db.Integer, nullable=False)
    l_size = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)

class Promos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(15), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)


with app.app_context():
    db.create_all()
