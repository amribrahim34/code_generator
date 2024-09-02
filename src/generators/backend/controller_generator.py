from typing import Dict, Any, List, Union
from src.core.interfaces.generator import Generator
from src.core.models.schema import Model, Attribute, Relationship
from src.infrastructure.template_reader import TemplateReader
from src.infrastructure.config_loader import ConfigLoader
from src.core.utils.string_utils import to_pascal_case

class ControllerGenerator(Generator):
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        template_dir = config.get('template_dir', 'src/templates')
        self.template_reader = TemplateReader(template_dir)

    def generate(self, model: Union[Dict[str, Any], Model]) -> Dict[str, str]:
        generated_files = {}
        controller_types = ['Admin', 'Website', 'MobileApp']
        
        for controller_type in controller_types:
            controller_content = self._generate_controller(model, controller_type)
            model_name = model['name'] if isinstance(model, dict) else model.name
            generated_files[f"app/Http/Controllers/{controller_type}/{model_name}Controller.php"] = controller_content
        
        return generated_files

    def get_template(self, template_name: str) -> str:
        template_path = self.config.get('controller_template_path', 'backend/controller_stub.php')
        return self.template_reader.read_template(template_path)

    def render_template(self, template: str, context: Dict[str, Any]) -> str:
        return template.format(**context)

    def _generate_controller(self, model: Union[Dict[str, Any], Model], controller_type: str) -> str:
        context = self._prepare_controller_context(model, controller_type)
        template = self.get_template('controller')
        return self.render_template(template, context)

    def _prepare_controller_context(self, model: Union[Dict[str, Any], Model], controller_type: str) -> Dict[str, Any]:
        model_name = model['name'] if isinstance(model, dict) else model.name
        attributes = model['attributes'] if isinstance(model, dict) else model.attributes
        relationships = model['relationships'] if isinstance(model, dict) else model.relationships

        return {
            'class_name': f"{model_name}Controller",
            'model_name': model_name,
            'model_variable': model_name.lower(),
            'namespace': f"App\\Http\\Controllers\\{controller_type}",
            'use_repository': self.config.get('controller', {}).get('use_repository', True),
            'use_form_requests': self.config.get('controller', {}).get('use_form_requests', True),
            'model_attributes': attributes,
            'relationships': relationships,
            'api_version': self.config.get('api_versions', {}).get(controller_type.lower(), 'v1'),
            'request_class': f"{model_name}Request",
            'resource_class': f"{model_name}Resource",
            'repository_interface': f"I{model_name}Repository",
        }

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