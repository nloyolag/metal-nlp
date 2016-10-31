from flask import Flask
import os

# Script that initializes app global values

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
app.secret_key = ''

from app import views
