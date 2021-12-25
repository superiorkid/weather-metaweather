from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
import os

WEATHER_ICON = os.path.join('static', 'weather_img')

app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)
app.config['UPLOAD_FOLDER'] = WEATHER_ICON

from app import routes