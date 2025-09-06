from typing import Dict, Any, Union, List
from src.core.interfaces.code_generator import ICodeGenerator
from src.core.entities.schema import Model, Attribute ,Schema
from src.core.interfaces.template_renderer import ITemplateRenderer
from src.core.interfaces.config_loader import IConfigLoader
from src.utilities .string_utils import to_pascal_case, to_snake_case, pluralize

class NotificationGenerator(ICodeGenerator):
    def __init__(self, config_loader: IConfigLoader, template_renderer: ITemplateRenderer):
        self.config_loader = config_loader
        self.template_renderer = template_renderer

    
    def generate(self, schema: Schema) -> Dict[str, str]:
        generated_files = {}
        notification_types = ['Created', 'Updated', 'Deleted']

        for notification_type in notification_types:
            for model in schema.models:
                notification_content = self._generate_notification(model, notification_type)
                model_name = model['name'] if isinstance(model, dict) else model.name
                file_path = f"backend/app/Notifications/{model_name}{notification_type}Notification.php"
                generated_files[file_path] = notification_content
                
        return generated_files

    def get_output_path(self, model_name: str , notification_type) -> str:
        return f"backend/app/Notifications/{model_name}{notification_type}Notification.php"

    def render_template(self, template: str, context: Dict[str, Any]) -> str:
        return self.template_renderer.render(template, context)

    def _generate_notification(self, model: Union[Dict[str, Any], Model], notification_type: str) -> str:
        context = self.prepare_context(model, notification_type)
        template = self.get_template('notification')
        return self.template_renderer.render('backend/laravel/notification.stub', context)

    def prepare_context(self, model: Union[Dict[str, Any], Model], notification_type: str) -> Dict[str, Any]:
        model_name = model['name'] if isinstance(model, dict) else model.name
        attributes = model['attributes'] if isinstance(model, dict) else model.attributes

        return {
            'model_name': model_name,
            'notification_name': f"{model_name}{notification_type}Notification",
            'namespace': self.config_loader.get('notification_namespace', 'App\\Notifications'),
            'model_namespace': self.config_loader.get('model_namespace', 'App\\Models'),
            'attributes': attributes,
            'model_variable': to_snake_case(model_name),
            'notification_type': notification_type,
        }

    def get_template(self, template_name: str) -> str:
        template_path = self.config_loader.get('notification_template_path', 'backend/laravel/notification.stub')
        return self.template_renderer.load_template(template_path)

    def validate_model(self, model: Union[Dict[str, Any], Model]) -> None:
        if isinstance(model, dict):
            if not model.get('name') or not model.get('attributes'):
                raise ValueError("Model must have a name and attributes")
        else:
            if not model.name or not model.attributes:
                raise ValueError("Model must have a name and attributes")
