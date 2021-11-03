from flask import Flask , render_template,request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL')

from app.controller.routes import *
from app.controller.models import *