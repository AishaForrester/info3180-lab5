from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)

#Initializing database lab4

db = SQLAlchemy(app)
migrate= Migrate(app, db)

from app import models

from app import views
