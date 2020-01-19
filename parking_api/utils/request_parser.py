class RequestParser:
    @staticmethod
    def parse_args(request, fields):
        """
        Parses request query strings args
        :param request: request object
        :param fields: list of dicts with keys - name:string, required:boolean, default:any, type:string
        :return: dict with error, body fields - error will be true if input request object does meet the requirement
        """
        result = {'error': True, 'body': {}}
        for field in fields:
            field_name = field['name']
            field_required = field.get('required', False)
            field_type = field.get('type', 'string')
            field_default = field.get('default', 'pr_default_value')
            field_value = request.args.get(field_name, None)
            if field_required and field_value is None:
                return result

            if field_default is not 'pr_default_value' and field_value is None:
                result['body'][field_name] = field_default
                continue

            try:
                if field_type is 'int':
                    result['body'][field_name] = int(field_value)
                elif field_type is 'float':
                    result['body'][field_name] = float(field_value)
                else:
                    pass
            except ValueError:
                return result

        result['error'] = False
        return result
