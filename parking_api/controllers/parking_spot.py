from flask import request

from ..utils.response import ResponseUtil
from ..utils.request_parser import RequestParser
from ..models import ParkingSpot


def get_parking_spots():
    """
    Fetch all parking spots
    :return: response with parking spots
    """
    all_spots = []
    for spot in ParkingSpot.objects:
        all_spots.append(spot.fetch())
    if len(all_spots) == 0:  # no parkings spots
        return ResponseUtil.send_no_data()
    return ResponseUtil.send_success(all_spots)


def search_parking_spots():
    """
    Fetches nearby parking spots provided location and radius
    request args: lat, lng and radius (in meters, default 50m)
    :return: response with parking spots
    """
    nearby_spots = []
    parsed_input = RequestParser.parse_args(request, [
        {'name': 'lat', 'required': True, 'type': 'float'},
        {'name': 'lng', 'required': True, 'type': 'float'},
        {'name': 'radius', 'default': 50, 'type': 'int'}
    ])

    if parsed_input['error']:
        # invalid request args
        return ResponseUtil.send_bad_request(message='Please provide valid lat, lng and radius')

    lat = parsed_input['body']['lat']  # latitude
    lng = parsed_input['body']['lng']  # longitude
    radius = parsed_input['body']['radius']  # radius in meters

    if lng < -180 or lng > 180 or lat < -90 or lat > 90 or radius < 0:  # checks lat, lng and radius
        return ResponseUtil.send_bad_request(message='Please provide valid lat, lng and radius')

    # find parking spots within given radius from given location
    # where 6371000 is the length of equator of the earth in meters
    for spot in ParkingSpot.objects(location__geo_within_sphere=[[lng, lat], radius/6371000]):
        nearby_spots.append(spot.fetch())

    if len(nearby_spots) == 0:  # no nearby parking spots
        return ResponseUtil.send_no_data()
    return ResponseUtil.send_success(nearby_spots)


