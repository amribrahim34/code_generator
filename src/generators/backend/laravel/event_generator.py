from typing import Dict, Any, Union
from src.core.interfaces.code_generator import ICodeGenerator
from src.core.entities.schema import Model, Attribute ,Schema
from src.core.interfaces.template_renderer import ITemplateRenderer
from src.core.interfaces.config_loader import IConfigLoader
from src.utilities .string_utils import to_pascal_case, to_snake_case

class EventGenerator(ICodeGenerator):
    def __init__(self, config_loader: IConfigLoader, template_renderer: ITemplateRenderer):
        self.config_loader = config_loader
        self.template_renderer = template_renderer

    
    def generate(self, schema: Schema) -> Dict[str, str]:
        generated_files = {}
        event_types = ['Created', 'Updated', 'Deleted']

        for event_type in event_types:
            for model in schema.models:
                event_content = self._generate_event(model, event_type)
                model_name = model['name'] if isinstance(model, dict) else model.name
                file_path = f"backend/app/Events/{model_name}{event_type}Event.php"
                generated_files[file_path] = event_content

        return generated_files


    def get_output_path(self, model_name: str , event_type) -> str:
        return f"backend/app/Events/{model_name}{event_type}Event.php"

    def render_template(self, template: str, context: Dict[str, Any]) -> str:
        return self.template_renderer.render('backend/laravel/event.stub', context)

    def _generate_event(self, model: Union[Dict[str, Any], Model], event_type: str) -> str:
        context = self.prepare_context(model, event_type)
        template = self.get_template('event')
        return self.template_renderer.render('backend/laravel/event.stub', context)

    def prepare_context(self, model: Union[Dict[str, Any], Model], event_type: str) -> Dict[str, Any]:
        model_name = model['name'] if isinstance(model, dict) else model.name
        return {
            'model_name': model_name,
            'event_name': f"{model_name}{event_type}Event",
            'namespace': self.config_loader.get('event_namespace', 'App\\Events'),
            'model_namespace': self.config_loader.get('model_namespace', 'App\\Models'),
            'model_variable': to_snake_case(model_name),
            'event_type': event_type,
        }

    def get_template(self, template_name: str) -> str:
        template_path = self.config_loader.get('event_template_path', 'backend/laravel/event.stub')
        return self.template_renderer.load_template(template_path)

    def validate_model(self, model: Union[Dict[str, Any], Model]) -> None:
        if isinstance(model, dict):
            if not model.get('name'):
                raise ValueError("Model must have a name")
        else:
            if not model.name:
                raise ValueError("Model must have a name")
