from flask import Blueprint, Response, render_template
from flask import json, request

# local import
from app.service.bluetooth import Bluetooth

api_bp = Blueprint(
    "api",
    __name__,
    template_folder="templates",
    url_prefix="/api"
)


@api_bp.route("/bluetooth/connect", methods=["POST"])
def api_bluetooth_connect():
    data = request.get_json()
    return data
