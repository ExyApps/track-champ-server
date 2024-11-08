import os

class ProdConfig:
    TESTING = False
    PROJECT_PATH_JOINER = '../..'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev_key'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///project.db' #Production/Dev

class DevConfig(ProdConfig):
    PROJECT_PATH_JOINER = '..'

class TestConfig(ProdConfig):
    TESTING = True
    PROJECT_PATH_JOINER = '..'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:' #In-memory for tests