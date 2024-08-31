import json

class JsonParser:
    def parse(self, input_data):
        try:
            # If input_data is already a Python object (list or dict), use it directly
            if isinstance(input_data, (list, dict)):
                data = input_data
            else:
                # If it's a string, try to parse it as JSON
                data = json.loads(input_data)

            if isinstance(data, dict) and 'models' in data:
                return data['models']
            elif isinstance(data, list):
                return data
            else:
                raise ValueError("Invalid JSON structure. Expected a dictionary with a 'models' key or a list of models.")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON input")