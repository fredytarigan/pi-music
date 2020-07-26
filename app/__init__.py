import logging

from flask import Flask

# local import
from app.routes.home import home


def create_app():
    app = Flask(__name__)

    app.register_blueprint(home)

    return app
