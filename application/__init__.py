import logging

from flask import Flask
from dashboard.views import dashboard

app = Flask(__name__)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
# Assign the URL prefixes for each blueprint
app.register_blueprint(dashboard, url_prefix='/dashboard')

from application import views
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
import SQLAlchemy_declear

engine = create_engine('sqlite:///argo_food.db')
try:
    engine.connect()
    engine.execute('SELECT 1;')
except OperationalError:
    SQLAlchemy_declear()