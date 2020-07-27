from flask import Blueprint, Response, render_template
from flask import json

# local import
from app.service.bluetooth import Bluetooth

home_bp = Blueprint(
    "home",
    __name__,
    template_folder="templates",
    url_prefix="/"
)


@home_bp.route("/")
def index():
    bluetooth = Bluetooth()
    devices = bluetooth.search_devices()

    return render_template(
        'home.html',
        devices=devices
    )
