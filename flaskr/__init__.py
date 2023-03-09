from flask import Flask, render_template
from config import Development


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Development())

    with app.app_context():
        # Include our Routes
        from . import routes

        # Register Blueprints
        app.register_blueprint(routes.pr_bp)


        return app
