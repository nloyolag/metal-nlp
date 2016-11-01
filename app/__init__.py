from flask import Flask
import os

# Script that initializes app global values

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
APP_STATIC = os.path.join(APP_ROOT, 'static')
SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.secret_key = SECRET_KEY

from app import views
