from itsdangerous import URLSafeSerializer
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


s = URLSafeSerializer('subagio165')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'rahasia123456'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

db = SQLAlchemy(app)
from app import routes