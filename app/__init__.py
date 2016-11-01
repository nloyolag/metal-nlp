#!flask/bin/python
from flask import Flask
import os

# Script that initializes app global values

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
APP_STATIC = os.path.join(APP_ROOT, 'static')
app.secret_key = 'yeah'

from app import views
