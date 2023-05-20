from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

app = Flask(__name__)

current_dir = os.path.abspath(os.path.dirname(__file__))
database_uri = 'sqlite:///' + os.path.join(current_dir, 'webhook.db')

app.config['SECRET_KEY'] = '38cebh8gfj61k6f06jb3f57421d530t1'
app.config['SQLALCHEMY_DATABASE_URI'] = database_uri  # 'sqlite:///webhook.db'


database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'alert-info'

from simulador_dos_webhooks import routes
