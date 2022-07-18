import os

class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(50)
    SESSION_PERMANENT = False
    SESSION_TYPE = 'filesystem'
    SESSION_KEY_PREFIX = ''
    SESSION_FILE_THRESHOLD = 20
    SESSION_USE_SIGNER = False

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
