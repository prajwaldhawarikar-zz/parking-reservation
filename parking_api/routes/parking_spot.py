from flask import Blueprint

from ..controllers import parking_spot

bp = Blueprint("parking_spots", __name__, url_prefix="/api/v1/parking_spots")


@bp.route("/")
def get_parking_spots():
    """
    Fetches all parking spots
    :return: response
    """
    return parking_spot.get_parking_spots()


@bp.route("/search")
def search_parking_spots():
    """
    Searches nearby parking spots provided location and radius
    :return: response
    """
    return parking_spot.search_parking_spots()
