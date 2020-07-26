from flask import Blueprint, Response
from flask import json

home = Blueprint("home", __name__)


@home.route("/")
def index():
    data = {"message": "Hello World !!!", "status": "OK", "code": "200"}
    response = json.dumps(data)
    resp = Response(response, status=200, mimetype="application/json")

    return resp
