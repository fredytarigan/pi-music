import logging

from flask import Flask

# local import
from app.routes.home import home_bp
from app.routes.api import api_bp


def create_app():
    app = Flask(__name__)

    app.register_blueprint(home_bp)
    app.register_blueprint(api_bp)

    return app
