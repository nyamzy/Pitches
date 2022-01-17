from ensurepip import bootstrap
from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap

# Initializing the app
app = Flask(__name__, instance_relative_config=True)

# Configuration setup
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

# Initializing flask extensions
bootstrap = Bootstrap(app)

from app import views