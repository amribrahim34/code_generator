from typing import Dict, Any, Union ,List
from src.core.interfaces.code_generator import ICodeGenerator
from src.core.entities.schema import Model, Attribute ,Schema
from src.core.interfaces.template_renderer import ITemplateRenderer
from src.core.interfaces.config_loader import IConfigLoader
from src.utilities.string_utils import to_pascal_case, to_snake_case

class FactoryGenerator(ICodeGenerator):
    def __init__(self, config_loader: IConfigLoader, template_renderer: ITemplateRenderer):
        self.config_loader = config_loader
        self.template_renderer = template_renderer


    def generate(self, schema: Schema) -> Dict[str, str]:
        generated_files = {}

        for model in schema.models:
            factory_content = self._generate_factory(model)
            model_name = model['name'] if isinstance(model, dict) else model.name
            file_path = f"backend/database/factories/{model_name}Factory.php"
            generated_files[file_path] = factory_content

        return generated_files

    def _generate_factory(self, model: Union[Dict[str, Any], Model]) -> str:
        context = self.prepare_context(model)
        template = self.get_template('factory')
        return self.template_renderer.render('backend/laravel/factory.stub', context)


    def get_output_path(self, model_name: str) -> str:
        return f"backend.database/factories/{model_name}Factory.php"

    def render_template(self, template: str, context: Dict[str, Any]) -> str:
        return self.template_renderer.render('backend/laravel/factory.stub', context)
        
    def prepare_context(self, model: Union[Dict[str, Any], Model]) -> Dict[str, Any]:
        model_name = model['name'] if isinstance(model, dict) else model.name
        attributes = model['attributes'] if isinstance(model, dict) else model.attributes

        return {
            'model_name': model_name,
            'model_namespace': f"App\\Models\\{model_name}",
            'factory_name': f"{model_name}Factory",
            'attributes': self._prepare_attributes(attributes),
        }

    def _prepare_attributes(self, attributes: Union[List[Dict[str, Any]], List[Attribute]]) -> List[Dict[str, Any]]:
        prepared_attributes = []
        for attr in attributes:
            if isinstance(attr, dict):
                prepared_attributes.append({
                    'name': attr['name'],
                    'type': attr['type'],
                    'faker_method': self._get_faker_method(attr['type']),
                })
            else:
                prepared_attributes.append({
                    'name': attr.name,
                    'type': attr.type,
                    'faker_method': self._get_faker_method(attr.type),
                })
        return prepared_attributes

    def _get_faker_method(self, attr_type: str) -> str:
        faker_methods = {
            'string': 'faker->word',
            'text': 'faker->paragraph',
            'integer': 'faker->randomNumber()',
            'float': 'faker->randomFloat(2)',
            'boolean': 'faker->boolean',
            'date': 'faker->date()',
            'datetime': 'faker->dateTime()',
            'email': 'faker->safeEmail',
            'password': 'bcrypt($faker->password)',
            'url': 'faker->url',
            'uuid': 'faker->uuid',
        }
        return faker_methods.get(attr_type, 'faker->word')

    def get_template(self, template_name: str) -> str:
        template_path = self.config_loader.get('factory_template_path', 'backend/laravel/factory.stub')
        return self.template_renderer.load_template(template_path)

    def validate_model(self, model: Union[Dict[str, Any], Model]) -> None:
        if isinstance(model, dict):
            if not model.get('name') or not model.get('attributes'):
                raise ValueError("Model must have a name and attributes")
        else:
            if not model.name or not model.attributes:
                raise ValueError("Model must have a name and attributes")

    def post_generation_tasks(self, generated_files: Dict[str, str]) -> None:
        # Perform any post-generation tasks here, such as formatting or linting
        pass

# Example usage (this would be part of the BackendGenerationService)
# config_loader = ConfigLoader()
# template_renderer = TemplateRenderer()
# factory_generator = FactoryGenerator(config_loader, template_renderer)
# generated_files = factory_generator.generate(model)