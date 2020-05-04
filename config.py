import os

class Config:
   SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://brendawanjiku:brenda@localhost/pitch'
   SECRET_KEY='brenda-wanjiku'
class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
