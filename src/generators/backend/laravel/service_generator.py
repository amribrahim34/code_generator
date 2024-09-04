from typing import Dict, Any, Union, List
from src.core.interfaces.code_generator import ICodeGenerator
from src.core.entities.schema import Model, Attribute ,Schema
from src.core.interfaces.template_renderer import ITemplateRenderer
from src.core.interfaces.config_loader import IConfigLoader
from src.utilities .string_utils import to_pascal_case, to_snake_case, pluralize

class ServiceGenerator(ICodeGenerator):
    def __init__(self, config_loader: IConfigLoader, template_renderer: ITemplateRenderer):
        self.config_loader = config_loader
        self.template_renderer = template_renderer

    
    def generate(self, schema: Schema) -> Dict[str, str]:
        generated_files = {}
        service_types = ['Admin', 'CustomerWebsite', 'MobileApp']

        for service_type in service_types:
            for model in schema.models:
                service_content = self._generate_service(model, service_type)
                model_name = model['name'] if isinstance(model, dict) else model.name
                file_path = f"backend/app/Services/{service_type}/{model_name}Service.php"
                generated_files[file_path] = service_content

        return generated_files


    def get_output_path(self, model_name: str , service_type ) -> str:
        return f"backend/app/Services/{service_type}/{model_name}Service.php"

    def render_template(self, template: str, context: Dict[str, Any]) -> str:
        return self.template_renderer.render('backend/laravel/service.stub', context)

    def _generate_service(self, model: Union[Dict[str, Any], Model], service_type: str) -> str:
        context = self.prepare_context(model, service_type)
        template = 'backend/laravel/service.stub'
        return self.template_renderer.render(template, context)

    def prepare_context(self, model: Union[Dict[str, Any], Model], service_type: str) -> Dict[str, Any]:
        model_name = model['name'] if isinstance(model, dict) else model.name
        attributes = model['attributes'] if isinstance(model, dict) else model.attributes

        return {
            'model_name': model_name,
            'service_name': f"{model_name}Service",
            'namespace': f"App\\Services\\{service_type}",
            'model_namespace': self.config_loader.get('model_namespace', 'App\\Models'),
            'repository_namespace': f"App\\Repositories\\{service_type}\\Interfaces",
            'attributes': attributes,
            'model_variable': to_snake_case(model_name),
            'service_type': service_type,
        }

    def get_template(self, template_name: str) -> str:
        template_path = self.config_loader.get('service_template_path', 'backend/laravel/service.stub')
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