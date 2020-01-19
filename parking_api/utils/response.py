from flask import jsonify, make_response


class ResponseUtil:
    @staticmethod
    def send_success(data):
        """
        Sends OK reponse
        :param data: reponse body
        :return: response
        """
        return make_response(jsonify(data), 200)

    @staticmethod
    def send_bad_request(message='Please provide valid data', **kwargs):
        """
        Sends BAD REQUEST response
        :param message: response message
        :return: response
        """
        resp_data = kwargs
        resp_data.update({'message': message})
        return make_response(jsonify(resp_data), 400)

    @staticmethod
    def send_no_data():
        """
        Sends NO DATA response
        :return: response
        """
        return make_response(jsonify([]), 404)
