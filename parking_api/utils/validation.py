import bson


class ValidationUtil:
    @staticmethod
    def is_mongo_id(value):
        """
        Validates mongo ObjectId
        :param value: value to checks
        :return: True if value valid else False
        """
        return bson.objectid.ObjectId.is_valid(value)
