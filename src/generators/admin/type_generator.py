import os
from typing import Dict, List

class TypeGenerator:
    def __init__(self, config: Dict, models: List[Dict]):
        self.config = config
        self.models = models
        self.template_path = os.path.join(self.config['template_dir'], 'admin', 'type_stub.ts')
        self.output_dir = os.path.join(self.config['frontend']['output_dir'], self.config['frontend']['type_dir'])

    def generate(self , model):
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        generated_files = {}
        for model in self.models:
            file_content = self._generate_model_type(model)
            file_name = f"{model['name'].lower()}Types.ts"
            file_path = os.path.join(self.output_dir, file_name)
            
            with open(file_path, 'w') as file:
                file.write(file_content)
            
            generated_files[file_name] = file_content

        self._generate_index_file()
        return generated_files

    def _generate_model_type(self, model: Dict) -> str:
        model_name = model['name']
        model_attributes = self._generate_model_attributes(model['attributes'])

        with open(self.template_path, 'r') as template_file:
            template = template_file.read()

        type_content = template.replace('{{MODEL_NAME}}', model_name)
        type_content = type_content.replace('{{MODEL_ATTRIBUTES}}', model_attributes)

        return type_content

    def _generate_model_attributes(self, attributes: List[Dict]) -> str:
        return '\n'.join([f"  {attr['name']}: {self._map_type(attr['type'])}" for attr in attributes])

    def _generate_index_file(self):
        index_content = []

        for model in self.models:
            model_name = model['name']
            export_statement = f"export type {{ {model_name}, Create{model_name}DTO, Update{model_name}DTO }} from './{model_name.lower()}Types'"
            index_content.append(export_statement)

        index_content = "\n".join(index_content)

        output_path = os.path.join(self.output_dir, 'index.ts')
        with open(output_path, 'w') as output_file:
            output_file.write(index_content)

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

def generate_types(config: Dict, models: List[Dict]):
    generator = TypeGenerator(config, models)
    return generator.generate()

if __name__ == "__main__":
    # This is just for testing purposes
    test_config = {
        'template_dir': './templates',
        'frontend': {
            'output_dir': './output',
            'type_dir': 'types'
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
        },
        {
            'name': 'Post',
            'attributes': [
                {'name': 'id', 'type': 'bigIncrements'},
                {'name': 'title', 'type': 'string'},
                {'name': 'content', 'type': 'text'},
                {'name': 'userId', 'type': 'unsignedBigInteger'},
            ]
        }
    ]
    generated_files = generate_types(test_config, test_models)
    print(generated_files)