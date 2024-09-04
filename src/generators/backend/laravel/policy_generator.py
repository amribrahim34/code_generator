from typing import Dict, Any, Union, List
from src.core.interfaces.code_generator import ICodeGenerator
from src.core.entities.schema import Model, Attribute ,Schema
from src.core.interfaces.template_renderer import ITemplateRenderer
from src.core.interfaces.config_loader import IConfigLoader
from src.utilities.string_utils import to_pascal_case, to_snake_case

class PolicyGenerator(ICodeGenerator):
    def __init__(self, config_loader: IConfigLoader, template_renderer: ITemplateRenderer):
        self.config_loader = config_loader
        self.template_renderer = template_renderer

    
    def generate(self, schema: Schema) -> Dict[str, str]:
        generated_files = {}

        for model in schema.models:
            policy_content = self._generate_policy(model)
            model_name = model['name'] if isinstance(model, dict) else model.name
            file_path = f"app/Policies/{model_name}Policy.php"
            generated_files[file_path] = policy_content
                    
        return generated_files

    def get_output_path(self, model_name: str) -> str:
        return f"app/Policies/{model_name}Policy.php"

    def render_template(self, template: str, context: Dict[str, Any]) -> str:
        return self.template_renderer.render(template, context)

    def _generate_policy(self, model: Union[Dict[str, Any], Model]) -> str:
        context = self.prepare_context(model)
        template = self.get_template('policy')
        return self.template_renderer.render(template, context)

    def prepare_context(self, model: Union[Dict[str, Any], Model]) -> Dict[str, Any]:
        model_name = model['name'] if isinstance(model, dict) else model.name
        return {
            'model_name': model_name,
            'policy_name': f"{model_name}Policy",
            'model_variable': to_snake_case(model_name),
            'namespace': self.config_loader.get('policy_namespace', 'App\\Policies'),
            'model_namespace': self.config_loader.get('model_namespace', 'App\\Models'),
            'use_authorization': self.config_loader.get('use_authorization', True),
        }

    def get_template(self, template_name: str) -> str:
        template_path = self.config_loader.get('policy_template_path', 'backend/policy_stub.php')
        return self.template_renderer.load_template(template_path)

    def validate_model(self, model: Union[Dict[str, Any], Model]) -> None:
        if isinstance(model, dict):
            if not model.get('name'):
                raise ValueError("Model must have a name")
        else:
            if not model.name:
                raise ValueError("Model must have a name")

    def post_generation_tasks(self, generated_files: Dict[str, str]) -> None:
        # Perform any post-generation tasks here, such as formatting or linting
        pass

# Example usage (this would be part of the BackendGenerationService)
# config_loader = ConfigLoader()
# template_renderer = TemplateRenderer()
# policy_generator = PolicyGenerator(config_loader, template_renderer)
# generated_files = policy_generator.generate(model)