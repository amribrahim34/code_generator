from typing import Dict, Any, Union, List
from src.core.interfaces.code_generator import ICodeGenerator
from src.core.entities.schema import Model, Attribute ,Schema
from src.core.interfaces.template_renderer import ITemplateRenderer
from src.core.interfaces.config_loader import IConfigLoader
from src.utilities.string_utils import to_pascal_case, to_snake_case, pluralize

class SeederGenerator(ICodeGenerator):
    def __init__(self, config_loader: IConfigLoader, template_renderer: ITemplateRenderer):
        self.config_loader = config_loader
        self.template_renderer = template_renderer

    
    def generate(self, schema: Schema) -> Dict[str, str]:
        generated_files = {}

        for model in schema.models:
            seeder_content = self._generate_seeder(model)
            model_name = model['name'] if isinstance(model, dict) else model.name
            file_path = f"backend/database/seeders/{model_name}Seeder.php"
            generated_files[file_path] = seeder_content

        return generated_files


    def get_output_path(self, model_name: str) -> str:
        return f"database/seeders/{model_name}Seeder.php"

    def render_template(self, template: str, context: Dict[str, Any]) -> str:
        return self.template_renderer.render(template, context)


    def _generate_seeder(self, model: Union[Dict[str, Any], Model]) -> str:
        context = self.prepare_context(model)
        template = 'backend/laravel/seeder.stub'
        return self.template_renderer.render(template, context)

    def prepare_context(self, model: Union[Dict[str, Any], Model]) -> Dict[str, Any]:
        model_name = model['name'] if isinstance(model, dict) else model.name
        attributes = model['attributes'] if isinstance(model, dict) else model.attributes

        return {
            'model_name': model_name,
            'seeder_name': f"{model_name}Seeder",
            'namespace': "Database\\Seeders",
            'model_namespace': self.config_loader.get('model_namespace', 'App\\Models'),
            'table_name': pluralize(to_snake_case(model_name)),
            'attributes': self._prepare_attributes(attributes),
            'factory_name': f"{model_name}Factory",
        }

    def _prepare_attributes(self, attributes: Union[List[Dict[str, Any]], List[Attribute]]) -> List[Dict[str, Any]]:
        prepared_attributes = []
        for attr in attributes:
            if isinstance(attr, dict):
                prepared_attributes.append({
                    'name': attr['name'],
                    'type': attr['type'],
                })
            else:
                prepared_attributes.append({
                    'name': attr.name,
                    'type': attr.type,
                })
        return prepared_attributes

    def get_template(self, template_name: str) -> str:
        template_path = self.config_loader.get('seeder_template_path', 'backend/laravel/seeder.stub')
        return self.template_renderer.load_template(template_path)

    def validate_model(self, model: Union[Dict[str, Any], Model]) -> None:
        if isinstance(model, dict):
            if not model.get('name') or not model.get('attributes'):
                raise ValueError("Model must have a name and attributes")
        else:
            if not model.name or not model.attributes:
                raise ValueError("Model must have a name and attributes")
