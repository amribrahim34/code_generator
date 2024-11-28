from typing import Dict, Any, List, Union
from src.core.interfaces.code_generator import ICodeGenerator
from src.core.interfaces.template_renderer import ITemplateRenderer
from src.core.entities.schema import Model, Attribute, Relationship ,Schema
from src.core.interfaces.config_loader import IConfigLoader
from src.utilities.string_utils import to_pascal_case, to_snake_case, to_kebab_case

class MiddlewareGenerator(ICodeGenerator):
    def __init__(self, config_loader: IConfigLoader, template_renderer: ITemplateRenderer):
        self.config_loader = config_loader
        self.template_renderer = template_renderer

    def generate(self, schema: Schema) -> Dict[str, str]:
        generated_files = {}
        middleware_types = ['Admin', 'Customer', 'Vendor']
            
        for middleware_type in middleware_types:
            content = self._generate_middleware(middleware_type)
            file_path = f"backend/app/Http/Middleware/Is{middleware_type}.php"
            generated_files[file_path] = content

        return generated_files

    def get_output_path(self, model_name: str) -> str:
        return f"backend/app/Http/Middleware/{model_name}Middleware.php"

    def _generate_middleware(self, middleware_type: str) -> str:
        context = self.prepare_context( middleware_type)
        return self.template_renderer.render(f'backend/laravel/middleware.stub', context)

    def prepare_context(self,middleware_type: str) -> Dict[str, Any]:
        
        return {
            'middleware_type': middleware_type,
            'class_name': f"Is{middleware_type}",
            'guard_name': middleware_type.lower(),
            'error_message': f"This {middleware_type.lower()} action is unauthorized.",
        }

    def get_template(self, template_name: str) -> str:
        template_path = self.config_loader.get(f'{template_name}_middleware_template_path', 
                                               f'backend/laravel/middleware/{template_name}.stub')
        return self.template_renderer.load_template(template_path)
    
    def render_template(self, template: str, context: Dict[str, Any]) -> str:
        return self.template_renderer.render(template, context)
    
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