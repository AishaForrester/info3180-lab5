from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect(app)
app.config.from_object(Config)

#Initializing database lab5

db = SQLAlchemy(app)
migrate= Migrate(app, db)

from app import models

from app import views
