from dotenv import load_dotenv
from os import environ, path

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config():
    SECRET_KEY = environ.get('SECRET_KEY')
    STATIC_FOLDER = 'flaskr/static'
    TEMPLATES_FOLDER = 'flaskr/templates'


class Development(Config):
    FLASK_ENV = 'development'
    TESTING = True
    DEBUG = True



class Production(Config):
    FLASK_ENV = 'production'
    TESTING = False
    DEBUG = False
