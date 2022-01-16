from flask import Flask
from .config import config_options
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_name):

    # Initializing the app
    app = Flask(__name__)

    # Configuration setup
    app.config.from_object(config_options(config_name))

    #Initializing flask extensions
    db.init_app(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    
    return app