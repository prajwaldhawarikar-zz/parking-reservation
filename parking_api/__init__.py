from flask import Flask, jsonify
from mongoengine import connect

from parking_api.routes import get_blueprints


app = Flask(__name__)


@app.route("/is_server_up")
def check_server_health():
    """
    Health check api
    :return: response with status 200 if server is up
    """
    resp = jsonify({
        'message': 'Server is up'
    })
    return resp


def init_app_components():
    """
    Loads blueprints
    """
    for bp in get_blueprints():
        app.register_blueprint(bp)


# connect with mongodb
connect(db='parking_reservation',
        username='developer',
        password='donotsharewithanyone',
        host='mongodb+srv://cluster0-646bz.mongodb.net/?retryWrites=true&w=majority')

init_app_components()
