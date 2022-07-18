import os

class Config(object):
    SECRET_KEY = os.urandom(50)
    SESSION_PERMANENT = False
    SESSION_TYPE = 'filesystem'
    SESSION_KEY_PREFIX = ''
    SESSION_FILE_THRESHOLD = 20
    SESSION_USE_SIGNER = False
    GAME_WIDTH = 20
    GAME_HEIGHT= 20
    GAME_RATIO = 0.1

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True