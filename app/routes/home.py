from flask import Blueprint, Response
from flask import json

# local import
from app.service.bluetooth import Bluetooth

home = Blueprint("home", __name__)


@home.route("/")
def index():
    bluetooth = Bluetooth()
    bluetooth.enable_bluetooth()
    return "Ok", 200
