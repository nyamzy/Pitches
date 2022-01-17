from ensurepip import bootstrap
from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap

# Initializing the app
app = Flask(__name__)

# Configuration setup
app.config.from_object(DevConfig)

# Initializing flask extensions
bootstrap = Bootstrap(app)

from app import views