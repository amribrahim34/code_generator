import os
from typing import Dict, List

class StoreGenerator:
    def __init__(self, config: Dict, models: List[Dict]):
        self.config = config
        self.models = models
        self.template_path = os.path.join(self.config['template_dir'], 'admin/store_stub.ts')
        self.output_dir = os.path.join(self.config['frontend']['output_dir'], self.config['frontend']['store_dir'])

    def generate(self , model):
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        generated_files = {}
        for model in self.models:
            generated_files.update(self._generate_store(model))

        return generated_files

    def _generate_store(self, model: Dict):
        model_name = model['name']
        model_name_plural = self._pluralize(model_name)
        model_name_lowercase = model_name.lower()
        model_name_plural_lowercase = model_name_plural.lower()

        with open(self.template_path, 'r') as template_file:
            template = template_file.read()

        store_content = template.replace('{{MODEL_NAME}}', model_name)
        store_content = store_content.replace('{{MODEL_NAME_PLURAL}}', model_name_plural)
        store_content = store_content.replace('{{MODEL_NAME_LOWERCASE}}', model_name_lowercase)
        store_content = store_content.replace('{{MODEL_NAME_PLURAL_LOWERCASE}}', model_name_plural_lowercase)
        store_content = store_content.replace('{{MODEL_INTERFACE}}', self._generate_model_interface(model))

        output_path = f"{model_name_lowercase}Store.ts"
        full_output_path = os.path.join(self.output_dir, output_path)
        with open(full_output_path, 'w') as output_file:
            output_file.write(store_content)

        return {output_path: store_content}


    def _generate_model_interface(self, model: Dict) -> str:
        interface = []
        for attr in model['attributes']:
            interface.append(f"  {attr['name']}: {self._map_type(attr['type'])}")
        return '\n'.join(interface)

    def _map_type(self, db_type: str) -> str:
        type_mapping = {
            'bigIncrements': 'number',
            'bigInteger': 'number',
            'boolean': 'boolean',
            'date': 'string',
            'dateTime': 'string',
            'decimal': 'number',
            'double': 'number',
            'float': 'number',
            'integer': 'number',
            'json': 'any',
            'jsonb': 'any',
            'string': 'string',
            'text': 'string',
            'time': 'string',
            'timestamp': 'string',
            'unsignedBigInteger': 'number',
            'unsignedInteger': 'number',
        }
        return type_mapping.get(db_type, 'any')

    def _pluralize(self, singular: str) -> str:
        # This is a very simple pluralization method. For a real-world application,
        # you might want to use a more robust pluralization library.
        if singular.endswith('y'):
            return singular[:-1] + 'ies'
        elif singular.endswith('s'):
            return singular + 'es'
        else:
            return singular + 's'

def generate_stores(config: Dict, models: List[Dict]):
    generator = StoreGenerator(config, models)
    return generator.generate()

if __name__ == "__main__":
    # This is just for testing purposes
    test_config = {
        'template_dir': './templates',
        'frontend': {
            'output_dir': './output',
            'store_dir': 'stores'
        }
    }
    test_models = [
        {
            'name': 'User',
            'attributes': [
                {'name': 'id', 'type': 'bigIncrements'},
                {'name': 'name', 'type': 'string'},
                {'name': 'email', 'type': 'string'},
                {'name': 'password', 'type': 'string'},
            ]
        }
    ]
    generate_stores(test_config, test_models)