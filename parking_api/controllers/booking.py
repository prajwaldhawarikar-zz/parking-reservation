from flask import request

from ..utils.response import ResponseUtil
from ..utils.validation import ValidationUtil
from ..models import Booking, ParkingSpot, User


def get_bookings():
    """
    Fetches bookings
    :return: response with bookings
    """
    bookings = []
    for booking in Booking.objects:
        user = booking.user
        parking_spot = booking.parking_spot
        booking_details = booking.fetch()
        booking_details['user'] = user.fetch()
        booking_details['parking_spot'] = parking_spot.fetch()
        bookings.append(booking_details)

    if not len(bookings):  # no bookings found
        return ResponseUtil.send_no_data()
    return ResponseUtil.send_success(bookings)


def reserve_parking_spot():
    """
    Reserves the parking spot
    request body: user (user id), parking_spot (parking_spot id)
    :return: booking details response
    """
    req_data = request.get_json()
    if req_data is None:
        return ResponseUtil.send_bad_request(message='Please provide valid parking spot to book')

    user = req_data.get('user', None)
    parking_spot = req_data.get('parking_spot', None)

    if not (ValidationUtil.is_mongo_id(user) and ValidationUtil.is_mongo_id(parking_spot)):
        # invalid parking spot or user
        return ResponseUtil.send_bad_request(message='Please provide valid parking spot to book')

    if not (ParkingSpot.objects(id=parking_spot).count() and User.objects(id=user).count()):
        # no parking spot or user
        return ResponseUtil.send_bad_request(message='Please provide valid parking spot to book and user id')

    booking = Booking(user=user, parking_spot=parking_spot).save().fetch()
    return ResponseUtil.send_success(booking)


def cancel_booking(_id):
    """
    Cancels booking
    request body: _id (parking spot id), state( state must be CANCELLED)
    :param _id: _id of the booking to cancel
    :return: response
    """
    req_data = request.get_json()
    if req_data is None:
        # invalid request body
        return ResponseUtil.send_bad_request(message='Please provide valid booking to cancel')
    booking_id = req_data.get('_id', None)
    state = req_data.get('state', None)

    if not (ValidationUtil.is_mongo_id(booking_id) and _id == booking_id and state == 'CANCELLED'):
        # invalid parking spot or state
        return ResponseUtil.send_bad_request(message='Please provide valid booking to cancel and boooking state')

    cancelled_booking = Booking.objects(id=booking_id).update_one(set__state='CANCELLED')

    if not cancelled_booking:  # booking not found
        return ResponseUtil.send_bad_request(message='Booking not found. Please provide valid booking to cancel')

    return ResponseUtil.send_success({'message': 'booking cancelled', '_id': booking_id})
