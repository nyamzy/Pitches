import os

class Config:
    """
    General configuration parent class
    """
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://nyamzy:redemption@localhost/pitches'

class ProdConfig(Config):
    """
    Production configuration child class
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevConfig(Config):
    """
    Development configuration child class
    """
    DEBUG = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig
}