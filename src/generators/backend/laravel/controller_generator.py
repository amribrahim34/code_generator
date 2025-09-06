from typing import Dict, Any, List, Union
from src.core.interfaces.code_generator import ICodeGenerator
from src.core.entities.schema import Model, Attribute, Relationship ,Schema
from src.core.interfaces.template_renderer import ITemplateRenderer
from src.core.interfaces.config_loader import IConfigLoader
from src.utilities.string_utils import to_pascal_case, to_snake_case, pluralize ,to_kebab_case

class ControllerGenerator(ICodeGenerator):
    def __init__(self, config_loader: IConfigLoader, template_renderer: ITemplateRenderer):
        self.config_loader = config_loader
        self.template_renderer = template_renderer


    def generate(self, schema: Schema) -> Dict[str, str]:
        generated_files = {}
        controller_types = ['Admin', 'CustomerWebsite', 'MobileApp']

        for controller_type in controller_types:
            for model in schema.models:
                content = self._generate_controller(model, controller_type)
                model_name = model['name'] if isinstance(model, dict) else model.name
                file_path = f"backend/app/Http/Controllers/{controller_type}/{model_name}Controller.php"
                generated_files[file_path] = content

        return generated_files
    
    
    def get_output_path(self, model_name: str) -> str:
        return f"backend/app/Http/Controllers/{model_name}Controller.php"

    def render_template(self, template: str, context: Dict[str, Any]) -> str:
        return self.template_renderer.render(template, context)

        
    def _generate_controller(self, model: Union[Dict[str, Any], Model], controller_type: str) -> str:
        context = self.prepare_context(model, controller_type)
        template = self.get_template('controller')
        return self.template_renderer.render('backend/laravel/controller.stub', context)

    def prepare_context(self, model: Union[Dict[str, Any], Model], controller_type: str) -> Dict[str, Any]:
        model_name = model['name'] if isinstance(model, dict) else model.name
        attributes = model['attributes'] if isinstance(model, dict) else model.attributes
        relationships = model['relationships'] if isinstance(model, dict) else model.relationships
        use_repository = self.config_loader.get('use_repository' ,False)
        
        context =  {
            'class_name': f"{model_name}Controller",
            'model_name': model_name,
            'model_name_kebab' : to_kebab_case(model_name),
            'model_variable': to_snake_case(model_name),
            'model_plural': pluralize(to_snake_case(model_name)),
            'namespace': f"App\\Http\\Controllers\\{controller_type}",
            'repository_namespace': f"App\\Repositories\\{controller_type}\\Interfaces",
            'request_namespace': f"App\\Http\\Requests\\{controller_type}",
            'resource_namespace': f"App\\Http\\Resources\\{controller_type}",
            'use_repository': True,
            'use_form_requests': True,
            'model_attributes': attributes,
            'relationships': relationships,
            'api_version': self.config_loader.get('api_versions', {}).get(controller_type.lower(), 'v1'),
            'request_class': f"{controller_type}{model_name}Request",
            'resource_class': f"{model_name}Resource",
            'repository_interface': f"{model_name}RepositoryInterface",
            'controller_type': controller_type,
            'controller_type_lower_case': to_kebab_case(controller_type),
            'translation_key': to_snake_case(model_name),
        }
        
        if use_repository:
            context.update({
                'use_repository': True,
                'repository_namespace': f"App\\Repositories\\Interfaces\\{controller_type}",
                'repository_interface': f"I{model_name}Repository",
            })
        else:
            context.update({
                'use_repository': False,
                'model_namespace': f"App\\Models",
            })

        return context

    def get_template(self, template_name: str) -> str:
        template_path = self.config_loader.get('controller_template_path', 'backend/laravel/controller.stub')
        return self.template_renderer.load_template(template_path)

    def _generate_method(self, method_name: str, context: Dict[str, Any]) -> str:
        method_template = self.get_template(f'controller_{method_name}_method')
        return self.template_renderer.render(method_template, context)

    def validate_model(self, model: Union[Dict[str, Any], Model]) -> None:
        if isinstance(model, dict):
            if not model.get('name') or not model.get('attributes'):
                raise ValueError("Model must have a name and attributes")
        else:
            if not model.name or not model.attributes:
                raise ValueError("Model must have a name and attributes")


# Example usage (this would be part of the BackendGenerationService)
# config_loader = ConfigLoader()
# template_renderer = TemplateRenderer()
# controller_generator = ControllerGenerator(config_loader, template_renderer)
# generated_files = controller_generator.generate(model)