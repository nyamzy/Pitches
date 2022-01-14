from flask import Flask
from .config import DevConfig

# Initializing the app
app = Flask(__name__)

# Configuration setup
app.config.from_object(DevConfig)


from app import views