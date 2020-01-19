import mongoengine


# user model
class User(mongoengine.Document):
    meta = {'collection': 'users'}

    # schema
    name = mongoengine.StringField()

    def fetch(self):
        """
        Fetches doc and parses id
        :return: doc
        """
        doc = self.to_mongo()
        doc['_id'] = str(doc['_id'])
        return doc
