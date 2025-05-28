from flask import Flask, request, jsonify, send_file
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cd_collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

CORS(app)

app.config['MAIL_SERVER'] = 'postbox.cloud.yandex.net'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'YCAJE6Zi1vyP-G5E9py5UJmtW'
app.config['MAIL_PASSWORD'] = 'BFTJIMReImC3SdhmYyEw+wpkIYD63IGkBWf4nh8jE5Du'
app.config['MAIL_USE_TLS'] = True
mail = Mail(app)
