from flask import Flask,render_template
from config import Development


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Development())

    @app.route('/')
    def hello_world():  # put application's code here
        return 'hello world'

    return app
