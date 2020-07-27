import logging

from flask import Flask

# local import
from app.routes.home import home_bp


def create_app():
    app = Flask(__name__)

    app.register_blueprint(home_bp)

    return app
