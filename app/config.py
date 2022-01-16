class Config:
    """
    General configuration parent class
    """
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://nyamzy:redemption@localhost/pitches'

class ProdConfig(Config):
    """
    Production configuration child class
    """
    pass

class DevConfig(Config):
    """
    Development configuration child class
    """
    DEBUG = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig
}