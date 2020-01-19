import mongoengine


# parking_spot model
class ParkingSpot(mongoengine.Document):
    meta = {'collection': 'parking_spots'}

    # schema
    address = mongoengine.StringField()
    location = mongoengine.PointField()

    def fetch(self):
        """
        Fetches doc and parses id
        :return: doc
        """
        doc = self.to_mongo()
        doc['_id'] = str(doc['_id'])
        return doc
