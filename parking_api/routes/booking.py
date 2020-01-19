from flask import Blueprint, request

from ..controllers import booking

bp = Blueprint("bookings", __name__, url_prefix="/api/v1/bookings")


@bp.route("", methods=["GET", "POST"])
def parking_slot_reservation():
    """
    Reserves a parking spot
    :return: response
    """
    if request.method == "POST":
        return booking.reserve_parking_spot()
    else:
        return booking.get_bookings()


@bp.route("<_id>/cancel", methods=["PATCH"])
def cancel_booking(_id):
    """
    Cancels reservation
    :param _id: booking id
    :return: response
    """
    return booking.cancel_booking(_id)
