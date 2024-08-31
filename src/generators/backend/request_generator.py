import os

class RequestGenerator:
    def __init__(self):
        self.template_path = os.path.join('src', 'templates','backend', 'request_stub.php')

    def generate(self, model):
        store_request = self._generate_request(model, 'Store')
        update_request = self._generate_request(model, 'Update')
        return {
            f"app/Http/Requests/{model['name']}StoreRequest.php": store_request,
            f"app/Http/Requests/{model['name']}UpdateRequest.php": update_request
        }

    def _generate_request(self, model, action):
        with open(self.template_path, 'r') as file:
            template = file.read()

        class_name = f"{model['name']}{action}Request"
        
        return template.format(
            class_name=class_name,
            rules=self._generate_rules(model, action),
            messages=self._generate_messages(model)
        )

    def _generate_rules(self, model, action):
        rules = []
        for attr in model['attributes']:
            if attr['name'].lower() == 'id':
                continue  # Skip 'id' as it's typically not part of the request
            rule = f"'{attr['name']}' => '"
            rule += 'required|' if action == 'Store' else 'sometimes|'
            rule += self._get_validation_rule(attr['type'])
            rule += "'"
            rules.append(rule)
        return ',\n            '.join(rules)

    def _get_validation_rule(self, type):
        type_rules = {
            'string': 'string|max:255',
            'integer': 'integer',
            'boolean': 'boolean',
            'text': 'string',
            'date': 'date',
            'datetime': 'date',
            'float': 'numeric',
            'decimal': 'numeric',
            'bigIncrements': 'integer',
            'unsignedBigInteger': 'integer',
            'timestamp': 'date',
        }
        return type_rules.get(type.lower(), 'string')

    def _generate_messages(self, model):
        messages = []
        for attr in model['attributes']:
            if attr['name'].lower() == 'id':
                continue
            messages.append(f"'{attr['name']}.required' => 'The {attr['name']} field is required.'")
            messages.append(f"'{attr['name']}.{self._get_validation_rule(attr['type']).split('|')[0]}' => 'The {attr['name']} must be a valid {attr['type']}.'")
        return ',\n            '.join(messages)