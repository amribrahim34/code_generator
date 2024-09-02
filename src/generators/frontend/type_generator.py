import os
from typing import Dict, List

class TypeGenerator:
    def __init__(self, config: Dict, models: List[Dict] = None):
        self.config = config
        # We're not using models here, but keeping it for compatibility
        self.template_path = os.path.join(self.config.get('template_dir', 'src/templates'), 'frontend/type_stub.ts')
        self.output_dir = os.path.join(self.config['frontend']['output_dir'], 'src', self.config['frontend']['type_dir'])

    def generate(self, schema: Dict) -> Dict[str, str]:
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        generated_files = {}
        for model in schema.get('models', []):
            file_content = self._generate_model_type(model)
            file_name = f"{model['name'].lower()}Types.ts"
            file_path = os.path.join(self.output_dir, file_name)
            
            generated_files[file_path] = file_content

        index_file = self._generate_index_file(schema.get('models', []))
        index_file_path = os.path.join(self.output_dir, 'index.ts')
        generated_files[index_file_path] = index_file

        return generated_files

    def _generate_model_type(self, model: Dict) -> str:
        model_name = model['name']
        model_attributes = self._generate_model_attributes(model['attributes'])

        with open(self.template_path, 'r') as template_file:
            template = template_file.read()

        type_content = template.replace('{{MODEL_NAME}}', model_name)
        type_content = type_content.replace('{{MODEL_ATTRIBUTES}}', model_attributes)

        return type_content

    def _generate_model_attributes(self, attributes: List) -> str:
        return '\n'.join([f"  {attr.name}: {self._map_type(attr.type)}" for attr in attributes])

    def _generate_index_file(self, models: List[Dict]) -> str:
        index_content = []

        for model in models:
            model_name = model['name']
            export_statement = f"export type {{ {model_name}, Create{model_name}DTO, Update{model_name}DTO }} from './{model_name.lower()}Types'"
            index_content.append(export_statement)

        return "\n".join(index_content)

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