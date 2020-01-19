from ..routes import booking, parking_spot


def get_blueprints():
    """
    :return: blueprints
    """
    return [booking.bp, parking_spot.bp]
