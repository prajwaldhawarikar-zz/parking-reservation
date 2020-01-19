import mongoengine
from bson.objectid import ObjectId
import datetime

from .parking_spot import ParkingSpot
from .user import User


# booking model
class Booking(mongoengine.Document):
    meta = {'collection': 'bookings'}

    # schema
    parking_spot = mongoengine.ReferenceField(ParkingSpot)
    user = mongoengine.ReferenceField(User)
    state = mongoengine.StringField(default='CONFIRMED')
    created_at = mongoengine.DateTimeField()
    updated_at = mongoengine.DateTimeField(default=datetime.datetime.now)

    def save(self, *args, **kwargs):
        """
        Updates timestamps and saves doc
        """
        if not self.created_at:
            self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        return super(Booking, self).save(*args, **kwargs)

    def fetch(self):
        """
        Fetches doc and parses id
        :return: doc
        """
        doc = self.to_mongo()
        for k, v in doc.items():
            if isinstance(v, ObjectId):
                doc[k] = str(v)

        return doc
